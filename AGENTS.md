# AGENTS.md

This file provides guidance for AI assistants working on this repository.

## Commands

- `uv run python build.py` - Build static site
- `uv run python dev_server.py` - Start dev server at http://localhost:8000

## Architecture

Minimalist static site generator with Python.

### Project Structure

```
├── build.py              # Site generator
├── dev_server.py         # Dev server with live reload
├── content/
│   ├── blog/            # Blog posts (*.md)
│   └── notes/           # Short notes (*.md)
├── templates/            # Jinja2 templates
│   ├── base.html        # Base layout
│   ├── index.html       # Homepage
│   ├── post.html        # Single post page
│   ├── blog_index.html  # Blog listing
│   ├── notes_index.html # Notes listing
│   ├── tags.html        # All tags
│   └── tag.html         # Single tag
├── static/              # Static assets
└── output/              # Generated site (git-ignored)
```

### Content Format

Markdown files with YAML frontmatter:

```yaml
---
title: "Post Title"
description: "Short description"
pubDate: 2025-01-15
tags: ["python", "web"]
draft: false
---

Content here...
```

### Design

- Single-column minimalist layout
- Clean typography, no clutter
- Homepage shows all content (posts + notes) combined
- Posts at `/blog/`, notes at `/notes/`
- Tags for organization

### Tech Stack

- Python 3.11+
- Jinja2 templates
- Python-Frontmatter
- Markdown with KaTeX for math
- Plain CSS (no frameworks)
