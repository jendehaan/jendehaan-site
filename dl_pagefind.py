import urllib.request
import os
import tarfile

url = 'https://github.com/CloudCannon/pagefind/releases/download/v1.1.0/pagefind-v1.1.0-aarch64-apple-darwin.tar.gz'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response, open('/tmp/pagefind.tar.gz', 'wb') as out_file:
        out_file.write(response.read())
    print("Downloaded!")
    
    with tarfile.open('/tmp/pagefind.tar.gz', 'r:gz') as tar:
        tar.extractall('/tmp/pagefind_bin')
    print("Extracted!")
except Exception as e:
    print(e)
