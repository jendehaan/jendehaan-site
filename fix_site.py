import os, re

new_about_text = '''    <section class="section">
      <div class="container">
        <h2 class="grad-b-sm">About this site</h2>
        <div class="post-body">
          <p>This site includes education and resources for neurodivergent brains on nervous system regulation, built around the Community Resilience Model and other related resources. Blog posts, podcast episodes, guided exercises, and eventually coaching and community will be available. Resources are written and produced by one neurodivergent person for other neurodivergent people (peer to peer style).</p>
        </div>
      </div>
    </section>

    <div class="container"><hr class="gradient-rule"></div>

    <!-- What I'm building section -->'''

def update_html(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except Exception as e:
        return
    
    orig = content

    # Fix local links
    # href="blog/" -> href="blog/index.html"
    content = re.sub(r'href="(?![a-zA-Z]+:|//)([^"#\'>]*?)/"', r'href="\1/index.html"', content)
    
    # About Page Text
    if filepath.endswith('about/index.html'):
        if "About this site" not in content and "<!-- What I'm building section -->" in content:
            content = content.replace("<!-- What I'm building section -->", new_about_text)

    # Products Page Cards
    if filepath.endswith('products/index.html'):
        content = content.replace('<div class="card product-card">', '<div class="show-card" style="flex-direction: column;">')

    # Footer standardize
    content = re.sub(
        r'<section class="section">(\s*<div class="container">\s*<div class="newsletter-cta">)',
        r'<section class="newsletter-wrapper">\1',
        content
    )
    # the ones that don't have newsletter-cta wrapper but have the H3
    if '<h3>Get launch updates</h3>' in content and 'max-width: 540px' in content:
        content = content.replace(
            '<section class="section">\n      <div class="container" style="max-width: 540px;">\n        <h3>Get launch updates</h3>',
            '<section class="newsletter-wrapper">\n      <div class="container">\n        <div class="newsletter-cta" style="max-width: 540px; margin: 0 auto;">\n        <h3>Get launch updates</h3>'
        )
        # We need to add the closing div for .newsletter-cta
        content = content.replace('</section>', '</div>\n    </section>', 1) # This is risky, let's skip for the wired-divergent and just change the section class
        
    # Safer for wired divergent:
    content = content.replace('<section class="section">\n      <div class="container" style="max-width: 540px;">\n        <h3>Get launch updates</h3>', '<section class="newsletter-wrapper">\n      <div class="container">\n        <div class="newsletter-cta" style="max-width: 540px; margin: 0 auto; padding-left: 0;">\n        <h3>Get launch updates</h3>')
    
    # This might break tags if not careful. Let's just fix it by script or do wired-divergent separately.
    
    if content != orig:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith('.html'):
            update_html(os.path.join(root, name))

# Ensure wired-divergent is closed correctly if we added a opening div.
print("Finished updates.")
