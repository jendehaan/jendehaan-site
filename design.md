# Design System Documentation

## Overview
This document outlines the design system for **Jen deHaan — Neurodivergent Educator + CRM Practitioner**. The site uses a modern, dark-themed, glassmorphic aesthetic with vibrant gradient accents. It focuses heavily on accessibility, responsiveness, and performance, adopting a static HTML/CSS approach without relying on heavy frameworks.

## 1. Typography

- **Headings & Display Font:** `Space Grotesk` (Weights: 500, 700). Used for all headers (`h1`, `h2`, `h3`), navigation text, buttons, and prominent numbers/labels.
- **Body Font:** Native System Sans-serif stack (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif`). This ensures maximum legibility and zero-load performance for primary reading experiences.
- **Text Hierarchy:**
  - Base Font Size: `18px`, Line-height: `1.65`
  - Body Text: `#ccc`
  - Secondary Text (`.text-secondary`): `#999`
  - Tertiary Text (`.text-tertiary`): `#888`
  - Section Labels (`.section-label`): Uppercase, 11px, `2px` letter spacing, `#666`.

## 2. Color Palette & Gradients

The site uses a dark base (almost black) contrasted with energetic, neurodivergent-friendly neon/rainbow gradients.

### Base Colors
- **Main Background:** `#0d2a30` (Dark Teal)
- **Card/Widget Background:** `#123a43`
- **Subtle Borders:** `#143640` or `rgba(255, 255, 255, 0.1)`

### Accent Colors
- **Primary Action (Coral):** `#E8593C`
- **Yellow:** `#F2A623`
- **Green:** `#4CAF50`
- **Blue:** `#3B8BD4`
- **Purple:** `#7B61FF`

### Global Gradients
Vibrant gradients are a visual staple of the site, applied via background rules, borders, and masked text (`-webkit-background-clip: text`).
- **Subtle Teal Gradient (`.grad-rainbow`):** Spans a subtle teal range from Medium Teal to Light Teal (`#40c4b5` to `#63e3d4`). Used for taglines, dates, and rule dividers.
- **Heading Gradient (`h2`, `.grad-b`):** 135-degree angle medium to light teal.
- **Compressed Gradient (`.grad-b-sm`):** Quick medium to light teal transition, primarily used for navigation names and blog titles.
- **Atmospheric Glow (`.hero-glow`):** Soft, semi-transparent backdrop washes behind hero elements.

## 3. UI Components

### Navigation (`.glass-nav`)
- **Visuals:** Fixed top pill-shaped bar (`border-radius: 40px`), relying on glassmorphism (`rgba(6, 20, 23, 0.6)` with a `16px` backdrop blur) to maintain visibility without entirely obscuring page content below it.
- **Search:** Pure CSS expanding search bar. It rests as a circular icon button and expands gracefully into a full `180px` input area on `:focus` or when text is present.
- **Mega Menu:** Implemented via CSS hover state for the Desktop "About" link offering deeper navigation without separate clicks.

### Buttons
All buttons use the `Space Grotesk` font and subtle pulse animations (`@keyframes btnPulse`) upon `:active` clicks.
- **Primary (`.btn-primary`):** Coral to darker red gradient (`#E8593C` out to `#D44A2E`). 
- **Secondary (`.btn-secondary`):** Transparent with a dark border. On hover, the border dynamically transitions to Coral.
- **Featured (`.btn-featured`):** Reserved for primary CTAs (like newsletter signups). Wrapped in the full spectrum rainbow gradient with a glowing box-shadow effect on hover.

### Cards & Layout Elements
- **Standard Card Data:** `#123a43` background with `0.5px solid #1e5e6b` borders. Soft border-color transitions on hover.
- **Show Cards:** Glass effects and elevated shadows (`box-shadow: 0 24px 48px rgba(0, 0, 0, 0.2)`) intended to spotlight primary products like podcast shows.

## 4. Blog & Article Infrastructure

The blog layout is optimized for high text density while exposing lateral browsing capabilities.

- **Post Grid Layout:** `1fr 340px` split with the primary article body resting on the left, and a contextual sticky sidebar resting on the right.
- **Typography:** Increased spacing for long-read comfort.
- **Categorical Tagging:** `.tag` labels feature unified pill structures. Specific category tags adopt designated accent colors (e.g., `.tag-coral`, `.tag-blue`, `.tag-purple`) providing visual categorization indexing at a glance.
- **Sidebar Widgets (`.sidebar-widget`):** Modular context blocks (e.g. Listen on Spotify, Promos) featuring top directional ambient glow overlays (`.widget-listen`, `.widget-promo`).

## 5. Accessibility (A11y) & SEO Integration

- **"Skip to content" link:** Present at the top of the body flow, visible off-screen until focused, to immediately bypass navigation for keyboard users navigation.
- **Focus States:** Every anchor uses custom `outline: 2px solid #E8593C` to make keyboard and screen-flow navigation distinctly apparent.
- **Reduced Motion:** Built-in `@media (prefers-reduced-motion: reduce)` queries which neutralize all animation and transition lengths (`0.01ms`) and disables smooth scrolling.
- **Semantic Structure:** Utilization of proper `header`, `nav`, `main`, `section`, and `footer` landmarks. Single `h1` header policy enforced per page.
- **Schema.org JSON-LD:** Enforced Person/Site context on all root heads.
