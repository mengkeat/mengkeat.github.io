# mengkeat.github.io

Minimalist personal blog built with Python.

## Quick Start

```bash
# Install UV (if needed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Build site
uv run python build.py

# Dev server with live reload
uv run python dev_server.py
```

Site will be at `http://localhost:8000`. Output goes to `output/`.

## Writing Content

### Blog Posts

Create `content/blog/my-post.md`:

```markdown
---
title: "My Post"
description: "Short description"
pubDate: 2025-01-15
tags: ["python"]
---

Content here. Math: $E = mc^2$

$$
\int_a^b f(x) \, dx
$$
```

### Notes

Create `content/notes/my-note.md`:

```markdown
---
title: "Quick Note"
description: "Brief note"
pubDate: 2025-01-15
tags: ["tips"]
---

Short content...
```

## Project Structure

| Path | Description |
|------|-------------|
| `content/blog/` | Blog posts |
| `content/notes/` | Short notes |
| `templates/` | Jinja2 templates |
| `static/` | Assets (images, etc.) |
| `output/` | Generated site |

## Deployment

Push to `main` branch. GitHub Actions builds and deploys to GitHub Pages automatically.

## Math Support

KaTeX is included. Use `$...$` for inline and `$$...$$` for display math.
