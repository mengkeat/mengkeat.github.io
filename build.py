"""
Static site generator. Converts Markdown to HTML.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class KaTeXPreprocessor(Preprocessor):
    """Protect math expressions from Markdown processing."""

    def run(self, lines):
        text = '\n'.join(lines)

        display_math = []
        def store_display(match):
            display_math.append(match.group(0))
            return f'DISPLAYMATH{len(display_math)-1}DISPLAYMATH'
        text = re.sub(r'\$\$[\s\S]*?\$\$', store_display, text)

        inline_math = []
        def store_inline(match):
            inline_math.append(match.group(0))
            return f'INLINEMATH{len(inline_math)-1}INLINEMATH'
        text = re.sub(r'\$(?!\$).*?\$', store_inline, text)

        self.display_math = display_math
        self.inline_math = inline_math
        return text.split('\n')


class KaTeXExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(KaTeXPreprocessor(md), 'katex', 27)


def restore_math(html: str, preprocessor) -> str:
    for i, math in enumerate(preprocessor.display_math):
        html = html.replace(f'DISPLAYMATH{i}DISPLAYMATH', math)
    for i, math in enumerate(preprocessor.inline_math):
        html = html.replace(f'INLINEMATH{i}INLINEMATH', math)
    return html


class SiteBuilder:
    def __init__(self):
        self.content_dir = Path("content")
        self.output_dir = Path("output")
        self.template_dir = Path("templates")
        self.static_dir = Path("static")

        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))
        self.env.globals['now'] = datetime.now()

        self.katex_ext = KaTeXExtension()
        self.md = markdown.Markdown(extensions=[
            'extra', 'codehilite', 'toc', 'fenced_code', self.katex_ext
        ])

        self.posts = []
        self.notes = []
        self.tags = defaultdict(list)

    def clean_output(self):
        if self.output_dir.exists():
            try:
                shutil.rmtree(self.output_dir)
            except PermissionError:
                for item in self.output_dir.iterdir():
                    if item.is_dir():
                        shutil.rmtree(item, ignore_errors=True)
                    else:
                        item.unlink(missing_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def copy_static(self):
        if self.static_dir.exists():
            shutil.copytree(self.static_dir, self.output_dir / "static")

    def parse_file(self, path: Path) -> dict:
        with open(path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        self.md.reset()
        preprocessor = self.md.preprocessors['katex']
        html = self.md.convert(post.content)
        html = restore_math(html, preprocessor)

        return {
            'title': post.get('title', 'Untitled'),
            'description': post.get('description', ''),
            'date': post.get('pubDate', datetime.now()),
            'tags': post.get('tags', []),
            'draft': post.get('draft', False),
            'content': html,
            'slug': path.stem,
        }

    def load_content(self):
        # Load blog posts
        blog_dir = self.content_dir / "blog"
        if blog_dir.exists():
            for md_file in sorted(blog_dir.glob("*.md")):
                post = self.parse_file(md_file)
                if not post['draft']:
                    post['type'] = 'blog'
                    post['url'] = f"/blog/{post['slug']}.html"
                    self.posts.append(post)
                    for tag in post['tags']:
                        self.tags[tag].append(post)

        # Load notes
        notes_dir = self.content_dir / "notes"
        if notes_dir.exists():
            for md_file in sorted(notes_dir.glob("*.md")):
                note = self.parse_file(md_file)
                if not note['draft']:
                    note['type'] = 'notes'
                    note['url'] = f"/notes/{note['slug']}.html"
                    self.notes.append(note)
                    for tag in note['tags']:
                        self.tags[tag].append(note)

        self.posts.sort(key=lambda x: x['date'], reverse=True)
        self.notes.sort(key=lambda x: x['date'], reverse=True)

    def render(self, template: str, path: Path, **context):
        html = self.env.get_template(template).render(**context)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding='utf-8')

    def build(self):
        print("Building site...")

        self.clean_output()
        self.load_content()
        print(f"  {len(self.posts)} posts, {len(self.notes)} notes")

        # Build posts
        for post in self.posts:
            self.render('post.html', self.output_dir / "blog" / f"{post['slug']}.html",
                       post=post)

        # Build notes
        for note in self.notes:
            self.render('post.html', self.output_dir / "notes" / f"{note['slug']}.html",
                       post=note)

        # Build indexes
        self.render('index.html', self.output_dir / "index.html", posts=self.posts, notes=self.notes)
        self.render('blog_index.html', self.output_dir / "blog" / "index.html", posts=self.posts)
        self.render('notes_index.html', self.output_dir / "notes" / "index.html", notes=self.notes)

        # Build tags
        tag_counts = {tag: len(items) for tag, items in self.tags.items()}
        sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
        self.render('tags.html', self.output_dir / "tags" / "index.html", tags=sorted_tags)

        for tag, items in self.tags.items():
            items_sorted = sorted(items, key=lambda x: x['date'], reverse=True)
            self.render('tag.html', self.output_dir / "tags" / f"{tag}.html",
                       tag=tag, items=items_sorted)

        self.copy_static()
        (self.output_dir / ".nojekyll").touch()

        print(f"Done. Output: {self.output_dir.absolute()}")


if __name__ == "__main__":
    SiteBuilder().build()
