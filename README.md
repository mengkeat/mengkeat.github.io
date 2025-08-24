# mengkeat.github.io — Astro site

This repository contains a minimal Astro site that automatically deploys to GitHub Pages via GitHub Actions.

## Local development (Windows cmd.exe)

```cmd
cd /d D:\Code\mengkeat.github.io
npm install
npm run dev
```

Visit http://localhost:3000 to see your site.

## Deployment

The site automatically deploys to GitHub Pages when you push to the `main` branch:

1. GitHub Action builds the site from source
2. Deploys the built files to the `gh-pages` branch  
3. GitHub Pages serves from the `gh-pages` branch

## Setup steps

1. Push this repo to GitHub as `mengkeat/mengkeat.github.io`
2. In GitHub repo Settings → Pages → Source: "GitHub Actions"
3. Push to main branch to trigger deployment
4. Site will be live at https://mengkeat.github.io

## Build locally

```cmd
npm run build
```

Built files go to `dist/` (not tracked in git).
