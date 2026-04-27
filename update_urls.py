import re

filepath = '/Users/jendehaan/Library/Mobile Documents/iCloud~md~obsidian/Documents/JenVault/SITES/jendehaan-site/jendehaan-site/podcaster-resources/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace URLs inside pr-cm-ref-list
def repl_ref_list(match):
    block = match.group(0)
    # Replace stereoforest.com/episodes/ with minute.captivate.fm/episode/
    # and remove trailing slashes if they exist before the quote
    block = block.replace('https://stereoforest.com/episodes/', 'https://minute.captivate.fm/episode/')
    block = re.sub(r'https://minute\.captivate\.fm/episode/([^"]+)/"', r'https://minute.captivate.fm/episode/\1"', block)
    return block

content = re.sub(r'<div class="pr-cm-ref-list">.*?</div>', repl_ref_list, content, flags=re.DOTALL)

# Now for the main index. The section is after '<h2>The Credibility Minute — All 55 Episodes</h2>'
# We can find the pr-ep-index block that follows it.
def repl_main_index(match):
    block = match.group(0)
    block = block.replace('https://stereoforest.com/episodes/', 'https://minute.captivate.fm/episode/')
    block = re.sub(r'https://minute\.captivate\.fm/episode/([^"]+)/"', r'https://minute.captivate.fm/episode/\1"', block)
    
    # Replace the "coming this week" for 51-55
    block = block.replace(
        '<div class="pr-ep-row ep-soon"><span class="pr-ep-n">51</span><span class="pr-ep-t">Coming this week</span></div>',
        '<div class="pr-ep-row"><span class="pr-ep-n">51</span><span class="pr-ep-t"><a href="https://minute.captivate.fm/episode/51-your-imaginary-audience-is-holding-your-solo-podcasting-back" target="_blank">Your Imaginary Audience is Holding Your Solo Podcasting Back</a></span></div>'
    )
    block = block.replace(
        '<div class="pr-ep-row ep-soon"><span class="pr-ep-n">52</span><span class="pr-ep-t">Coming this week</span></div>',
        '<div class="pr-ep-row"><span class="pr-ep-n">52</span><span class="pr-ep-t"><a href="https://minute.captivate.fm/episode/52-why-you-need-a-pile-of-cold-pancakes-in-your-story-to-resonate" target="_blank">Why You Need a Pile of Cold Pancakes in Your Story to Resonate</a></span></div>'
    )
    block = block.replace(
        '<div class="pr-ep-row ep-soon"><span class="pr-ep-n">53</span><span class="pr-ep-t">Coming this week</span></div>',
        '<div class="pr-ep-row"><span class="pr-ep-n">53</span><span class="pr-ep-t"><a href="https://minute.captivate.fm/episode/53-treating-your-listener-like-a-co-worker-vocally-at-least" target="_blank">Treating Your Listener Like a Co-worker (Vocally, At Least)</a></span></div>'
    )
    block = block.replace(
        '<div class="pr-ep-row ep-soon"><span class="pr-ep-n">54</span><span class="pr-ep-t">Coming this week</span></div>',
        '<div class="pr-ep-row"><span class="pr-ep-n">54</span><span class="pr-ep-t"><a href="https://minute.captivate.fm/episode/54-the-jam-study-a-lesson-in-listener-psychology" target="_blank">The Jam Study: A Lesson in Listener Psychology</a></span></div>'
    )
    block = block.replace(
        '<div class="pr-ep-row ep-soon"><span class="pr-ep-n">55</span><span class="pr-ep-t">Coming this week</span></div>',
        '<div class="pr-ep-row"><span class="pr-ep-n">55</span><span class="pr-ep-t"><a href="https://minute.captivate.fm/episode/55-when-more-options-are-actually-good-in-your-episode" target="_blank">When More Options Are Actually Good in Your Episode</a></span></div>'
    )
    
    return block

content = re.sub(r'<h2>The Credibility Minute — All 55 Episodes</h2>.*?(<div class="pr-ep-index">.*?</div>\s*</div>)', lambda m: m.group(0).replace(m.group(1), repl_main_index(re.match(r'.*', m.group(1), re.DOTALL))), content, flags=re.DOTALL)

# Let's fix the trailer link in the main index too
trailer_str = '<a href="https://stereoforest.com/episodes/welcome-to-the-credibility-minute-a-new-micro-podcast/" target="_blank" style="color:#666;">Trailer: Welcome to the Credibility Minute</a>'
trailer_repl = '<a href="https://minute.captivate.fm/episode/welcome-to-the-credibility-minute-a-new-micro-podcast" target="_blank" style="color:#666;">Trailer: Welcome to the Credibility Minute</a>'
content = content.replace(trailer_str, trailer_repl)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("URLs updated successfully.")
