# Design Doc: Garron Stevenson's Personal Blog

## 1. Overview
A minimal, monochrome personal blog for Garron Stevenson, hosted on GitHub Pages. The design focuses on a refined "Soft Gray" aesthetic with an asymmetric layout and clear typography.

## 2. Visual Style & Palette
- **Style:** Modern Minimalism / Soft Gray.
- **Palette:** 
  - Background: `#fafafa` (Main) / `#ffffff` (Sidebar).
  - Primary Text: `#111111`.
  - Secondary Text: `#555555` / `#666666`.
  - Accents/Borders: `#eaeaea` / `#dddddd`.
- **Typography:** System sans-serif stack (Inter, -apple-system, etc.) for a clean, professional look.
- **Icons:** Minimalist outline style.

## 3. Structure & Layout
- **Pattern:** Asymmetric Split.
- **Desktop:** 
  - Fixed left sidebar (approx. 250px-300px) containing branding, navigation, and social links.
  - Scrolling right column for main content.
- **Mobile:** 
  - Collapses to a standard vertical stack with a top header/navigation.

## 4. Pages & Features
### 4.1 Home (Blog List)
- Displays blog posts as excerpts.
- Format: Date (upper case) -> Title -> Excerpt -> "Read More" link.

### 4.2 Contact Page
- Simple form with fields for Name, Email, and Message.
- Submission handled via **Formspree** (Static site compatible).
- Space for social media icons (GitHub, LinkedIn, BlueSky).

### 4.3 Blog Posts
- Dedicated pages for full post content, maintaining the same sidebar/content layout.

## 5. Technical Stack
- **Hosting:** GitHub Pages.
- **Frontend:** Pure HTML5 and Vanilla CSS.
- **Icons:** SVG icons (Lucide or similar minimalist outlines).
- **Form Handling:** Formspree.

## 6. Social Media Links
- **GitHub:** https://github.com/copperfeesh
- **LinkedIn:** https://www.linkedin.com/in/garronstevenson/
- **BlueSky:** https://bsky.app/profile/copperfish.net
