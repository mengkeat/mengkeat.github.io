# Project Overview

This is a Python-based static site generator for a personal blog and TIL (Today I Learned) collection.

## Technology Stack

- Python 3.11+
- UV package manager
- Jinja2 templates
- Markdown with Python-Markdown
- KaTeX for math rendering
- Tailwind CSS via CDN

## Directory Structure

- `content/` - Markdown content files
  - `content/blog/` - Blog posts
  - `content/til/` - TIL entries
- `templates/` - Jinja2 templates
- `static/` - Static assets (CSS, images, etc.)
- `output/` - Generated HTML (auto-created during build)
- `.venv/` - Python virtual environment (git-ignored)

## Key Files

- `build.py` - Main build script
- `dev_server.py` - Development server with live reload
- `pyproject.toml` - Python dependencies
- `QUICKSTART.md` - Quick reference guide
- `README.md` - Full documentation

## Features

✅ Blog posts with YAML frontmatter
✅ TIL (Today I Learned) entries
✅ Tag system and tag pages
✅ KaTeX math rendering
✅ Code syntax highlighting
✅ Responsive design
✅ GitHub Pages deployment
✅ Live reload development server
✅ Homepage with recent posts

## Development Workflow

```bash
uv sync                          # Install dependencies
uv run python dev_server.py      # Start dev server with live reload
uv run python build.py           # Build for production
```

## Deployment

The site automatically deploys to GitHub Pages when you push to the `main` branch:
- GitHub Actions uses Python 3.11 + UV
- Runs `uv sync` and `uv run python build.py`
- Deploys `output/` directory

## Testing Checklist

When making changes, verify:

- [ ] Run `uv run python build.py` - builds successfully
- [ ] Run `uv run python dev_server.py` - server starts
- [ ] Visit http://localhost:8000 - homepage loads
- [ ] Check blog posts - all posts visible and render correctly
- [ ] Check TIL entries - all TILs visible and render correctly
- [ ] Check tags - tag pages work
- [ ] Check math rendering - KaTeX equations display correctly
- [ ] Check code highlighting - code blocks are highlighted
- [ ] Push to GitHub - deployment works
- [ ] Visit your GitHub Pages URL - live site works

## Extending the System

The Python-based system is designed to be easily extended.

### Adding New Content Types

Follow the pattern in `build.py`:
1. Add parsing method for the new content type
2. Add build method to generate HTML
3. Create Jinja2 template
4. Update navigation/index pages as needed

Example structure:
```python
# build.py
def parse_new_type(self, file_path: Path):
    # Parse your content
    pass

def build_new_type(self):
    # Generate HTML
    pass
```

### Adding New Features

Common extensions:
- RSS feed generation
- Search functionality
- Related posts
- Comment system integration
- Analytics
- Dark mode toggle

## Troubleshooting

### "command not found: uv"
Install UV: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### "No module named 'frontmatter'"
Run: `uv sync`

### Build fails with Python errors
Check Python version: `python --version` (need 3.11+)

### Math not rendering
- Check `$` delimiters in markdown
- Open browser console for JavaScript errors
- Verify KaTeX CDN is accessible

### Old site still showing on GitHub Pages
- Check GitHub Actions - build should be using Python
- Clear browser cache
- Wait a few minutes for deployment

## Resources

- **Documentation**: See [README.md](README.md) for full details
- **Quick Start**: See [QUICKSTART.md](QUICKSTART.md) for common tasks
- **Issues**: Open an issue on GitHub if you encounter problems
