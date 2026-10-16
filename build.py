#!/usr/bin/env python3
"""
Static site generator for copperfish.net (copperfeesh.github.io).
Reads markdown posts from content/posts/, renders HTML, generates RSS feed (feed.xml),
and sitemap.xml.
"""

import sys
import re
from pathlib import Path
from datetime import datetime, timezone

try:
    import yaml
except ImportError:
    yaml = None

try:
    import markdown
except ImportError:
    markdown = None

BASE_URL = "https://copperfish.net"
SITE_TITLE = "Garron Stevenson"
SITE_DESCRIPTION = (
    "Personal blog and technical notes by Garron Stevenson on self-hosting, homelab, and software engineering."
)

ROOT_DIR = Path(__file__).resolve().parent
CONTENT_DIR = ROOT_DIR / "content" / "posts"
TEMPLATES_DIR = ROOT_DIR / "templates"
BLOG_DIR = ROOT_DIR / "blog"


def parse_frontmatter(file_path: Path):
    text = file_path.read_text(encoding="utf-8")
    frontmatter = {}
    body = text

    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            body = parts[2].strip()
            if yaml:
                frontmatter = yaml.safe_load(fm_text) or {}
            else:
                # Basic key-value parser fallback
                for line in fm_text.splitlines():
                    if ":" in line:
                        k, v = line.split(":", 1)
                        frontmatter[k.strip()] = v.strip().strip("\"'")

    return frontmatter, body


def format_display_date(date_obj) -> str:
    """Format e.g. 2026-06-08 into 'June 8, 2026'."""
    if isinstance(date_obj, str):
        try:
            date_obj = datetime.fromisoformat(date_obj).date()
        except ValueError:
            return date_obj
    return f"{date_obj.strftime('%B')} {date_obj.day}, {date_obj.year}"


def format_iso_date(date_obj) -> str:
    if isinstance(date_obj, str):
        return date_obj
    return date_obj.strftime("%Y-%m-%d")


def format_rfc822_date(date_obj) -> str:
    if isinstance(date_obj, str):
        try:
            date_obj = datetime.fromisoformat(date_obj)
        except ValueError:
            return date_obj
    if not isinstance(date_obj, datetime):
        date_obj = datetime.combine(date_obj, datetime.min.time(), tzinfo=timezone.utc)
    elif date_obj.tzinfo is None:
        date_obj = date_obj.replace(tzinfo=timezone.utc)
    return date_obj.strftime("%a, %d %b %Y %H:%M:%S %z")


def markdown_to_html(md_text: str) -> str:
    if markdown:
        return markdown.markdown(
            md_text,
            extensions=["fenced_code", "tables", "attr_list", "nl2br"]
        )
    # Basic fallback if markdown module is absent
    paragraphs = md_text.split("\n\n")
    html_parts = []
    for p in paragraphs:
        p = p.strip()
        if p.startswith("```"):
            lines = p.splitlines()
            lang = lines[0].replace("```", "").strip() or "text"
            code = "\n".join(lines[1:-1])
            html_parts.append(f'<pre><code class="language-{lang}">{code}</code></pre>')
        elif p.startswith("# "):
            html_parts.append(f"<h1>{p[2:]}</h1>")
        elif p.startswith("## "):
            html_parts.append(f"<h2>{p[3:]}</h2>")
        elif p.startswith("### "):
            html_parts.append(f"<h3>{p[4:]}</h3>")
        else:
            html_parts.append(f"<p>{p}</p>")
    return "\n".join(html_parts)


def build():
    print(f"Building site for {SITE_TITLE} ({BASE_URL})...")

    # Load templates
    sidebar_template = (TEMPLATES_DIR / "partials" / "sidebar.html").read_text(encoding="utf-8")
    index_template = (TEMPLATES_DIR / "index.html").read_text(encoding="utf-8")
    post_template = (TEMPLATES_DIR / "post.html").read_text(encoding="utf-8")

    BLOG_DIR.mkdir(parents=True, exist_ok=True)

    posts = []
    if CONTENT_DIR.exists():
        for md_file in CONTENT_DIR.glob("*.md"):
            fm, body = parse_frontmatter(md_file)
            slug = fm.get("slug") or md_file.stem
            title = fm.get("title", slug.replace("-", " ").title())
            date_raw = fm.get("date", datetime.now().date())
            excerpt = fm.get("excerpt", "")
            description = fm.get("description") or excerpt or SITE_DESCRIPTION
            tags = fm.get("tags", [])

            html_content = markdown_to_html(body)

            posts.append({
                "slug": slug,
                "title": title,
                "date_raw": date_raw,
                "formatted_date": format_display_date(date_raw),
                "iso_date": format_iso_date(date_raw),
                "rfc822_date": format_rfc822_date(date_raw),
                "excerpt": excerpt,
                "description": description,
                "tags": tags,
                "html_content": html_content,
            })

    # Sort posts descending by date
    posts.sort(key=lambda p: str(p["iso_date"]), reverse=True)
    print(f"Found {len(posts)} post(s).")

    # 1. Render Blog Posts
    sidebar_post = sidebar_template.replace("{{root}}", "../")
    for post in posts:
        post_url = f"{BASE_URL}/blog/{post['slug']}.html"
        rendered = post_template
        rendered = rendered.replace("{{title}}", post["title"])
        rendered = rendered.replace("{{description}}", post["description"])
        rendered = rendered.replace("{{canonical_url}}", post_url)
        rendered = rendered.replace("{{iso_date}}", post["iso_date"])
        rendered = rendered.replace("{{formatted_date}}", post["formatted_date"])
        rendered = rendered.replace("{{content}}", post["html_content"])
        rendered = rendered.replace("{{sidebar}}", sidebar_post)

        out_path = BLOG_DIR / f"{post['slug']}.html"
        out_path.write_text(rendered, encoding="utf-8")
        print(f"  -> Generated {out_path.relative_to(ROOT_DIR)}")

    # 2. Render Index Page
    sidebar_index = sidebar_template.replace("{{root}}", "")
    posts_list_html = []
    for post in posts:
        item = (
            f'                <article class="post-item">\n'
            f'                    <time class="post-date">{post["formatted_date"]}</time>\n'
            f'                    <h2 class="post-title"><a href="blog/{post["slug"]}.html">{post["title"]}</a></h2>\n'
            f'                    <p class="post-excerpt">{post["excerpt"]}</p>\n'
            f'                    <a href="blog/{post["slug"]}.html" class="read-more">Read More</a>\n'
            f'                </article>'
        )
        posts_list_html.append(item)

    index_html = index_template
    index_html = index_html.replace("{{sidebar}}", sidebar_index)
    index_html = index_html.replace("{{posts_list}}", "\n".join(posts_list_html))

    index_path = ROOT_DIR / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    print(f"  -> Generated {index_path.relative_to(ROOT_DIR)}")

    # 3. Generate RSS Feed (feed.xml)
    current_time_rfc = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S %z")
    feed_items = []
    for post in posts:
        post_link = f"{BASE_URL}/blog/{post['slug']}.html"
        item_xml = (
            f"    <item>\n"
            f"      <title>{post['title']}</title>\n"
            f"      <link>{post_link}</link>\n"
            f"      <guid>{post_link}</guid>\n"
            f"      <pubDate>{post['rfc822_date']}</pubDate>\n"
            f"      <description><![CDATA[{post['excerpt']}]]></description>\n"
            f"    </item>"
        )
        feed_items.append(item_xml)

    feed_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{SITE_TITLE}</title>
    <link>{BASE_URL}/</link>
    <description>{SITE_DESCRIPTION}</description>
    <language>en-us</language>
    <lastBuildDate>{current_time_rfc}</lastBuildDate>
    <atom:link href="{BASE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
{chr(10).join(feed_items)}
  </channel>
</rss>
"""
    feed_path = ROOT_DIR / "feed.xml"
    feed_path.write_text(feed_xml, encoding="utf-8")
    print(f"  -> Generated {feed_path.relative_to(ROOT_DIR)}")

    # 4. Generate Sitemap (sitemap.xml)
    latest_date = posts[0]["iso_date"] if posts else datetime.now().strftime("%Y-%m-%d")
    sitemap_entries = [
        f"  <url>\n"
        f"    <loc>{BASE_URL}/</loc>\n"
        f"    <lastmod>{latest_date}</lastmod>\n"
        f"    <changefreq>weekly</changefreq>\n"
        f"    <priority>1.0</priority>\n"
        f"  </url>"
    ]
    for post in posts:
        sitemap_entries.append(
            f"  <url>\n"
            f"    <loc>{BASE_URL}/blog/{post['slug']}.html</loc>\n"
            f"    <lastmod>{post['iso_date']}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>0.8</priority>\n"
            f"  </url>"
        )

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_entries)}
</urlset>
"""
    sitemap_path = ROOT_DIR / "sitemap.xml"
    sitemap_path.write_text(sitemap_xml, encoding="utf-8")
    print(f"  -> Generated {sitemap_path.relative_to(ROOT_DIR)}")

    # 5. Generate robots.txt
    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    robots_path = ROOT_DIR / "robots.txt"
    robots_path.write_text(robots_txt, encoding="utf-8")
    print(f"  -> Generated {robots_path.relative_to(ROOT_DIR)}")

    print("Build complete!")


if __name__ == "__main__":
    build()
