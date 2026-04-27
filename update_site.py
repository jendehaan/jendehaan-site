import os
import re

SITE_DIR = "/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site"

def update_css():
    css_path = os.path.join(SITE_DIR, 'style.css')
    with open(css_path, 'r') as f:
        content = f.read()
    
    # 1. Update font-size
    content = re.sub(r'font-size:\s*16px;', 'font-size: 18px;', content)
    
    # 2. Update media queries
    content = content.replace('(max-width: 900px)', '(max-width: 1024px)')
    
    # 3. Add desktop-only/mobile-only and align-items: center
    if '.desktop-only' not in content:
        # We will append the utility classes
        content += """

/* --- Responsive Menu Utility Classes --- */
.desktop-only { display: block; }
.mobile-only { display: none; }

@media (max-width: 1024px) {
  .desktop-only { display: none !important; }
  .mobile-only { display: block !important; }
  
  .nav-links.open {
    align-items: center;
    text-align: center;
  }
}
"""
    with open(css_path, 'w') as f:
        f.write(content)
    print("Updated CSS.")

def build_nav(depth):
    # depth = 0 for index.html, depth=1 for subdirectories
    prefix = '../' if depth > 0 else './'
    index_prefix = '../' if depth > 0 else './'
    
    nav_html = f"""  <!-- Navigation -->
  <nav class="glass-nav" aria-label="Main navigation">
    <div class="nav-container">
      <a href="{index_prefix}index.html" class="nav-name grad-b-sm">Jen deHaan</a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">&#9776;</button>
      <ul class="nav-links">
        <li><a href="{prefix}wired-divergent/index.html">Wired Divergent</a></li>
        <li><a href="{prefix}blog/index.html">Blog</a></li>
        <li><a href="{prefix}products/index.html">Products</a></li>

        <!-- Desktop Dropdown -->
        <li class="has-dropdown desktop-only">
          <a style="cursor: default;">About &nbsp;▾</a>
          <div class="mega-menu">
            <div class="mega-menu-content">
              <a href="{prefix}about/index.html" class="mega-menu-link">
                <strong>About Jen</strong>
                <span class="mega-desc">Background, approach, and credentials.</span>
              </a>
              <a href="{prefix}contact/index.html" class="mega-menu-link">
                <strong>Contact</strong>
                <span class="mega-desc">Get in touch.</span>
              </a>
            </div>
          </div>
        </li>

        <!-- Mobile Flat Links -->
        <li class="mobile-only"><a href="{prefix}about/index.html">About Jen</a></li>
        <li class="mobile-only"><a href="{prefix}contact/index.html">Contact</a></li>

        <li><a href="{prefix}newsletters/index.html" class="btn-nav-newsletter">Newsletter</a></li>
      </ul>
    </div>
  </nav>"""
    return nav_html

def build_footer(depth):
    prefix = '../' if depth > 0 else './'
    footer_html = f"""  <!-- Footer -->
  <footer class="site-footer">
    <div class="container footer-container">
      <div class="footer-left">
        &copy; 2026 Jen deHaan<br>
        <span class="footer-subtext">All rights reserved · Made and hosted in Canada.</span>
      </div>
      <div class="footer-right">
        <ul class="footer-links">
          <li><a href="{prefix}privacy-policy/index.html">Privacy</a></li>
          <li><a href="{prefix}contact/index.html">Contact</a></li>
          <li><a href="{prefix}feed.xml">RSS</a></li>
        </ul>
      </div>
    </div>
  </footer>"""
    return footer_html

def update_html_files():
    for root, dirs, files in os.walk(SITE_DIR):
        for file in files:
            if file == 'index.html':
                filepath = os.path.join(root, file)
                depth = relpath_depth(filepath)
                
                with open(filepath, 'r') as f:
                    content = f.read()

                # If skipping podcaster-resources or youtube which we'll rewrite entirely next
                if 'youtube/index.html' in filepath or 'podcaster-resources/index.html' in filepath:
                    continue
                    
                # Replace nav
                nav_pattern = re.compile(r'<!--\s*(Nav|Navigation)\s*-->.*?<main id="main">', re.DOTALL | re.IGNORECASE)
                replacement = build_nav(depth) + '\n\n  <!-- Main -->\n  <main id="main">'
                content = nav_pattern.sub(replacement, content)
                
                # Replace footer
                footer_pattern = re.compile(r'<!--\s*Footer\s*-->.*?</footer>', re.DOTALL | re.IGNORECASE)
                content = footer_pattern.sub(build_footer(depth), content)
                
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"Updated {filepath}")

def relpath_depth(filepath):
    rel = os.path.relpath(filepath, SITE_DIR)
    if rel == 'index.html':
        return 0
    return 1

update_css()
update_html_files()
