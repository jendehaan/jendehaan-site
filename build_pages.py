import os

SITE_DIR = "/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site"

def build_nav(depth):
    prefix = '../' if depth > 0 else './'
    index_prefix = '../' if depth > 0 else './'
    return f"""  <nav class="glass-nav" aria-label="Main navigation">
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

def build_footer(depth):
    prefix = '../' if depth > 0 else './'
    return f"""  <footer class="site-footer" style="margin-top: 40px;">
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

  <main id="main" style="padding-top: 120px;">
    <section class="section">
      <div class="container">
        <h1 class="display grad-b">YouTube</h1>
        <p style="font-size: 1.2rem; color: #ccc; max-width: 800px; margin-bottom: 2rem;">Channels and playlists covering neurodivergence, improv, and podcasting performance.</p>
        
        <div class="channel-links">
          <a href="https://youtube.com/@jdehaan" class="channel-link">@jdehaan</a>
          <a href="https://youtube.com/@YourSoloPodcast" class="channel-link">@YourSoloPodcast</a>
          <a href="https://youtube.com/@yourimprovbrain" class="channel-link">@yourimprovbrain</a>
        </div>

        <h2 class="grad-b-sm">Featured Playlists</h2>
        <div class="yt-playlist-grid">
          
          <div class="yt-playlist-card">
            <div class="yt-video-wrap">
              <iframe src="https://www.youtube.com/embed/videoseries?list=PL62Xz05v1loi-GJadY0qN8jBxJPrR0erg" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
          </div>

          <div class="yt-playlist-card">
            <div class="yt-video-wrap">
              <iframe src="https://www.youtube.com/embed/videoseries?list=PL62Xz05v1loh-XKTdnnEKD1Y-3OfagADp" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
          </div>

          <div class="yt-playlist-card">
            <div class="yt-video-wrap">
              <iframe src="https://www.youtube.com/embed/videoseries?list=PLgWFYbO_riyhUdCPiSRe0fHo3doqmy_b0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
          </div>

        </div>
      </div>
    </section>
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
  </script>
</body>
</html>
"""
    with open(os.path.join(SITE_DIR, 'youtube/index.html'), 'w') as f:
        f.write(html)
        
def write_podcaster_page():
    with open(os.path.join(SITE_DIR, 'podcaster-resources/pr_code.html'), 'r') as f:
        pr_content = f.read()

    html = f"""<!DOCTYPE html>
<html lang="en-CA">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Podcaster Performance Resources — Jen deHaan</title>
  <meta name="description" content="Resources about podcasting as a performance and communication discipline.">
  <link rel="stylesheet" href="../style.css">
  {pr_content}
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
  </script>
</body>
</html>
"""
    with open(os.path.join(SITE_DIR, 'podcaster-resources/index.html'), 'w') as f:
        f.write(html)

write_youtube_page()
write_podcaster_page()
print("Youtube and Podcaster updated")
