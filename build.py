#!/usr/bin/env python3
"""
Simple static site generator for a blog with KaTeX support.
Converts Markdown files to HTML using Jinja2 templates.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any
from collections import defaultdict
import re

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class KaTeXPreprocessor(Preprocessor):
    """Preprocessor to protect KaTeX math expressions from Markdown processing."""

    def run(self, lines):
        text = '\n'.join(lines)

        # Store display math ($$...$$)
        display_math = []
        def store_display(match):
            display_math.append(match.group(0))
            return f'DISPLAYMATH{len(display_math)-1}DISPLAYMATH'

        text = re.sub(r'\$\$[\s\S]*?\$\$', store_display, text)

        # Store inline math ($...$)
        inline_math = []
        def store_inline(match):
            inline_math.append(match.group(0))
            return f'INLINEMATH{len(inline_math)-1}INLINEMATH'

        text = re.sub(r'\$(?!\$).*?\$', store_inline, text)

        # Store the math for later restoration
        self.display_math = display_math
        self.inline_math = inline_math

        return text.split('\n')


class KaTeXExtension(Extension):
    """Extension to add KaTeX support to Markdown."""

    def extendMarkdown(self, md):
        md.preprocessors.register(KaTeXPreprocessor(md), 'katex', 27)


def restore_math(html: str, preprocessor: KaTeXPreprocessor) -> str:
    """Restore KaTeX math expressions after Markdown processing."""
    # Restore display math
    for i, math in enumerate(preprocessor.display_math):
        html = html.replace(f'DISPLAYMATH{i}DISPLAYMATH', math)

    # Restore inline math
    for i, math in enumerate(preprocessor.inline_math):
        html = html.replace(f'INLINEMATH{i}INLINEMATH', math)

    return html


class SiteBuilder:
    def __init__(self, content_dir: Path = Path("content"),
                 output_dir: Path = Path("output"),
                 template_dir: Path = Path("templates"),
                 static_dir: Path = Path("static")):
        self.content_dir = content_dir
        self.output_dir = output_dir
        self.template_dir = template_dir
        self.static_dir = static_dir

        # Set up Jinja2 environment
        self.env = Environment(loader=FileSystemLoader(str(template_dir)))
        self.env.globals['now'] = datetime.now()

        # Set up Markdown processor
        self.katex_ext = KaTeXExtension()
        self.md = markdown.Markdown(extensions=[
            'extra',
            'codehilite',
            'toc',
            'fenced_code',
            self.katex_ext
        ])

        self.posts: List[Dict[str, Any]] = []
        self.tils: List[Dict[str, Any]] = []
        self.tags: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    def clean_output(self):
        """Remove existing output directory."""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True)

    def copy_static(self):
        """Copy static files to output directory."""
        if self.static_dir.exists():
            output_static = self.output_dir / "static"
            shutil.copytree(self.static_dir, output_static)

    def parse_markdown_file(self, file_path: Path) -> Dict[str, Any]:
        """Parse a markdown file with frontmatter."""
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        # Reset markdown processor for each file
        self.md.reset()

        # Get the preprocessor instance
        preprocessor = self.md.preprocessors['katex']

        # Convert markdown to HTML
        html_content = self.md.convert(post.content)

        # Restore KaTeX math
        html_content = restore_math(html_content, preprocessor)

        return {
            'title': post.get('title', 'Untitled'),
            'description': post.get('description', ''),
            'date': post.get('pubDate', datetime.now()),
            'updated': post.get('updatedDate'),
            'author': post.get('author', 'Chris Meng'),
            'tags': post.get('tags', []),
            'category': post.get('category', ''),
            'draft': post.get('draft', False),
            'featured': post.get('featured', False),
            'content': html_content,
            'slug': file_path.stem,
            'toc': self.md.toc if hasattr(self.md, 'toc') else ''
        }

    def load_content(self):
        """Load all blog posts and TIL entries."""
        # Load blog posts
        blog_dir = self.content_dir / "blog"
        if blog_dir.exists():
            for md_file in sorted(blog_dir.glob("*.md")):
                post = self.parse_markdown_file(md_file)
                if not post['draft']:
                    post['type'] = 'blog'
                    post['url'] = f"/blog/{post['slug']}.html"
                    self.posts.append(post)

                    # Add to tags
                    for tag in post['tags']:
                        self.tags[tag].append(post)

        # Load TIL entries
        til_dir = self.content_dir / "til"
        if til_dir.exists():
            for md_file in sorted(til_dir.glob("*.md")):
                til = self.parse_markdown_file(md_file)
                if not til['draft']:
                    til['type'] = 'til'
                    til['url'] = f"/til/{til['slug']}.html"
                    self.tils.append(til)

                    # Add to tags
                    for tag in til['tags']:
                        self.tags[tag].append(til)

        # Sort by date (newest first)
        self.posts.sort(key=lambda x: x['date'], reverse=True)
        self.tils.sort(key=lambda x: x['date'], reverse=True)

    def render_page(self, template_name: str, output_path: Path, **context):
        """Render a page using a template."""
        template = self.env.get_template(template_name)
        html = template.render(**context)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

    def build_posts(self):
        """Build individual blog post pages."""
        for post in self.posts:
            output_path = self.output_dir / "blog" / f"{post['slug']}.html"
            self.render_page('post.html', output_path, post=post, all_tags=sorted(self.tags.keys()))

    def build_tils(self):
        """Build individual TIL pages."""
        for til in self.tils:
            output_path = self.output_dir / "til" / f"{til['slug']}.html"
            self.render_page('post.html', output_path, post=til, all_tags=sorted(self.tags.keys()))

    def build_index(self):
        """Build the homepage."""
        recent_posts = self.posts[:4]
        recent_tils = self.tils[:2]

        self.render_page(
            'index.html',
            self.output_dir / "index.html",
            recent_posts=recent_posts,
            recent_tils=recent_tils,
            all_tags=sorted(self.tags.keys())
        )

    def build_blog_index(self):
        """Build the blog index page."""
        self.render_page(
            'blog_index.html',
            self.output_dir / "blog" / "index.html",
            posts=self.posts,
            all_tags=sorted(self.tags.keys())
        )

    def build_til_index(self):
        """Build the TIL index page."""
        self.render_page(
            'til_index.html',
            self.output_dir / "til" / "index.html",
            tils=self.tils,
            all_tags=sorted(self.tags.keys())
        )

    def build_tag_pages(self):
        """Build tag pages."""
        # Build tag index
        tag_counts = {tag: len(items) for tag, items in self.tags.items()}
        sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)

        self.render_page(
            'tags.html',
            self.output_dir / "tags" / "index.html",
            tags=sorted_tags,
            all_tags=sorted(self.tags.keys())
        )

        # Build individual tag pages
        for tag, items in self.tags.items():
            items_sorted = sorted(items, key=lambda x: x['date'], reverse=True)
            self.render_page(
                'tag.html',
                self.output_dir / "tags" / f"{tag}.html",
                tag=tag,
                items=items_sorted,
                all_tags=sorted(self.tags.keys())
            )

    def build(self):
        """Build the entire site."""
        print("🏗️  Building site...")

        print("  📁 Cleaning output directory...")
        self.clean_output()

        print("  📄 Loading content...")
        self.load_content()
        print(f"     Found {len(self.posts)} blog posts and {len(self.tils)} TIL entries")

        print("  📝 Building blog posts...")
        self.build_posts()

        print("  💡 Building TIL entries...")
        self.build_tils()

        print("  🏠 Building homepage...")
        self.build_index()

        print("  📚 Building blog index...")
        self.build_blog_index()

        print("  📚 Building TIL index...")
        self.build_til_index()

        print("  🏷️  Building tag pages...")
        self.build_tag_pages()

        print("  📦 Copying static files...")
        self.copy_static()

        print("✅ Build complete!")
        print(f"   Output: {self.output_dir.absolute()}")


def main():
    builder = SiteBuilder()
    builder.build()


if __name__ == "__main__":
    main()
