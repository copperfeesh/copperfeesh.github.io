# copperfish.net (`copperfeesh.github.io`)

The personal website and technical blog of [Garron Stevenson](https://copperfish.net), hosted on GitHub Pages.

Designed with a modern, monochrome "Soft Gray" aesthetic, system typography, native dark mode support, and zero JavaScript framework overhead.

---

## Quick Start

### 1. Requirements
- Python 3.8+ (with `markdown` and `pyyaml`)

```bash
pip install -r requirements.txt
```

### 2. Local Preview
Start a local HTTP server:

```bash
python -m http.server 8000
```

Open `http://localhost:8000` in your browser.

---

## Writing a New Blog Post

1. Create a new markdown file in `content/posts/<post-slug>.md`.
2. Add frontmatter metadata at the top:

```markdown
---
title: "Your Post Title"
date: "2026-10-16"
slug: "your-post-slug"
excerpt: "A brief 1-2 sentence preview for the home page index..."
description: "A short SEO meta description for search engines and social cards."
tags:
  - homelab
  - docker
---

Write your article here in standard Markdown.

Code blocks with syntax highlighting:

```bash
echo "Hello world"
```
```

3. Rebuild the site:

```bash
python build.py
```

`build.py` automatically generates:
- The compiled HTML page: `blog/<post-slug>.html`
- The homepage listing in `index.html` (sorted by date descending)
- The RSS 2.0 feed in `feed.xml`
- Search engine sitemap in `sitemap.xml`
- `robots.txt`

4. Commit and push:

```bash
git add .
git commit -m "feat: add new post on ..."
git push origin main
```

GitHub Pages will deploy your updates live to [copperfish.net](https://copperfish.net).

---

## Features

- **Zero-Friction Publishing**: Write posts in clean Markdown files with YAML frontmatter.
- **Dark Mode**: System-aware (`prefers-color-scheme`) with manual toggle button in the sidebar (persisted in `localStorage`, zero theme flash on load).
- **SEO & Social Sharing**: Complete Open Graph (`og:*`), Twitter Cards, author tags, and canonical links.
- **Feeds & Discovery**: Automated RSS 2.0 feed (`feed.xml`), `sitemap.xml`, and `robots.txt`.
- **Favicon**: Minimalist vector copper fish SVG icon (`assets/favicon.svg`).
- **Code Highlighting**: Syntax-highlighted code blocks powered by Highlight.js (`github-dark` theme).
