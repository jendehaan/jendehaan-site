import os
import glob
import re

SITE_DIR = "/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site"

def fix_css_links():
    html_files = []
    for root, dirs, files in os.walk(SITE_DIR):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                html_files.append(path)

    for path in html_files:
        with open(path, 'r') as f:
            content = f.read()
        
        # Remove cache buster query params for local file viewing
        content = re.sub(r'href="\.\./style\.css\?v=\d+"', 'href="../style.css"', content)
        content = re.sub(r'href="style\.css\?v=\d+"', 'href="style.css"', content)

        with open(path, 'w') as f:
            f.write(content)

fix_css_links()
print("Fixed CSS links")
