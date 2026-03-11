#!/usr/bin/env python3
import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix meta keywords
content = re.sub(
    r'Miele oven repair Manhattan, Miele dishwasher repair Brooklyn, Miele refrigerator repair Queens, Miele washer repair Bronx',
    'Miele oven repair Westchester, Miele dishwasher repair White Plains, Miele refrigerator repair Yonkers, Miele washer repair New Rochelle',
    content
)

# Remove slide-bronx, slide-queens, slide-brooklyn sections entirely
content = re.sub(r'<div class="sa-slide" id="slide-brooklyn">.*?</div>\s*(?=<div class="sa-slide"|</div>\s*</div>\s*</div>)', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="sa-slide" id="slide-queens">.*?</div>\s*(?=<div class="sa-slide"|</div>\s*</div>\s*</div>)', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="sa-slide" id="slide-bronx">.*?</div>\s*(?=<div class="sa-slide"|</div>\s*</div>\s*</div>)', '', content, flags=re.DOTALL)

# Rename slide-manhattan to slide-westchester
content = content.replace('id="slide-manhattan"', 'id="slide-westchester"')

# Fix the footer/disclaimer text
content = re.sub(
    r'including Manhattan, Brooklyn, Queens, and the Bronx',
    'including White Plains, Yonkers, New Rochelle, Scarsdale, and all Westchester County towns',
    content
)

content = re.sub(
    r'Westchester County metropolitan area, including Manhattan, Brooklyn, Queens, and the Bronx',
    'Westchester County, NY area including White Plains, Yonkers, New Rochelle, Scarsdale, and all surrounding towns',
    content
)

# Replace any remaining standalone mentions
content = content.replace('Manhattan, NY', 'Westchester County, NY')
content = content.replace('Brooklyn, NY', 'White Plains, NY')
content = content.replace('Queens, NY', 'Yonkers, NY')
content = content.replace('Bronx, NY', 'New Rochelle, NY')
content = content.replace('The Bronx, NY', 'Scarsdale, NY')

# Don't replace Bronxville (it's a Westchester town)
# Make sure we didn't break Bronxville
content = content.replace('New Rochelleville', 'Bronxville')

with open('index.html', 'w') as f:
    f.write(content)

print("Removed all NYC mentions!")
