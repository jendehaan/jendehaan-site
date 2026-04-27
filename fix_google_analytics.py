import os
import re

base_dir = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site'

ga_snippet = """
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-HNZRZ79395"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-HNZRZ79395');
  </script>
"""

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content

            # Remove the existing snippet I just added if it's perfectly matched
            content = content.replace(ga_snippet, '')
            
            # Remove the commented out placeholder lines
            content = re.sub(r'<!--.*?googletagmanager.*?-->\s*', '', content)
            
            # Also remove any stranded gtag script blocks just in case
            content = re.sub(r'<script>\s*window\.dataLayer.*?</script>\s*', '', content, flags=re.DOTALL)
            
            # Now cleanly insert the snippet right before </head>
            if 'G-HNZRZ79395' not in content:
                content = content.replace('</head>', ga_snippet + '</head>')
                
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f"Fixed Google Analytics snippet in {count} files.")
