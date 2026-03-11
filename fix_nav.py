#!/usr/bin/env python3

with open('index.html', 'r') as f:
    content = f.read()

# Replace navigation dropdown
old_nav = '''<div class="service-areas-submenu" id="serviceAreasSubmenu">
                            <li><a href="#borough-manhattan" class="scroll-link">Manhattan</a></li>
                            <li><a href="#borough-brooklyn" class="scroll-link">Brooklyn</a></li>
                            <li><a href="#borough-queens" class="scroll-link">Queens</a></li>
                            <li><a href="#borough-bronx" class="scroll-link">Bronx</a></li>
                        </div>'''

new_nav = '''<div class="service-areas-submenu" id="serviceAreasSubmenu" style="max-height: 400px; overflow-y: auto;">
                            <li><a href="/ny/ardsley/">Ardsley</a></li>
                            <li><a href="/ny/bronxville/">Bronxville</a></li>
                            <li><a href="/ny/dobbs-ferry/">Dobbs Ferry</a></li>
                            <li><a href="/ny/eastchester/">Eastchester</a></li>
                            <li><a href="/ny/elmsford/">Elmsford</a></li>
                            <li><a href="/ny/fairview/">Fairview</a></li>
                            <li><a href="/ny/harrison/">Harrison</a></li>
                            <li><a href="/ny/hartsdale/">Hartsdale</a></li>
                            <li><a href="/ny/hastings-on-hudson/">Hastings-on-Hudson</a></li>
                            <li><a href="/ny/irvington/">Irvington</a></li>
                            <li><a href="/ny/larchmont/">Larchmont</a></li>
                            <li><a href="/ny/mamaroneck/">Mamaroneck</a></li>
                            <li><a href="/ny/mount-vernon/">Mount Vernon</a></li>
                            <li><a href="/ny/new-rochelle/">New Rochelle</a></li>
                            <li><a href="/ny/pelham-manor/">Pelham Manor</a></li>
                            <li><a href="/ny/rye/">Rye</a></li>
                            <li><a href="/ny/scarsdale/">Scarsdale</a></li>
                            <li><a href="/ny/tarrytown/">Tarrytown</a></li>
                            <li><a href="/ny/valhalla/">Valhalla</a></li>
                            <li><a href="/ny/village-of-pelham/">Village of Pelham</a></li>
                            <li><a href="/ny/white-plains/">White Plains</a></li>
                            <li><a href="/ny/yonkers/">Yonkers</a></li>
                        </div>'''

content = content.replace(old_nav, new_nav)

# Fix hero text
content = content.replace(
    'Serving Manhattan, Brooklyn, Queens and Bronx',
    'Serving All of Westchester County, NY'
)

# Fix any remaining Manhattan references in hero/header
content = content.replace(
    'Premium Service • Factory-Trained Technicians • Serving Manhattan, Brooklyn, Queens and Bronx',
    'Premium Service • Factory-Trained Technicians • Serving All of Westchester County'
)

with open('index.html', 'w') as f:
    f.write(content)

print("Fixed navigation dropdown with 22 Westchester towns!")
