#!/usr/bin/env python3
import re

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Westchester towns
towns = [
    ("ardsley", "Ardsley", "10502"),
    ("bronxville", "Bronxville", "10708"),
    ("dobbs-ferry", "Dobbs Ferry", "10522"),
    ("eastchester", "Eastchester", "10709"),
    ("elmsford", "Elmsford", "10523"),
    ("fairview", "Fairview", "10603"),
    ("harrison", "Harrison", "10528"),
    ("hartsdale", "Hartsdale", "10530"),
    ("hastings-on-hudson", "Hastings-on-Hudson", "10706"),
    ("irvington", "Irvington", "10533"),
    ("larchmont", "Larchmont", "10538"),
    ("mamaroneck", "Mamaroneck", "10543"),
    ("mount-vernon", "Mount Vernon", "10550, 10551, 10552"),
    ("new-rochelle", "New Rochelle", "10801, 10802, 10804"),
    ("pelham-manor", "Pelham Manor", "10803"),
    ("rye", "Rye", "10580"),
    ("scarsdale", "Scarsdale", "10583"),
    ("tarrytown", "Tarrytown", "10591"),
    ("valhalla", "Valhalla", "10595"),
    ("village-of-pelham", "Village of Pelham", "10803"),
    ("white-plains", "White Plains", "10601, 10603, 10605"),
    ("yonkers", "Yonkers", "10701, 10703, 10704, 10705"),
]

# Create town list items
town_items = ""
for slug, name, zipcode in towns:
    town_items += f'                                    <li onclick="this.classList.toggle(\'show-zip\')"><h3><a href="/ny/{slug}/">{name}</a></h3><div class="zip-code">ZIP: {zipcode}</div></li>\n'

# Replace borough tabs - change to single Westchester tab
old_tabs = '''<button class="sa-borough-tab active" data-borough="0">Manhattan</button>
                            <button class="sa-borough-tab" data-borough="1">Brooklyn</button>
                            <button class="sa-borough-tab" data-borough="2">Queens</button>
                            <button class="sa-borough-tab" data-borough="3">Bronx</button>'''

new_tabs = '''<button class="sa-borough-tab active" data-borough="0">Westchester County</button>'''

content = content.replace(old_tabs, new_tabs)

# Also try other variations
content = content.replace('data-borough="0">Westchester</button>', 'data-borough="0">Westchester County</button>')

# Replace the View All button text
content = re.sub(r'View All [^<]+ Service Areas', 'View All Westchester County Service Areas', content)

# Replace "Manhattan Neighborhoods We Service" etc with Westchester
content = re.sub(r'(Manhattan|Brooklyn|Queens|Bronx|Westchester) Neighborhoods We Service', 'Westchester County Towns We Service', content)

# Find and replace the Manhattan/first slide content
# This is tricky - we need to find the ul after "slide-manhattan" and replace its contents

# Pattern to find the Manhattan slide content
pattern = r'(<div class="sa-slide"[^>]*id="slide-manhattan"[^>]*>\s*<h2>[^<]+</h2>\s*<ul>)(.*?)(</ul>\s*</div>)'

def replace_towns(match):
    return match.group(1) + '\n' + town_items + '                                ' + match.group(3)

content = re.sub(pattern, replace_towns, content, flags=re.DOTALL)

# Remove other borough slides (Brooklyn, Queens, Bronx)
content = re.sub(r'<div class="sa-slide"[^>]*id="slide-brooklyn"[^>]*>.*?</div>\s*(?=<div class="sa-slide"|</div>\s*</div>\s*</div>\s*</section>)', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="sa-slide"[^>]*id="slide-queens"[^>]*>.*?</div>\s*(?=<div class="sa-slide"|</div>\s*</div>\s*</div>\s*</section>)', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="sa-slide"[^>]*id="slide-bronx"[^>]*>.*?</div>\s*(?=</div>\s*</div>\s*</div>\s*</section>)', '', content, flags=re.DOTALL)

# Update location references
content = content.replace('NYC', 'Westchester')
content = content.replace('New York City', 'Westchester County')

# Update the schema areaServed
old_area = '''"areaServed": [
            {"@type": "City", "name": "Manhattan"},
            {"@type": "City", "name": "Brooklyn"},
            {"@type": "City", "name": "Queens"},
            {"@type": "City", "name": "Bronx"}
        ]'''

new_area = '''"areaServed": [
            {"@type": "City", "name": "White Plains"},
            {"@type": "City", "name": "Yonkers"},
            {"@type": "City", "name": "New Rochelle"},
            {"@type": "City", "name": "Scarsdale"},
            {"@type": "City", "name": "Mount Vernon"}
        ]'''

content = content.replace(old_area, new_area)

# Update address
content = content.replace('"streetAddress": "401 Park Ave S"', '"streetAddress": "1 Martine Avenue"')
content = content.replace('"addressLocality": "New York"', '"addressLocality": "White Plains"')

# Write back
with open('index.html', 'w') as f:
    f.write(content)

print("Template updated with Westchester towns!")
print(f"Added {len(towns)} towns to the service areas")
