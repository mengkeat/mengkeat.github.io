# Quick Start

## Setup

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

## Development

```bash
# Start dev server (auto-reload)
uv run python dev_server.py

# Build only
uv run python build.py
```

## Adding Content

**Blog post:**
```bash
# Create content/blog/my-title.md with frontmatter:
---
title: "My Title"
description: "Description"
pubDate: 2025-01-15
tags: ["tag1", "tag2"]
---

Your markdown content here.
```

**Note:**
```bash
# Create content/notes/my-note.md (same format)
```

## Deploy

```bash
git add .
git commit -m "Add new post"
git push origin main
```

GitHub Actions auto-deploys to Pages.

## Frontmatter Fields

- `title` - Post title (required)
- `description` - Short description (required)
- `pubDate` - Date as YYYY-MM-DD (required)
- `tags` - Array of tags
- `draft` - Set `true` to hide from site
