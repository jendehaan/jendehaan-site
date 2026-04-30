import os
import glob

# The kit form block for the "Stay in the loop" sections
form_html = """          <div class="kit-form">
            <form action="https://app.kit.com/forms/9075050/subscriptions" method="post" data-uid="be7510d98c"
              id="newsletter-form">
              <input type="email" name="email_address" placeholder="Your email address" required>
              <button type="submit" class="btn-featured">Subscribe</button>
            </form>
            <div id="newsletter-success" class="kit-success" style="display: none;">
              Thanks for subscribing! Please check your inbox to confirm.
            </div>
            <p class="kit-powered">We won't send you spam. Unsubscribe at any time.</p>
          </div>"""

# The javascript snippet
js_snippet = """
    // Ajax Newsletter Form
    const nForm = document.getElementById('newsletter-form');
    const nSuccess = document.getElementById('newsletter-success');
    if (nForm) {
      nForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const btn = nForm.querySelector('button[type="submit"]');
        const ogText = btn.textContent;
        btn.textContent = 'Wait...';
        btn.disabled = true;

        fetch(nForm.action, {
          method: 'POST',
          body: new FormData(nForm),
          mode: 'no-cors'
        })
          .then(() => {
            nForm.style.display = 'none';
            nSuccess.style.display = 'block';
          })
          .catch(err => {
            console.warn('Background submission blocked (likely by privacy settings). Falling back to native submit.', err);
            nForm.submit();
          });
      });
    }
"""

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    changed = False

    # 1. Replace the "Subscribe" button with the embedded form in Stay in the Loop
    # We look for <a href="../newsletters/index.html" class="btn-featured">Subscribe</a>
    # or similar
    if '<h3>Stay in the loop</h3>' in content:
        # For relative paths that might be ../ or ./ or /
        import re
        old_button = re.search(r'<a href="[^"]*newsletters/[^"]*" class="btn-featured"[^>]*>Subscribe</a>', content)
        if old_button:
            content = content.replace(old_button.group(0), form_html)
            changed = True
        
        # Another variant for the blog post template
        old_button2 = re.search(r'<a href="[^"]*newsletters/[^"]*" class="btn-featured"[^>]*>Subscribe to newsletter</a>', content)
        if old_button2:
            content = content.replace(old_button2.group(0), form_html)
            changed = True

    # 2. Update the newsletters/index.html page itself to have the ID and success div
    if 'newsletters/index.html' in filepath and 'id="newsletter-form"' not in content:
        content = content.replace(
            '<form action="https://app.kit.com/forms/9075050/subscriptions" method="post" data-uid="be7510d98c">',
            '<form action="https://app.kit.com/forms/9075050/subscriptions" method="post" data-uid="be7510d98c" id="newsletter-form">'
        )
        content = content.replace(
            '</form>',
            '</form>\n          <div id="newsletter-success" class="kit-success" style="display: none; padding-top: 16px; color: #fff; font-weight: bold; text-align: center;">Thanks for subscribing! Please check your inbox to confirm.</div>'
        )
        changed = True

    # 3. Inject JS if it doesn't exist
    # Only if we added a form or updated the newsletter page
    if changed and '// Ajax Newsletter Form' not in content:
        # Insert before <!-- Osano Cookie Consent --> or </body>
        if '<!-- Osano Cookie Consent -->' in content:
            content = content.replace(
                '<!-- Osano Cookie Consent -->',
                f'<script>{js_snippet}</script>\n\n  <!-- Osano Cookie Consent -->'
            )
        else:
            content = content.replace('</body>', f'<script>{js_snippet}</script>\n</body>')

    if changed:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")

# Find all HTML files
for root, _, files in os.walk('/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
