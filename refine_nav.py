import os
import glob
import re

SITE_DIR = "/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site"

def build_nav(depth):
    prefix = ('../' * depth) if depth > 0 else './'
    index_prefix = ('../' * depth) if depth > 0 else './'
    return f"""  <nav class="glass-nav" aria-label="Main navigation">
    <div class="nav-grid">
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
        <li class="mobile-only mt-2"><a href="{prefix}search/index.html">Search</a></li>
        <li class="mobile-only mt-2"><a href="{prefix}newsletters/index.html" class="btn-featured btn-nav-newsletter">Newsletter</a></li>
      </ul>
      
      <div class="nav-actions desktop-only">
        <form action="{prefix}search/index.html" class="nav-search-form" method="get">
          <input type="search" name="q" class="nav-search-input" placeholder="Search..." aria-label="Search">
          <svg class="nav-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </form>
        <a href="{prefix}newsletters/index.html" class="btn-featured btn-nav-newsletter">Newsletter</a>
      </div>
    </div>
  </nav>"""

def fix_all_html_files():
    html_files = []
    for root, dirs, files in os.walk(SITE_DIR):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                depth = path.replace(SITE_DIR, "").count("/") - 1
                if depth < 0: depth = 0
                html_files.append((path, depth))

    for path, depth in html_files:
        with open(path, 'r') as f:
            content = f.read()
        
        content = re.sub(r'<nav class="glass-nav".*?</nav>', build_nav(depth), content, flags=re.DOTALL)
        
        # Add cache buster with correct dynamic depth
        prefix_str = ('../' * depth) if depth > 0 else './'
        if depth == 0: prefix_str = ''
        
        # Strip out old style declarations to replace with a standard one
        content = re.sub(r'<link rel="stylesheet" href="(\.\./)*style\.css(\?v=\d+)?">', f'<link rel="stylesheet" href="{prefix_str}style.css?v=4">', content)
        content = re.sub(r'<link rel="stylesheet" href="style\.css(\?v=\d+)?">', f'<link rel="stylesheet" href="{prefix_str}style.css?v=4">', content)
        
        with open(path, 'w') as f:
            f.write(content)

fix_all_html_files()
print("Fixed nav structure and added CSS cache busters.")
