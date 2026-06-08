# Personal Blog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a minimal, monochrome personal blog with an asymmetric split layout on GitHub Pages.

**Architecture:** A static website using HTML5 and Vanilla CSS. Layout features a fixed left sidebar for navigation/branding and a scrolling right column for content.

**Tech Stack:** HTML5, CSS3, SVG Icons, Formspree.

---

### Task 1: Setup Foundation & CSS Variables

**Files:**
- Modify: `css/style.css`
- Modify: `index.html`

- [ ] **Step 1: Define CSS Variables and Reset in css/style.css**

```css
:root {
  --bg-main: #fafafa;
  --bg-sidebar: #ffffff;
  --text-primary: #111111;
  --text-secondary: #555555;
  --text-muted: #888888;
  --border-color: #eaeaea;
  --sidebar-width: 280px;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background-color: var(--bg-main);
  color: var(--text-primary);
  line-height: 1.6;
}
```

- [ ] **Step 2: Update index.html with basic structure**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Garron Stevenson</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="layout">
        <aside class="sidebar" id="sidebar"></aside>
        <main class="content" id="content"></main>
    </div>
</body>
</html>
```

- [ ] **Step 3: Commit**

```bash
git add css/style.css index.html
git commit -m "chore: setup foundation and css variables"
```

### Task 2: Implement Shared Sidebar

**Files:**
- Modify: `css/style.css`
- Modify: `index.html`

- [ ] **Step 1: Style the Asymmetric Layout and Sidebar in css/style.css**

```css
.layout {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: var(--sidebar-width);
  background-color: var(--bg-sidebar);
  border-right: 1px solid var(--border-color);
  padding: 60px 40px;
  position: fixed;
  height: 100vh;
  display: flex; flex-direction: column;
}

.content {
  margin-left: var(--sidebar-width);
  flex: 1;
  padding: 80px 100px;
}

@media (max-width: 768px) {
  .layout {
    flex-direction: column;
  }
  .sidebar {
    width: 100%;
    height: auto;
    position: relative;
    padding: 30px 20px;
    border-right: none;
    border-bottom: 1px solid var(--border-color);
  }
  .content {
    margin-left: 0;
    padding: 40px 20px;
  }
}
```

- [ ] **Step 2: Add Sidebar Content to index.html**

```html
<aside class="sidebar">
    <h1 class="branding"><a href="index.html">Garron Stevenson</a></h1>
    <nav class="nav">
        <a href="index.html" class="nav-link active">Blog</a>
        <a href="contact.html" class="nav-link">Contact</a>
    </nav>
    <div class="social-links">
        <a href="https://github.com/copperfeesh" title="GitHub">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
        </a>
        <a href="https://www.linkedin.com/in/garronstevenson/" title="LinkedIn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
        <a href="https://bsky.app/profile/copperfish.net" title="BlueSky">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 16s-2-2.5-2-4c0-1.5 1-2.5 2-2.5s2 1 2 2.5c0 1.5-2 4-2 4z"></path></svg>
        </a>
    </div>
</aside>
```

- [ ] **Step 3: Add Sidebar Styling to css/style.css**

```css
.branding a {
  text-decoration: none;
  color: var(--text-primary);
  font-size: 1.4rem;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.nav {
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  flex-grow: 1;
}

.nav-link {
  text-decoration: none;
  color: var(--text-secondary);
  font-size: 0.95rem;
  transition: color 0.2s;
}

.nav-link:hover, .nav-link.active {
  color: var(--text-primary);
  font-weight: 500;
}

.social-links {
  display: flex;
  gap: 16px;
  margin-top: 40px;
}

.social-links a {
  color: var(--text-muted);
  transition: color 0.2s;
}

.social-links a:hover {
  color: var(--text-primary);
}
```

- [ ] **Step 4: Commit**

```bash
git add css/style.css index.html
git commit -m "feat: implement shared sidebar with navigation and social links"
```

### Task 3: Implement Main Blog List (Homepage)

**Files:**
- Modify: `index.html`
- Modify: `css/style.css`

- [ ] **Step 1: Add Post List Styling to css/style.css**

```css
.posts {
  max-width: 650px;
}

.post-item {
  margin-bottom: 80px;
}

.post-date {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  display: block;
  margin-bottom: 8px;
}

.post-title {
  font-size: 1.8rem;
  margin-bottom: 16px;
  font-weight: 600;
}

.post-title a {
  text-decoration: none;
  color: var(--text-primary);
}

.post-excerpt {
  color: var(--text-secondary);
  font-size: 1.05rem;
  margin-bottom: 20px;
}

.read-more {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text-primary);
  text-decoration: underline;
  text-underline-offset: 4px;
}
```

- [ ] **Step 2: Add Placeholder Posts to index.html**

```html
<main class="content">
    <div class="posts">
        <article class="post-item">
            <time class="post-date">June 8, 2026</time>
            <h2 class="post-title"><a href="blog/monochrome-beauty.html">The Beauty of Monochrome</a></h2>
            <p class="post-excerpt">Exploring why restricted color palettes often lead to more focused and professional-looking designs in the modern web...</p>
            <a href="blog/monochrome-beauty.html" class="read-more">Read More</a>
        </article>

        <article class="post-item">
            <time class="post-date">June 1, 2026</time>
            <h2 class="post-title"><a href="blog/static-performance.html">Static Site Performance</a></h2>
            <p class="post-excerpt">Why I decided to stick with pure HTML and CSS for my personal site instead of using a heavy framework...</p>
            <a href="blog/static-performance.html" class="read-more">Read More</a>
        </article>
    </div>
</main>
```

- [ ] **Step 3: Commit**

```bash
git add index.html css/style.css
git commit -m "feat: implement blog post list on homepage"
```

### Task 4: Implement Contact Page

**Files:**
- Create: `contact.html`
- Modify: `css/style.css`

- [ ] **Step 1: Create contact.html with Formspree Integration**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact | Garron Stevenson</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="layout">
        <aside class="sidebar">
            <h1 class="branding"><a href="index.html">Garron Stevenson</a></h1>
            <nav class="nav">
                <a href="index.html" class="nav-link">Blog</a>
                <a href="contact.html" class="nav-link active">Contact</a>
            </nav>
            <div class="social-links">
                <a href="https://github.com/copperfeesh" title="GitHub">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                </a>
                <a href="https://www.linkedin.com/in/garronstevenson/" title="LinkedIn">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                </a>
                <a href="https://bsky.app/profile/copperfish.net" title="BlueSky">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 16s-2-2.5-2-4c0-1.5 1-2.5 2-2.5s2 1 2 2.5c0 1.5-2 4-2 4z"></path></svg>
                </a>
            </div>
        </aside>
        <main class="content">
            <div class="contact-container">
                <h1 class="page-title">Get in Touch</h1>
                <p class="subtitle">Have a question or just want to say hi? Fill out the form below and I'll get back to you as soon as I can.</p>
                
                <form action="https://formspree.io/f/your-id" method="POST" class="contact-form">
                    <div class="form-group">
                        <label for="name">Name</label>
                        <input type="text" name="name" id="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" name="email" id="email" required>
                    </div>
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea name="message" id="message" rows="6" required></textarea>
                    </div>
                    <button type="submit" class="submit-btn">Send Message</button>
                </form>
            </div>
        </main>
    </div>
</body>
</html>
```

- [ ] **Step 2: Add Contact Form Styling to css/style.css**

```css
.contact-container {
  max-width: 500px;
}

.page-title {
  font-size: 2.2rem;
  margin-bottom: 12px;
}

.subtitle {
  color: var(--text-secondary);
  margin-bottom: 40px;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text-primary);
}

.form-group input, .form-group textarea {
  padding: 12px;
  border: 1px solid var(--border-color);
  background: white;
  font-family: inherit;
  font-size: 1rem;
  border-radius: 4px;
}

.form-group input:focus, .form-group textarea:focus {
  outline: none;
  border-color: var(--text-muted);
}

.submit-btn {
  background: var(--text-primary);
  color: white;
  border: none;
  padding: 14px 20px;
  font-size: 1rem;
  font-weight: 500;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s;
  align-self: flex-start;
}

.submit-btn:hover {
  opacity: 0.9;
}
```

- [ ] **Step 3: Commit**

```bash
git add contact.html css/style.css
git commit -m "feat: implement contact page with formspree"
```

### Task 5: Implement Blog Post Template & First Posts

**Files:**
- Create: `blog/monochrome-beauty.html`
- Create: `blog/static-performance.html`
- Modify: `css/style.css`

- [ ] **Step 1: Add Blog Post Styling to css/style.css**

```css
.post-content {
  max-width: 650px;
}

.post-header {
  margin-bottom: 40px;
}

.post-body {
  font-size: 1.1rem;
  color: var(--text-secondary);
}

.post-body p {
  margin-bottom: 24px;
}

.back-link {
  display: inline-block;
  margin-bottom: 40px;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.9rem;
}

.back-link:hover {
  color: var(--text-primary);
}
```

- [ ] **Step 2: Create blog/monochrome-beauty.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Beauty of Monochrome | Garron Stevenson</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="layout">
        <aside class="sidebar">
            <h1 class="branding"><a href="../index.html">Garron Stevenson</a></h1>
            <nav class="nav">
                <a href="../index.html" class="nav-link active">Blog</a>
                <a href="../contact.html" class="nav-link">Contact</a>
            </nav>
            <div class="social-links">
                <a href="https://github.com/copperfeesh" title="GitHub">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                </a>
                <a href="https://www.linkedin.com/in/garronstevenson/" title="LinkedIn">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                </a>
                <a href="https://bsky.app/profile/copperfish.net" title="BlueSky">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 16s-2-2.5-2-4c0-1.5 1-2.5 2-2.5s2 1 2 2.5c0 1.5-2 4-2 4z"></path></svg>
                </a>
            </div>
        </aside>
        <main class="content">
            <article class="post-content">
                <a href="../index.html" class="back-link">← Back to Blog</a>
                <header class="post-header">
                    <time class="post-date">June 8, 2026</time>
                    <h1 class="post-title">The Beauty of Monochrome</h1>
                </header>
                <div class="post-body">
                    <p>Exploring why restricted color palettes often lead to more focused and professional-looking designs in the modern web...</p>
                    <p>Monochrome doesn't mean boring. It means clarity. By removing the distraction of color, we force the layout and typography to do the heavy lifting.</p>
                </div>
            </article>
        </main>
    </div>
</body>
</html>
```

- [ ] **Step 3: Create blog/static-performance.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Static Site Performance | Garron Stevenson</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <div class="layout">
        <aside class="sidebar">
            <h1 class="branding"><a href="../index.html">Garron Stevenson</a></h1>
            <nav class="nav">
                <a href="../index.html" class="nav-link active">Blog</a>
                <a href="../contact.html" class="nav-link">Contact</a>
            </nav>
            <div class="social-links">
                <a href="https://github.com/copperfeesh" title="GitHub">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                </a>
                <a href="https://www.linkedin.com/in/garronstevenson/" title="LinkedIn">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                </a>
                <a href="https://bsky.app/profile/copperfish.net" title="BlueSky">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 16s-2-2.5-2-4c0-1.5 1-2.5 2-2.5s2 1 2 2.5c0 1.5-2 4-2 4z"></path></svg>
                </a>
            </div>
        </aside>
        <main class="content">
            <article class="post-content">
                <a href="../index.html" class="back-link">← Back to Blog</a>
                <header class="post-header">
                    <time class="post-date">June 1, 2026</time>
                    <h1 class="post-title">Static Site Performance</h1>
                </header>
                <div class="post-body">
                    <p>Why I decided to stick with pure HTML and CSS for my personal site instead of using a heavy framework...</p>
                    <p>Performance is a feature. Static sites are fast, secure, and easy to host.</p>
                </div>
            </article>
        </main>
    </div>
</body>
</html>
```

- [ ] **Step 4: Commit**

```bash
git add blog/*.html css/style.css
git commit -m "feat: implement blog post pages"
```
