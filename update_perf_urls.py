filepath = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/podcaster-resources/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('https://stereoforest.com/episodes/', 'https://performance.captivate.fm/episodes/')
content = content.replace('https://stereoforest.com/podcast-performance-lab/', 'https://performance.captivate.fm/podcast-performance-lab/')
content = content.replace('>stereoforest.com/podcast-performance-lab<', '>performance.captivate.fm/podcast-performance-lab<')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Perf URLs updated successfully.")
