import re

filepath = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/blog/categories/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_grid = """<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px;">
          
          <div class="card" style="padding: 32px; display: flex; flex-direction: column;">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="nervous-system-regulation/index.html" class="tag tag-nervous" style="border: none; font-weight: 700;">Nervous System Regulation</a>
            </h3>
            <p style="color: #aebbc1; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">What regulation actually means for neurodivergent brains, how it works, why most mainstream advice misses the mark, and what to do instead.</p>
          </div>

          <div class="card" style="padding: 32px; display: flex; flex-direction: column;">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="autistic-experience/index.html" class="tag tag-autistic" style="border: none; font-weight: 700;">Autistic Experience</a>
            </h3>
            <p style="color: #aebbc1; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Masking, burnout, late identification, social dynamics, and the ongoing process of figuring out what accommodation looks like for you.</p>
          </div>

          <div class="card" style="padding: 32px; display: flex; flex-direction: column;">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="adhd/index.html" class="tag tag-adhd" style="border: none; font-weight: 700;">ADHD</a>
            </h3>
            <p style="color: #aebbc1; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Paralysis, executive function, the gap between knowing what to do and doing it, and regulation strategies that account for how ADHD brains actually work.</p>
          </div>

          <div class="card" style="padding: 32px; display: flex; flex-direction: column;">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="sensory-processing/index.html" class="tag tag-sensory" style="border: none; font-weight: 700;">Sensory Processing</a>
            </h3>
            <p style="color: #aebbc1; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Sensory overload, interoception, proprioception, and practical approaches to managing a sensory environment that wasn't designed with you in mind.</p>
          </div>

          <div class="card" style="padding: 32px; display: flex; flex-direction: column;">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="somatic-practices/index.html" class="tag tag-somatic" style="border: none; font-weight: 700;">Somatic Practices</a>
            </h3>
            <p style="color: #aebbc1; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Body-based regulation tools grounded in the Community Resilience Model. Grounding, resourcing, tracking, and other skills you can use right now.</p>
          </div>

          <div class="card" style="padding: 32px; display: flex; flex-direction: column;">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="science-evidence/index.html" class="tag tag-science" style="border: none; font-weight: 700;">Science & Evidence</a>
            </h3>
            <p style="color: #aebbc1; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Research reviews, framework critiques, and the science behind nervous system regulation. Where the evidence is strong, where it's contested, and why that matters.</p>
          </div>

          <div class="card" style="padding: 32px; display: flex; flex-direction: column;">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="workplace/index.html" class="tag tag-workplace" style="border: none; font-weight: 700;">Workplace & Professional Life</a>
            </h3>
            <p style="color: #aebbc1; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Surviving and functioning in workplaces that weren't built for neurodivergent people. Masking at work, accommodation, burnout, and professional identity.</p>
          </div>

          <div class="card" style="padding: 32px; display: flex; flex-direction: column;">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="lived-experience/index.html" class="tag tag-lived" style="border: none; font-weight: 700;">Lived Experience</a>
            </h3>
            <p style="color: #aebbc1; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Personal essays, late diagnosis stories, and the intersections of neurodivergence with the rest of life.</p>
          </div>

          <div class="card" style="padding: 32px; display: flex; flex-direction: column;">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="wired-divergent/index.html" class="tag tag-wired" style="border: none; font-weight: 700;">Wired Divergent</a>
            </h3>
            <p style="color: #aebbc1; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Companion posts for episodes of Wired Divergent: Nervous System Regulation for Neurodivergent Brains. Each post expands on the episode's topic with additional context, links, and resources.</p>
          </div>

        </div>"""

content = re.sub(r'<div style="display: grid; grid-template-columns: repeat\(auto-fill, minmax\(300px, 1fr\)\); gap: 16px;">.*?</div>\s*</div>\s*</section>', new_grid + '\n      </div>\n    </section>', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Categories updated successfully.")
