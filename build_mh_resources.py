import os
import re

template_path = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/about/index.html'
dest_dir = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/mental-health-resources'
dest_path = os.path.join(dest_dir, 'index.html')

os.makedirs(dest_dir, exist_ok=True)

with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace metadata
content = re.sub(r'<title>.*?</title>', '<title>Mental Health Resources — Jen deHaan</title>', content)
content = re.sub(r'<meta name="description"\s*content=".*?">', '<meta name="description" content="A directory of global mental health helplines, neurodivergent-specific therapy directories, and inclusive mental health resources.">', content, flags=re.DOTALL)
content = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Mental Health Resources — Jen deHaan">', content)
content = re.sub(r'<meta property="og:description"\s*content=".*?">', '<meta property="og:description" content="A directory of global mental health helplines, neurodivergent-specific therapy directories, and inclusive mental health resources.">', content, flags=re.DOTALL)
content = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://jendehaan.com/mental-health-resources/">', content)
content = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="Mental Health Resources — Jen deHaan">', content)
content = re.sub(r'<meta name="twitter:description"\s*content=".*?">', '<meta name="twitter:description" content="A directory of global mental health helplines, neurodivergent-specific therapy directories, and inclusive mental health resources.">', content, flags=re.DOTALL)

# Replace JSON-LD
json_ld = """<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Mental Health Resources",
    "url": "https://jendehaan.com/mental-health-resources/",
    "description": "A directory of global mental health helplines, neurodivergent-specific therapy directories, and inclusive mental health resources."
  }
  </script>"""
content = re.sub(r'<script type="application/ld\+json">.*?</script>', json_ld, content, flags=re.DOTALL)

# Replace hero
hero_new = """
    <section class="hero-narrow">
      <div class="hero-bg" style="background-image: url('../assets/images/Wired-Divergent-Background-Wide.jpg');"></div>
      <div class="container">
        <h1 class="display">Mental Health Resources</h1>
        <p class="hero-desc">Global crisis helplines and neurodivergent-affirming therapy directories.</p>
      </div>
    </section>
"""
content = re.sub(r'<section class="hero-narrow">.*?</section>', hero_new, content, flags=re.DOTALL)

# Generate main body
main_body = """
    <section class="section">
      <div class="container" style="max-width: 800px;">
        
        <h2 class="grad-b-sm" style="margin-bottom: 24px;">Immediate Mental Health Support & Helplines</h2>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://findahelpline.com/" target="_blank" rel="noopener">Find A Helpline</a></h3>
          <p style="margin-bottom: 0;">This platform acts as a global directory connecting people to free and confidential support in over 150 countries.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://www.befrienders.org/" target="_blank" rel="noopener">Befrienders Worldwide</a></h3>
          <p style="margin-bottom: 0;">This is an international network of emotional support centers providing confidential help for people experiencing distress.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://lifeline-international.com/" target="_blank" rel="noopener">Lifeline International</a></h3>
          <p style="margin-bottom: 0;">This worldwide network aims to improve access to emotional support and crisis helplines for people in distress.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://naseeha.org/" target="_blank" rel="noopener">Naseeha Mental Health</a></h3>
          <p style="margin-bottom: 0;">This is an international, 24/7 mental health helpline answering calls from around the world for anyone needing assistance.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://www.crisistextline.org/" target="_blank" rel="noopener">Crisis Text Line</a></h3>
          <p style="margin-bottom: 0;">This service provides free, 24/7, confidential, text-based mental health support and crisis intervention.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 48px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://988lifeline.org/" target="_blank" rel="noopener">988 Suicide & Crisis Lifeline</a></h3>
          <p style="margin-bottom: 0;">This number operates as the active 24/7 emotional support and crisis lifeline for residents in both the United States and Canada.</p>
        </div>

        <div class="top-rule" style="margin-bottom: 48px; position: static; height: 1px; background: rgba(255,255,255,0.1);"></div>

        <h2 class="grad-b-sm" style="margin-bottom: 24px;">Neurodivergent-Specific Therapy Directories</h2>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://neurodiversity.directory/" target="_blank" rel="noopener">The Neurodiversity Directory</a></h3>
          <p style="margin-bottom: 0;">This is a centralized, global platform built to connect individuals with neurodiversity-related services, including ADHD and autism therapy.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://thrivingautistic.org/" target="_blank" rel="noopener">Thriving Autistic</a></h3>
          <p style="margin-bottom: 0;">This organization offers an international network specifically dedicated to connecting individuals with neurodivergent psychologists, therapists, and coaches.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://neurodivergentinsights.com/ndi-directory/" target="_blank" rel="noopener">NDI Directory / Neurodivergent Insights</a></h3>
          <p style="margin-bottom: 0;">This resource lists neurodivergent-affirming medical professionals and globally accessible coaches who are committed to ongoing learning.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 48px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://ndtherapists.com/" target="_blank" rel="noopener">Neurodivergent Therapists</a></h3>
          <p style="margin-bottom: 0;">This grassroots directory connects neurodivergent clients with licensed therapists, psychologists, and social workers who are also neurodivergent.</p>
        </div>
        
        <div class="top-rule" style="margin-bottom: 48px; position: static; height: 1px; background: rgba(255,255,255,0.1);"></div>

        <h2 class="grad-b-sm" style="margin-bottom: 24px;">Inclusive and Accessible Mental Health Directories</h2>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://www.inclusivetherapists.com/" target="_blank" rel="noopener">Inclusive Therapists</a></h3>
          <p style="margin-bottom: 0;">This specialized directory focuses on connecting clients with culturally responsive, social justice-oriented therapists.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://openpathcollective.org/" target="_blank" rel="noopener">OpenPath Psychotherapy Collective</a></h3>
          <p style="margin-bottom: 0;">This directory allows individuals to find affordable, in-office, and online psychotherapy sessions.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://nqttcn.com/" target="_blank" rel="noopener">National Queer & Trans Therapists of Color Network</a></h3>
          <p style="margin-bottom: 0;">This directory is specifically built to help QTBIPOC individuals connect with QTBIPOC mental health practitioners.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://www.asianmhc.org/" target="_blank" rel="noopener">Asian Mental Health Collective</a></h3>
          <p style="margin-bottom: 0;">This is a dedicated resource to help individuals find culturally responsive mental health professionals.</p>
        </div>
        
        <div class="card" style="padding: 24px; margin-bottom: 16px;">
          <h3 style="margin-top: 0; margin-bottom: 8px;"><a href="https://latinxtherapy.com/" target="_blank" rel="noopener">Latinx Therapy</a></h3>
          <p style="margin-bottom: 0;">This national directory connects individuals with Latinx therapists operating in private practice.</p>
        </div>
        
      </div>
    </section>
"""

content = re.sub(r'(<section class="hero-narrow">.*?</section>).*?(</main>)', r'\1\n' + main_body + r'\n\2', content, flags=re.DOTALL)

with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Mental health resources page built successfully.")
