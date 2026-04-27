import re

with open('404.html', 'r') as f:
    html = f.read()

# Fix style.css
html = html.replace('href="style.css?v=4"', 'href="/style.css?v=4"')

# Fix navigation
html = html.replace('href="./index.html"', 'href="/"')
html = html.replace('href="about/index.html"', 'href="/about/"')
html = html.replace('href="blog/index.html"', 'href="/blog/"')
html = html.replace('href="wired-divergent/index.html"', 'href="/wired-divergent/"')
html = html.replace('href="youtube/index.html"', 'href="/youtube/"')
html = html.replace('href="podcaster-resources/index.html"', 'href="/podcaster-resources/"')
html = html.replace('href="products/index.html"', 'href="/products/"')
html = html.replace('href="newsletters/index.html"', 'href="/newsletters/"')
html = html.replace('href="contact/index.html"', 'href="/contact/"')

# Fix footer
html = html.replace('href="./privacy-policy/index.html"', 'href="/privacy-policy/"')
html = html.replace('href="./contact/index.html"', 'href="/contact/"')
html = html.replace('href="./feed.xml"', 'href="/feed.xml"')

with open('404.html', 'w') as f:
    f.write(html)
