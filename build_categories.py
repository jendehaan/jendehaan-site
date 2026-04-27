import os
import re

template_path = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/blog/categories/neurodivergence/index.html'
base_dir = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/blog/categories'

categories = [
    {
        "slug": "nervous-system-regulation",
        "name": "Nervous System Regulation",
        "desc": "What regulation actually means for neurodivergent brains, how it works, why most mainstream advice misses the mark, and what to do instead.",
        "bg_color": "#1d6821"
    },
    {
        "slug": "autistic-experience",
        "name": "Autistic Experience",
        "desc": "Masking, burnout, late identification, social dynamics, and the ongoing process of figuring out what accommodation looks like for you.",
        "bg_color": "#4a3a94"
    },
    {
        "slug": "adhd",
        "name": "ADHD",
        "desc": "Paralysis, executive function, the gap between knowing what to do and doing it, and regulation strategies that account for how ADHD brains actually work.",
        "bg_color": "#996409"
    },
    {
        "slug": "sensory-processing",
        "name": "Sensory Processing",
        "desc": "Sensory overload, interoception, proprioception, and practical approaches to managing a sensory environment that wasn't designed with you in mind.",
        "bg_color": "#005a8c"
    },
    {
        "slug": "somatic-practices",
        "name": "Somatic Practices",
        "desc": "Body-based regulation tools grounded in the Community Resilience Model. Grounding, resourcing, tracking, and other skills you can use right now.",
        "bg_color": "#00695c"
    },
    {
        "slug": "science-evidence",
        "name": "Science & Evidence",
        "desc": "Research reviews, framework critiques, and the science behind nervous system regulation. Where the evidence is strong, where it's contested, and why that matters.",
        "bg_color": "#455a64"
    },
    {
        "slug": "workplace",
        "name": "Workplace & Professional Life",
        "desc": "Surviving and functioning in workplaces that weren't built for neurodivergent people. Masking at work, accommodation, burnout, and professional identity.",
        "bg_color": "#283593"
    },
    {
        "slug": "lived-experience",
        "name": "Lived Experience",
        "desc": "Personal essays, late diagnosis stories, and the intersections of neurodivergence with the rest of life.",
        "bg_color": "#ad1457"
    },
    {
        "slug": "wired-divergent",
        "name": "Wired Divergent",
        "desc": "Companion posts for episodes of Wired Divergent: Nervous System Regulation for Neurodivergent Brains. Each post expands on the episode's topic with additional context, links, and resources.",
        "bg_color": "#9e3520"
    }
]

with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

for cat in categories:
    cat_dir = os.path.join(base_dir, cat['slug'])
    os.makedirs(cat_dir, exist_ok=True)
    
    new_content = template_content
    
    # Replace title
    new_content = re.sub(r'<title>.*?</title>', f'<title>Category: {cat["name"]} — Jen deHaan</title>', new_content)
    
    # Replace meta description
    new_content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{cat["desc"]}">', new_content)
    
    # Replace H1 string
    h1_pattern = r'<h1 class="display">Posts Tagged: <span class="tag.*?>.*?</span></h1>'
    new_h1 = f'<h1 class="display">Posts Tagged: <span class="tag" style="font-size:32px; padding: 4px 16px; position:relative; top:-4px; background: {cat["bg_color"]}; color: #fff; border: none; font-weight: 700;">{cat["name"].lower()}</span></h1>'
    new_content = re.sub(h1_pattern, new_h1, new_content)
    
    # Replace paragraph description
    desc_pattern = r'<p class="hero-desc">.*?</p>'
    new_desc = f'<p class="hero-desc">{cat["desc"]}</p>'
    new_content = re.sub(desc_pattern, new_desc, new_content)
    
    file_path = os.path.join(cat_dir, 'index.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Category pages built successfully.")
