import os
import re

base_dir = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site'
categories = ['nervous-system-regulation', 'adhd', 'sensory-processing']

new_list = '''        <div class="blog-list">
          <div class="card" style="margin-bottom: 24px;">
            <h2 style="margin-top: 0; margin-bottom: 8px;"><a href="../../functional-freeze-vs-adhd-paralysis/index.html" style="color: inherit; text-decoration: none;">Functional Freeze vs ADHD Paralysis: What Your Nervous System Is Actually Doing</a></h2>
            <div style="font-size: 13px; color: #999; margin-bottom: 8px;">April 24, 2026</div>
            <div class="tag-list" style="margin-bottom: 16px;">
              <a href="../nervous-system-regulation/index.html" class="tag tag-nervous" style="font-size: 11px; padding: 4px 10px; text-decoration: none;">Nervous System Regulation</a>
              <a href="../adhd/index.html" class="tag tag-adhd" style="font-size: 11px; padding: 4px 10px; text-decoration: none;">ADHD</a>
              <a href="../sensory-processing/index.html" class="tag tag-sensory" style="font-size: 11px; padding: 4px 10px; text-decoration: none;">Sensory Processing</a>
            </div>
            <p class="excerpt" style="margin-bottom: 0;">Functional freeze and ADHD paralysis look the same from the outside. From the inside, they involve different biology and need different responses. Here's how to tell which one you're in.</p>
          </div>
        </div>'''

for cat in categories:
    path = os.path.join(base_dir, 'blog', 'categories', cat, 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(r'<div class="blog-list">.*?(</section>)', new_list + r'\n      </div>\n    \1', html, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Categories fixed")
