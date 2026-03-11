#!/usr/bin/env python3
import re

# Read the current index.html
with open('index.html', 'r') as f:
    content = f.read()

# Westchester towns with ZIP codes
towns = [
    ("Ardsley", "10502", "/ny/ardsley/"),
    ("Bronxville", "10708", "/ny/bronxville/"),
    ("Dobbs Ferry", "10522", "/ny/dobbs-ferry/"),
    ("Eastchester", "10709", "/ny/eastchester/"),
    ("Elmsford", "10523", "/ny/elmsford/"),
    ("Fairview", "10603", "/ny/fairview/"),
    ("Harrison", "10528", "/ny/harrison/"),
    ("Hartsdale", "10530", "/ny/hartsdale/"),
    ("Hastings-on-Hudson", "10706", "/ny/hastings-on-hudson/"),
    ("Irvington", "10533", "/ny/irvington/"),
    ("Larchmont", "10538", "/ny/larchmont/"),
    ("Mamaroneck", "10543", "/ny/mamaroneck/"),
    ("Mount Vernon", "10550, 10551, 10552, 10553", "/ny/mount-vernon/"),
    ("New Rochelle", "10801, 10802, 10804, 10805", "/ny/new-rochelle/"),
    ("Pelham Manor", "10803", "/ny/pelham-manor/"),
    ("Rye", "10580", "/ny/rye/"),
    ("Scarsdale", "10583", "/ny/scarsdale/"),
    ("Tarrytown", "10591", "/ny/tarrytown/"),
    ("Valhalla", "10595", "/ny/valhalla/"),
    ("Village of Pelham", "10803", "/ny/village-of-pelham/"),
    ("White Plains", "10601, 10602, 10603, 10604, 10605, 10606, 10607", "/ny/white-plains/"),
    ("Yonkers", "10701, 10702, 10703, 10704, 10705, 10710", "/ny/yonkers/"),
]

# Create the new service areas HTML
service_areas_html = '''
            <section class="service-areas" id="locations">
                <h2>Westchester County Towns We Service</h2>
                <p>We proudly serve all of <strong>Westchester County, NY</strong> with fast, reliable, same-day Miele appliance repair.</p>
                <div class="towns-grid">
'''

for town, zip_code, url in towns:
    service_areas_html += f'''                    <a href="{url}" class="town-card">
                        <h3>{town}</h3>
                        <span class="zip">ZIP: {zip_code}</span>
                    </a>
'''

service_areas_html += '''                </div>
            </section>
'''

# Add CSS for the towns grid
towns_css = '''
        .service-areas { padding: 80px 0; background: var(--gray); }
        .service-areas h2 { text-align: center; color: var(--blue); margin-bottom: 10px; }
        .service-areas > p { text-align: center; margin-bottom: 40px; }
        .towns-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; padding: 0 20px; }
        .town-card { display: block; background: white; padding: 25px 20px; border-radius: 10px; text-decoration: none; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.08); transition: all 0.3s; }
        .town-card:hover { transform: translateY(-5px); box-shadow: 0 8px 25px rgba(0,0,0,0.15); background: var(--blue); }
        .town-card:hover h3, .town-card:hover .zip { color: white; }
        .town-card h3 { margin: 0 0 8px 0; color: var(--blue); font-size: 1.1rem; }
        .town-card .zip { color: #666; font-size: 0.85rem; }
'''

# Find and replace the service areas section
# Look for the pattern that starts the service areas section
start_pattern = r'<section class="service-areas"[^>]*>.*?<h2>Service Areas'
end_pattern = r'</section>\s*(?=<section class="reviews"|<section class="contact"|<section class="faq"|<footer)'

# Find the service areas section and replace it
content = re.sub(
    r'(<section class="service-areas"[^>]*>.*?</section>)',
    service_areas_html,
    content,
    flags=re.DOTALL
)

# Add CSS before </style>
if '.towns-grid' not in content:
    content = content.replace('</style>', towns_css + '\n        </style>')

# Also update the navigation dropdown if it exists
# Replace borough tabs with a simple link to service areas
nav_update = '''<a href="#locations" class="nav-link">Service Areas</a>'''

# Write the updated content
with open('index.html', 'w') as f:
    f.write(content)

print("Index.html updated with Westchester towns!")
