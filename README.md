# Mengkeat's Digital Garden

A simple Python-based static site generator for a blog with KaTeX support for mathematical notation.

## Features

- **Simple Markdown-based content**: Write blog posts and TIL (Today I Learned) entries in Markdown
- **Frontmatter support**: Add metadata like title, date, tags, and more using YAML frontmatter
- **KaTeX integration**: Beautiful mathematical notation rendering with LaTeX syntax
- **Tag system**: Organize content by tags with automatic tag pages
- **Fast builds**: Pure Python with minimal dependencies
- **Live reload**: Development server with automatic rebuilds on file changes
- **GitHub Pages ready**: Automatic deployment via GitHub Actions

## Requirements

- Python 3.11 or higher
- [UV](https://github.com/astral-sh/uv) package manager

## Installation

1. Install UV (if you haven't already):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone this repository:

```bash
git clone https://github.com/mengkeat/mengkeat.github.io.git
cd mengkeat.github.io
```

3. Install dependencies:

```bash
uv sync
```

## Development

### Quick Start

Run the development server with live reload:

```bash
uv run python dev_server.py
```

This will:
- Build your site
- Start a local server at `http://localhost:8000`
- Watch for changes and rebuild automatically

To use a different port:

```bash
uv run python dev_server.py --port 3000
```

### Build Only

To build the site without starting a server:

```bash
uv run python build.py
```

The generated HTML files will be in the `output/` directory.

## Content Management

### Directory Structure

```
content/
├── blog/          # Blog posts
│   └── *.md
└── til/           # Today I Learned entries
    └── *.md
templates/         # Jinja2 templates
static/            # Static files (CSS, images, etc.)
output/            # Generated site (git-ignored)
```

### Writing Blog Posts

Create a new Markdown file in `content/blog/`:

```markdown
---
title: "My Blog Post Title"
description: "A short description of the post"
pubDate: 2025-01-15
author: "Your Name"
tags: ["python", "web-development"]
featured: false
draft: false
---

# My Blog Post Title

Your content here...

## Math Support

You can use inline math like $E = mc^2$ or display math:

$$
\int_a^b f(x) \, dx
$$
```

### Writing TIL Entries

Create a new Markdown file in `content/til/`:

```markdown
---
title: "Something I Learned Today"
description: "A quick note about what I learned"
pubDate: 2025-01-15
tags: ["python", "til"]
category: "Python"
draft: false
---

# Something I Learned Today

Quick explanation here...
```

### Frontmatter Fields

**Blog Posts:**
- `title` (required): Post title
- `description` (required): Short description
- `pubDate` (required): Publication date (YYYY-MM-DD)
- `author`: Author name (default: "Chris Meng")
- `tags`: Array of tags (default: [])
- `featured`: Boolean for featured posts (default: false)
- `draft`: Boolean to hide from site (default: false)
- `updatedDate`: Optional update date

**TIL Entries:**
- `title` (required): Entry title
- `description` (required): Short description
- `pubDate` (required): Publication date (YYYY-MM-DD)
- `tags`: Array of tags (default: [])
- `category`: Category name
- `draft`: Boolean to hide from site (default: false)

## Mathematical Notation

The blog supports KaTeX for rendering mathematical expressions:

### Inline Math

Use single dollar signs: `$x^2 + y^2 = z^2$` renders as $x^2 + y^2 = z^2$

### Display Math

Use double dollar signs:

```
$$
\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
```

### Advanced Math Features

- Greek letters: `$\alpha, \beta, \gamma$`
- Matrices: `$\begin{bmatrix} a & b \\ c & d \end{bmatrix}$`
- Summations: `$\sum_{i=1}^n i$`
- Integrals: `$\int_0^\infty e^{-x} dx$`
- And much more! See [KaTeX documentation](https://katex.org/docs/supported.html)

## Code Highlighting

Fenced code blocks are automatically highlighted:

```python
def hello_world():
    print("Hello, world!")
```

## Customization

### Templates

Templates are located in `templates/` and use Jinja2:

- `base.html`: Base layout with header, footer, and navigation
- `index.html`: Homepage
- `post.html`: Individual blog post/TIL page
- `blog_index.html`: Blog listing page
- `til_index.html`: TIL listing page
- `tags.html`: Tag index page
- `tag.html`: Individual tag page

### Styling

The site uses Tailwind CSS loaded via CDN. Styles are embedded in `templates/base.html`.

To customize:
1. Edit the Tailwind config in `templates/base.html`
2. Add custom CSS in the `<style>` section
3. Or create a separate CSS file in `static/css/`

## Deployment

### GitHub Pages

The site automatically deploys to GitHub Pages when you push to the `main` branch.

The workflow:
1. Builds the site using Python and UV
2. Uploads the `output/` directory
3. Deploys to GitHub Pages

See `.github/workflows/deploy.yml` for details.

### Manual Deployment

1. Build the site:
   ```bash
   uv run python build.py
   ```

2. Deploy the `output/` directory to any static hosting service:
   - GitHub Pages
   - Netlify
   - Vercel
   - AWS S3
   - etc.

## Extending the System

### Adding Marimo Notebook Support

The build system is designed to be extensible. To add Marimo notebook support:

1. Add marimo to `pyproject.toml`:
   ```toml
   dependencies = [
       # ... existing dependencies
       "marimo>=0.1.0",
   ]
   ```

2. Update `build.py` to handle `.py` or `.marimo` files:
   ```python
   def parse_marimo_notebook(self, file_path: Path) -> Dict[str, Any]:
       # Parse marimo notebook and convert to HTML
       pass
   ```

3. Create a new template `marimo.html` for notebook rendering

### Adding Other Content Types

Follow the same pattern as blog posts and TIL entries:

1. Create a new content directory (e.g., `content/projects/`)
2. Add parsing logic in `build.py`
3. Create corresponding templates
4. Add navigation links in `templates/base.html`

## Project Structure

```
.
├── build.py              # Main build script
├── dev_server.py         # Development server with live reload
├── pyproject.toml        # Python dependencies
├── content/              # Markdown content
│   ├── blog/
│   └── til/
├── templates/            # Jinja2 templates
│   ├── base.html
│   ├── index.html
│   ├── post.html
│   ├── blog_index.html
│   ├── til_index.html
│   ├── tags.html
│   └── tag.html
├── static/               # Static assets
└── output/               # Generated site (git-ignored)
```

## Troubleshooting

### Build Fails

1. Ensure you're using Python 3.11+:
   ```bash
   python --version
   ```

2. Check that all dependencies are installed:
   ```bash
   uv sync
   ```

3. Check for syntax errors in your Markdown files

### KaTeX Not Rendering

1. Check that you're using the correct delimiters (`$...$` or `$$...$$`)
2. Ensure the KaTeX CDN is accessible
3. Check browser console for JavaScript errors

### Live Reload Not Working

1. Ensure `watchdog` is installed:
   ```bash
   uv sync --all-extras
   ```

2. Check that you're editing files in `content/`, `templates/`, or `static/`

## License

MIT

## Credits

Built with:
- [Python](https://www.python.org/)
- [Jinja2](https://jinja.palletsprojects.com/)
- [Python-Markdown](https://python-markdown.github.io/)
- [Pygments](https://pygments.org/)
- [KaTeX](https://katex.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [UV](https://github.com/astral-sh/uv)
