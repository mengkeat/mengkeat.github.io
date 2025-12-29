# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Development:
- `python build.py` or `uv run python build.py` - Build static site to `output/` directory
- `python dev_server.py` or `uv run python dev_server.py` - Start development server at http://localhost:3000 with live reload

## Architecture

This is a personal blog and portfolio site built with a Python-based static site generator, featuring a dual-column layout showcasing both long-form blog posts and short "Today I Learned" (TIL) entries.

### Technology Stack

- **Python 3.11+**: Core language
- **Jinja2**: Template engine for HTML generation
- **Python-Frontmatter**: YAML frontmatter parsing
- **Markdown**: Content authoring with KaTeX extension for math
- **UV**: Fast Python package manager
- **Tailwind CSS**: Styling framework (via CDN)
- **KaTeX**: Mathematical notation rendering

### Project Structure

```
.
├── build.py              # Static site generator
├── dev_server.py         # Development server with live reload
├── content/              # Markdown content files
│   ├── blog/            # Blog posts
│   └── til/             # Today I Learned entries
├── templates/            # Jinja2 HTML templates
│   ├── base.html        # Base layout template
│   ├── index.html       # Homepage template
│   ├── blog_index.html  # Blog listing page
│   ├── til_index.html   # TIL listing page
│   ├── post.html        # Individual blog/TIL post
│   ├── tag.html         # Single tag page
│   └── tags.html        # All tags page
├── static/              # Static assets (CSS, images, favicon)
└── output/              # Generated static site (ignored in git)
```

### Key Components

- **Base Template** (`templates/base.html`): Main site layout with navigation, sidebar, and footer
- **Build Script** (`build.py`): Converts Markdown to HTML with KaTeX support
- **Dev Server** (`dev_server.py`): Watches for file changes and rebuilds automatically
- **Pages Structure**:
  - `/` - Homepage with featured blog posts and TIL entries
  - `/blog/` - Blog index and individual posts
  - `/til/` - Today I Learned entries
  - `/tags/` - Content organized by tags

### Content Architecture

- **Blog Posts**: Long-form articles in `content/blog/` (`.md` files)
- **TIL Entries**: Short learning snippets in `content/til/` (`.md` files)
- **Frontmatter**: Each content file has YAML frontmatter with title, date, tags, description
- **Mathematical Content**: Uses KaTeX for LaTeX-style equation rendering with custom preprocessor

### Styling

- **Tailwind CSS**: Primary styling framework (loaded via CDN)
- **Design System**: Clean, modern aesthetic with stone/amber color scheme
- **Responsive**: Mobile-first responsive design with sidebar that stacks on smaller screens
- **Fonts**: Inter font family from Google Fonts

### Mathematical Notation

The site supports mathematical notation through:
- KaTeX library for fast math rendering (loaded via CDN)
- Custom KaTeX preprocessor in build.py that protects math expressions
- Inline math: `$...$`
- Display math: `$$...$$`
- KaTeX CSS and JavaScript loaded in base template

### Deployment

- **GitHub Actions**: Automatic deployment to GitHub Pages on push to main branch
- **Workflow**: `.github/workflows/deploy.yml`
- **Build Process**:
  1. Install UV and Python dependencies
  2. Run `uv run python build.py`
  3. Upload `output/` directory to GitHub Pages
- **Static Output**: Site generates fully static HTML/CSS for optimal performance

### Development Notes

- All content files must have proper YAML frontmatter (title, date, tags, description)
- Mathematical content should use `$...$` for inline and `$$...$$` for display math
- New blog posts go in `content/blog/` with `.md` extension
- New TIL entries go in `content/til/` with `.md` extension
- Templates use Jinja2 syntax
- Static files in `static/` are copied directly to `output/static/`
- The `.nojekyll` file in output prevents GitHub Pages from treating it as a Jekyll site
- Development server watches for changes in `content/`, `templates/`, and `static/`

### Dependencies

Managed via UV package manager (see `pyproject.toml`):
- `jinja2` - Template engine
- `markdown` - Markdown processing
- `python-frontmatter` - Frontmatter parsing
- `watchdog` - File system watching for dev server
