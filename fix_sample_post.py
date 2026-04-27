import os
import re

SITE_DIR = "/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site"

# 1. fix canonical link
ff_path = os.path.join(SITE_DIR, 'blog', 'functional-freeze-vs-adhd-paralysis', 'index.html')
with open(ff_path, 'r') as f: content = f.read()
content = content.replace('href="https://jendehaan.com/blog/sample-post/"', 'href="https://jendehaan.com/blog/functional-freeze-vs-adhd-paralysis/"')
with open(ff_path, 'w') as f: f.write(content)

# 2. fix sitemap and feed
for xml_file in ['sitemap.xml', 'feed.xml']:
    xml_path = os.path.join(SITE_DIR, xml_file)
    with open(xml_path, 'r') as f: content = f.read()
    content = content.replace('sample-post', 'functional-freeze-vs-adhd-paralysis')
    with open(xml_path, 'w') as f: f.write(content)

# 3. scrub empty categories
cats = ['wired-divergent', 'neurodivergence', 'workplace', 'autistic-experience', 'somatic-practices', 'science-evidence', 'lived-experience']
empty_list = '''        <div class="blog-list">
          <p>New posts coming soon...</p>
        </div>'''

for cat in cats:
    path = os.path.join(SITE_DIR, 'blog', 'categories', cat, 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(r'<div class="blog-list">.*?(</section>)', empty_list + r'\n      </div>\n    \1', html, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
print("Scrubbed")
