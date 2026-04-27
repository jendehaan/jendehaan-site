import re

with open('style.css', 'r') as f:
    css = f.read()

# 1. Update basic grey backgrounds to dark teal
css = re.sub(r'#111(?!\d|a-f|A-F)', '#061417', css) # body
css = re.sub(r'#161616', '#091c21', css) # cards
css = re.sub(r'#1a1a1a', '#0b242a', css) # tags, inputs
css = re.sub(r'#222(?!\d|a-f|A-F)', '#0e2b33', css) # yt-thumb

# Update grey borders to teal tinted
css = re.sub(r'#2a2a2a', '#143640', css)
css = re.sub(r'#333(?!\d|a-f|A-F)', '#1b4754', css)

# Update glassmorphism rgba grays
css = css.replace('rgba(20, 20, 20', 'rgba(6, 20, 23')
css = css.replace('rgba(30, 30, 30', 'rgba(10, 35, 40')
css = css.replace('rgba(25, 20, 45', 'rgba(8, 28, 33') # newsletter radial gradient

# Update textual elements' rainbow gradients
subtle_teal_90 = 'linear-gradient(90deg, #40c4b5, #63e3d4)'
subtle_teal_135 = 'linear-gradient(135deg, #40c4b5, #63e3d4)'

css = css.replace('linear-gradient(90deg, #E8593C, #F2A623, #4CAF50, #3B8BD4, #7B61FF)', subtle_teal_90)
css = css.replace('linear-gradient(135deg, #E8593C 0%, #F2A623 30%, #4CAF50 65%, #3B8BD4 100%)', subtle_teal_135)
css = css.replace('linear-gradient(135deg, #E8593C 0%, #F2A623 45%, #3B8BD4 100%)', subtle_teal_135)

with open('style.css', 'w') as f:
    f.write(css)

with open('design.md', 'r') as f:
    design = f.read()

design = design.replace('#111', '#061417 (Dark Teal)')
design = design.replace('#161616', '#091c21')
design = design.replace('#2a2a2a', '#143640')
design = design.replace('rgba(20, 20, 20', 'rgba(6, 20, 23')

import sys
sys.stdout.write("Modification complete.\n")
