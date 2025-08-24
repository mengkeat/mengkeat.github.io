# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Development:
- `npm run dev` - Start development server at http://localhost:3000
- `npm run build` - Build static site to `dist/` directory 
- `npm run preview` - Preview built site locally

## Architecture

This is a personal blog and portfolio site built with Astro, featuring a dual-column layout showcasing both long-form blog posts and short "Today I Learned" (TIL) entries.

### Key Components

- **BaseLayout** (`src/layouts/BaseLayout.astro`): Main site template with navigation, sidebar, and footer
- **KaTeX Component** (`src/components/KaTeX.astro`): Renders LaTeX mathematical expressions using KaTeX
- **Pages Structure**:
  - `/` - Homepage with featured blog posts and TIL entries
  - `/blog/` - Blog index and individual posts
  - `/til` - Today I Learned entries
  - `/tags` - Content organized by tags

### Content Architecture

- **Blog Posts**: Long-form articles in `src/pages/blog/` (`.astro` files)
- **TIL Entries**: Short learning snippets (currently hardcoded in homepage)
- **Mathematical Content**: Uses KaTeX for LaTeX-style equation rendering with remark-math and rehype-katex plugins

### Styling

- **Tailwind CSS**: Primary styling framework with custom configuration
- **Design System**: Clean, modern aesthetic with gray/blue color scheme
- **Responsive**: Mobile-first responsive design with sidebar that stacks on smaller screens

### Mathematical Notation

The site supports mathematical notation through:
- KaTeX library for fast math rendering
- Remark-math and rehype-katex for markdown processing
- Custom KaTeX component for inline and display math
- CDN stylesheet loaded in BaseLayout for consistent styling

### Deployment

- **GitHub Actions**: Automatic deployment to GitHub Pages on push to main branch
- **Static Output**: Site generates static files for optimal performance
- **Node.js 20**: Uses npm for dependency management

### Development Notes

- All mathematical content should use the KaTeX component for consistency
- New blog posts should follow the existing `.astro` file pattern in `src/pages/blog/`
- Maintain the existing Tailwind class naming conventions
- KaTeX CSS is loaded via CDN in the BaseLayout head section