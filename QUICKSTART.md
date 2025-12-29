# Quick Start Guide

## First Time Setup

1. **Install UV** (Python package manager):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/yourusername/mengkeat.github.io.git
   cd mengkeat.github.io
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

## Development

**Start development server** (with live reload):
```bash
uv run python dev_server.py
```

Visit http://localhost:8000 to see your site.

The server will automatically rebuild when you edit files in:
- `content/` - Your blog posts and TIL entries
- `templates/` - Jinja2 templates
- `static/` - Static assets

Press `Ctrl+C` to stop the server.

## Building

**Build the site** (without server):
```bash
uv run python build.py
```

Output goes to `output/` directory. You can open `output/index.html` in a browser to preview.

## Writing Content

### New Blog Post

Create `content/blog/my-post.md`:

```markdown
---
title: "My Post Title"
description: "Short description"
pubDate: 2025-01-15
tags: ["python", "web"]
---

# My Post Title

Content goes here...

Math: $E = mc^2$

$$
\int_a^b f(x) \, dx
$$
```

### New TIL Entry

Create `content/til/my-til.md`:

```markdown
---
title: "Today I Learned Something"
description: "Quick note"
pubDate: 2025-01-15
tags: ["python"]
category: "Python"
---

Quick explanation...
```

## Deployment

**Automatic deployment to GitHub Pages:**
1. Push your changes to the `main` branch:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

2. GitHub Actions will automatically:
   - Build the site using `uv run python build.py`
   - Deploy the `output/` directory to GitHub Pages
   - Your site will be live at `https://yourusername.github.io`

**Check deployment status:**
- Visit your repository's "Actions" tab on GitHub
- Look for the latest workflow run

## Common Tasks

**Add a new dependency:**
```bash
uv add package-name
```

**Update dependencies:**
```bash
uv sync --upgrade
```

**View installed packages:**
```bash
uv pip list
```

**Clean build artifacts:**
```bash
rm -rf output/
```

## Troubleshooting

**"command not found: uv"**
- Install UV: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Restart your terminal
- Verify installation: `uv --version`

**Build fails?**
- Check Python version: `python --version` (need 3.11+)
- Reinstall dependencies: `uv sync`
- Check for syntax errors in your markdown files

**Math not rendering?**
- Use `$...$` for inline math (e.g., `$E = mc^2$`)
- Use `$$...$$` for display math on separate lines
- Check browser console for JavaScript errors
- Verify KaTeX CDN is accessible

**Server not updating?**
- Make sure you saved your files
- Check terminal for build errors
- Try restarting the server (Ctrl+C, then restart)

**Port 8000 already in use?**
- Find and kill the process: `lsof -ti:8000 | xargs kill -9`
- Or use a different port by modifying `dev_server.py`

**Deployment not working?**
- Check GitHub Actions logs in your repository
- Verify `.github/workflows/deploy.yml` is correct
- Ensure GitHub Pages is enabled in repository settings

## Project Structure

```
content/blog/       ← Blog posts (*.md)
content/til/        ← TIL entries (*.md)
templates/          ← Jinja2 templates
static/             ← CSS, images, etc.
output/             ← Generated site (auto-created)
```

## Next Steps

- Read the full [README.md](README.md) for more details
- Customize templates in `templates/`
- Add static assets to `static/`
- Write more content in `content/`
