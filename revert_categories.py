import re

filepath = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/blog/categories/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_grid = """<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px;">
          
          <div style="padding: 32px; border-radius: 24px; background: #e2f5e3; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="nervous-system-regulation/index.html" class="tag" style="font-size: 14px; background: #1d6821; color: #fff; border: none; font-weight: 700;">nervous system regulation</a>
            </h3>
            <p style="color: #1d6821; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">What regulation actually means for neurodivergent brains, how it works, why most mainstream advice misses the mark, and what to do instead.</p>
          </div>

          <div style="padding: 32px; border-radius: 24px; background: #edeafe; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="autistic-experience/index.html" class="tag" style="font-size: 14px; background: #4a3a94; color: #fff; border: none; font-weight: 700;">autistic experience</a>
            </h3>
            <p style="color: #4a3a94; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Masking, burnout, late identification, social dynamics, and the ongoing process of figuring out what accommodation looks like for you.</p>
          </div>

          <div style="padding: 32px; border-radius: 24px; background: #fdf4e3; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="adhd/index.html" class="tag" style="font-size: 14px; background: #996409; color: #fff; border: none; font-weight: 700;">adhd</a>
            </h3>
            <p style="color: #996409; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Paralysis, executive function, the gap between knowing what to do and doing it, and regulation strategies that account for how ADHD brains actually work.</p>
          </div>

          <div style="padding: 32px; border-radius: 24px; background: #e6f4fa; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="sensory-processing/index.html" class="tag" style="font-size: 14px; background: #005a8c; color: #fff; border: none; font-weight: 700;">sensory processing</a>
            </h3>
            <p style="color: #005a8c; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Sensory overload, interoception, proprioception, and practical approaches to managing a sensory environment that wasn't designed with you in mind.</p>
          </div>

          <div style="padding: 32px; border-radius: 24px; background: #e0f2f1; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="somatic-practices/index.html" class="tag" style="font-size: 14px; background: #00695c; color: #fff; border: none; font-weight: 700;">somatic practices</a>
            </h3>
            <p style="color: #00695c; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Body-based regulation tools grounded in the Community Resilience Model. Grounding, resourcing, tracking, and other skills you can use right now.</p>
          </div>

          <div style="padding: 32px; border-radius: 24px; background: #eceff1; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="science-evidence/index.html" class="tag" style="font-size: 14px; background: #455a64; color: #fff; border: none; font-weight: 700;">science & evidence</a>
            </h3>
            <p style="color: #455a64; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Research reviews, framework critiques, and the science behind nervous system regulation. Where the evidence is strong, where it's contested, and why that matters.</p>
          </div>

          <div style="padding: 32px; border-radius: 24px; background: #e8eaf6; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="workplace/index.html" class="tag" style="font-size: 14px; background: #283593; color: #fff; border: none; font-weight: 700;">workplace & professional life</a>
            </h3>
            <p style="color: #283593; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Surviving and functioning in workplaces that weren't built for neurodivergent people. Masking at work, accommodation, burnout, and professional identity.</p>
          </div>

          <div style="padding: 32px; border-radius: 24px; background: #fce4ec; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="lived-experience/index.html" class="tag" style="font-size: 14px; background: #ad1457; color: #fff; border: none; font-weight: 700;">lived experience</a>
            </h3>
            <p style="color: #ad1457; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Personal essays, late diagnosis stories, and the intersections of neurodivergence with the rest of life.</p>
          </div>

          <div style="padding: 32px; border-radius: 24px; background: #fae9e6; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
            <h3 style="margin-top:0; margin-bottom:16px;">
              <a href="wired-divergent/index.html" class="tag" style="font-size: 14px; background: #9e3520; color: #fff; border: none; font-weight: 700;">wired divergent</a>
            </h3>
            <p style="color: #9e3520; margin: 0; font-size: 15px; font-weight: 500; line-height: 1.6;">Companion posts for episodes of Wired Divergent: Nervous System Regulation for Neurodivergent Brains. Each post expands on the episode's topic with additional context, links, and resources.</p>
          </div>

        </div>"""

content = re.sub(r'<div style="display: grid; grid-template-columns: repeat\(auto-fill, minmax\(300px, 1fr\)\); gap: 16px;">.*?</div>\s*</div>\s*</section>', new_grid + '\n      </div>\n    </section>', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Categories reverted successfully.")
