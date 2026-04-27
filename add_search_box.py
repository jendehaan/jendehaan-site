import os
import re

base_dir = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/blog/categories'

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Determine relative path to search
            rel_path = os.path.relpath(
                '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/search/index.html',
                root
            )
            
            search_block = f"""
    <!-- Search Callout -->
    <section class="section" style="padding-top: 0; padding-bottom: 60px;">
      <div class="container" style="max-width: 800px; text-align: center;">
        <div style="padding: 40px; border-radius: 16px; background: #123a43; border: 1px solid #1e5e6b; box-shadow: 0 8px 24px rgba(0,0,0,0.15);">
          <h3 style="margin-top: 0; color: #fff; font-family: 'Space Grotesk', sans-serif;">Didn't find what you're looking for?</h3>
          <p style="color: #aebbc1; margin-bottom: 24px; font-size: 1.1rem;">Search across all articles, podcasts, and resources.</p>
          <form action="{rel_path}" method="get" style="display: flex; gap: 12px; max-width: 400px; margin: 0 auto;">
            <input type="search" name="q" placeholder="Search..." style="flex: 1; padding: 14px 20px; border-radius: 8px; border: 1px solid #1e5e6b; background: #07181b; color: #fff; font-family: 'DM Sans', sans-serif; font-size: 16px;" aria-label="Search">
            <button type="submit" class="btn-featured" style="padding: 14px 28px; border: none; cursor: pointer;">Search</button>
          </form>
        </div>
      </div>
    </section>
"""
            
            # Remove existing search block if it was added before (for idempotency)
            content = re.sub(r'<!-- Search Callout -->.*?</section>', '', content, flags=re.DOTALL)
            
            # Insert just before </main>
            if '</main>' in content:
                content = content.replace('</main>', search_block + '</main>')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Added search block to {filepath}")

