import os

base_dir = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site'

osano_snippet = """
  <!-- Osano Cookie Consent -->
  <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.css" />
  <script src="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.js" data-cfasync="false"></script>
  <script>
  window.addEventListener("load", function(){
  window.cookieconsent.initialise({
    "palette": {
      "popup": {
        "background": "#0d2a30",
        "text": "#aebbc1"
      },
      "button": {
        "background": "#E8593C",
        "text": "#ffffff"
      }
    },
    "theme": "classic",
    "position": "bottom-right",
    "content": {
      "href": "https://jendehaan.com/privacy-policy/"
    }
  })});
  </script>
"""

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'cookieconsent.min.js' not in content:
                new_content = content.replace('</body>', osano_snippet + '</body>')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f"Added Osano snippet to {count} files.")
