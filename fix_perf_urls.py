filepath = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/podcaster-resources/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Just replace "episodes/" with "episode/" for the captivate URLs
content = content.replace('https://performance.captivate.fm/episodes/', 'https://performance.captivate.fm/episode/')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed performance captivate URLs.")
