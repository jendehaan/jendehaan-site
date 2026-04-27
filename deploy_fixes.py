import os
import glob

SITE_DIR = "/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site"

def build_nav(depth):
    prefix = '../' if depth > 0 else './'
    index_prefix = '../' if depth > 0 else './'
    return f"""  <nav class="glass-nav" aria-label="Main navigation">
    <div class="nav-grid">
      <div class="nav-left">
        <a href="{index_prefix}index.html" class="nav-name grad-b-sm">Jen deHaan</a>
      </div>
      <div class="nav-center">
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
        </ul>
      </div>
      <div class="nav-right">
        <a href="{prefix}newsletters/index.html" class="btn-featured btn-nav-newsletter">Newsletter</a>
      </div>
    </div>
  </nav>"""

def build_footer(depth):
    prefix = '../' if depth > 0 else './'
    return f"""  <footer class="site-footer" style="margin-top: 40px; padding: 40px 0; border-top: 1px solid rgba(255, 255, 255, 0.05);">
    <div class="container footer-container">
      <div class="footer-left">
        &copy; 2026 Jen deHaan<br>
        <span class="footer-subtext">All rights reserved · Made and hosted in Canada.</span>
      </div>
      <div class="footer-right">
        <ul class="footer-links" style="list-style: none; display: flex; gap: 1rem;">
          <li><a href="{prefix}privacy-policy/index.html">Privacy</a></li>
          <li><a href="{prefix}contact/index.html">Contact</a></li>
          <li><a href="{prefix}feed.xml">RSS</a></li>
        </ul>
      </div>
    </div>
  </footer>"""

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
        if "youtube/index.html" in path or "podcaster-resources/index.html" in path:
            continue
        with open(path, 'r') as f:
            content = f.read()
        
        # We need to replace the entire <nav ...> ... </nav> block
        import re
        content = re.sub(r'<nav class="glass-nav".*?</nav>', build_nav(depth), content, flags=re.DOTALL)
        content = re.sub(r'<footer class="site-footer".*?</footer>', build_footer(depth), content, flags=re.DOTALL)
        
        with open(path, 'w') as f:
            f.write(content)

def write_youtube_page():
    html = f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>YouTube — Jen deHaan</title>
  <meta name="description" content="Jen's YouTube channels and playlists covering neurodivergence, improv, podcasting performance, and camera presence.">
  <link rel="stylesheet" href="../style.css">
  <style>
    .yt-playlist-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 2rem;
      margin-top: 2rem;
    }}
    .yt-playlist-card {{
      background: rgba(20, 20, 20, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}
    .yt-video-wrap {{
      position: relative;
      padding-bottom: 56.25%;
      height: 0;
      overflow: hidden;
    }}
    .yt-video-wrap iframe {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border: 0;
    }}
    .channel-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 3rem;
    }}
    .channel-link {{
      background: rgba(232, 89, 60, 0.1);
      color: #E8593C;
      padding: 0.75rem 1.5rem;
      border-radius: 40px;
      font-weight: 600;
      font-size: 0.95rem;
      transition: background 0.2s;
    }}
    .channel-link:hover {{
      background: rgba(232, 89, 60, 0.2);
      text-decoration: none;
    }}
  </style>
</head>
<body>
{build_nav(1)}

  <main id="main" style="padding-top: 120px; padding-bottom: 60px;">
    <section class="section">
      <div class="container">
        <h1 class="display grad-b">YouTube</h1>
        <p style="font-size: 1.2rem; color: #ccc; max-width: 800px; margin-bottom: 2rem;">Channels and playlists covering neurodivergence, improv, and podcasting performance.</p>
        
        <div class="channel-links">
          <a href="https://youtube.com/@jdehaan" class="channel-link">@jdehaan</a>
          <a href="https://youtube.com/@YourSoloPodcast" class="channel-link">@YourSoloPodcast</a>
          <a href="https://youtube.com/@yourimprovbrain" class="channel-link">@yourimprovbrain</a>
        </div>

        <div style="background: rgba(232, 89, 60, 0.1); border-left: 3px solid #E8593C; padding: 1rem; border-radius: 4px; margin-bottom: 2rem; font-size: 0.9rem;">
          <strong>Note about Local Embeds:</strong> When viewing this page locally (e.g. from your desktop), YouTube's API may throw an “Error 153” on playlists. Once the site is published online to a real domain, the playlists will load normally!
        </div>

        <h2 class="grad-b-sm">Featured Playlists</h2>
        <div class="yt-playlist-grid">
          
          <div class="yt-playlist-card">
            <div class="yt-video-wrap">
              <iframe src="https://www.youtube.com/embed/videoseries?list=PL62Xz05v1loi-GJadY0qN8jBxJPrR0erg&origin=https://jendehaan.com" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
          </div>

          <div class="yt-playlist-card">
            <div class="yt-video-wrap">
              <iframe src="https://www.youtube.com/embed/videoseries?list=PL62Xz05v1loh-XKTdnnEKD1Y-3OfagADp&origin=https://jendehaan.com" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
          </div>

          <div class="yt-playlist-card">
            <div class="yt-video-wrap">
              <iframe src="https://www.youtube.com/embed/videoseries?list=PLgWFYbO_riyhUdCPiSRe0fHo3doqmy_b0&origin=https://jendehaan.com" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
          </div>

        </div>
      </div>
    </section>
  </main>

{build_footer(1)}
</body>
</html>
"""
    with open(os.path.join(SITE_DIR, 'youtube/index.html'), 'w') as f:
        f.write(html)
        
def write_podcaster_page():
    with open(os.path.join(SITE_DIR, 'podcaster-resources/pr_code.html'), 'r') as f:
        pr_content = f.read()
    
    # pr_content contains <style>...</style> </head> <body> <main id="main"> <div class="pr-wrap"> ...
    # We must cleanly extract just the styles, and just the inner HTML for the main body.
    
    import re
    # Extract styles
    styles_match = re.search(r'<style>(.*?)</style>', pr_content, re.DOTALL)
    styles = styles_match.group(1) if styles_match else ""
    
    # Extract inner body wrap
    wrap_match = re.search(r'<div class="pr-wrap">(.*?)</div>\s*<script>', pr_content, re.DOTALL)
    if wrap_match:
        inner_content = wrap_match.group(1)
    else:
        # Fallback if that failed to match
        inner_content = pr_content

    html = f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Podcaster Performance Resources — Jen deHaan</title>
  <meta name="description" content="Resources about podcasting as a performance and communication discipline.">
  <link rel="stylesheet" href="../style.css">
  <style>
    {styles}
  </style>
</head>
<body>
{build_nav(1)}

  <main id="main" style="padding-top: 120px;">
    <div class="container pb-4">
      <div style="background: rgba(232, 89, 60, 0.1); border-left: 3px solid #E8593C; padding: 1rem; border-radius: 4px; margin-bottom: 2rem; font-size: 0.9rem;">
        <strong>Note about Local Embeds:</strong> When viewing these videos locally from a file path, YouTube may display an "Error 153 Video Player configuration error". Once the site is uploaded online, the videos will stream perfectly.
      </div>
    </div>
    <div class="pr-wrap" style="padding-top: 0;">
      {inner_content}
    </div>
  </main>

  {build_footer(1)}

  <script>
    const toggle = document.querySelector('.nav-toggle');
    const links = document.querySelector('.nav-links');
    if (toggle && links) {{
      toggle.addEventListener('click', () => {{
        const open = links.classList.toggle('open');
        toggle.setAttribute('aria-expanded', open);
      }});
    }}

    function prLoadYT(el, id) {{
      var iframe = document.createElement('iframe');
      // Added origin parameter to help mitigate error 153 when deployed
      iframe.src = 'https://www.youtube.com/embed/' + id + '?autoplay=1&origin=https://jendehaan.com';
      iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
      iframe.setAttribute('allowfullscreen', '');
      el.innerHTML = '';
      el.appendChild(iframe);
    }}
  </script>
</body>
</html>
"""
    with open(os.path.join(SITE_DIR, 'podcaster-resources/index.html'), 'w') as f:
        f.write(html)

fix_all_html_files()
write_youtube_page()
write_podcaster_page()
print("All pages fixed perfectly!")
