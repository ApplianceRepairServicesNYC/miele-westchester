#!/usr/bin/env python3
import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the 4 borough cards with 1 Westchester card
old_cards = '''<div class="borough-card" id="borough-manhattan">
                        <div class="pin-icon">
                            <svg viewBox="0 0 24 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 0C5.4 0 0 5.4 0 12c0 9 12 24 12 24s12-15 12-24c0-6.6-5.4-12-12-12z" fill="#c41e3a"/>
                                <circle cx="12" cy="12" r="5" fill="#fff"/>
                            </svg>
                        </div>
                        <h3>Manhattan, NY</h3>
                        <p>Serving All Manhattan Neighborhoods</p>
                        <a href="https://www.google.com/maps/place/Manhattan,+New+York,+NY" target="_blank" rel="noopener" class="map-btn">View on Google Maps →</a>
                    </div>
                    <div class="borough-card" id="borough-brooklyn">
                        <div class="pin-icon">
                            <svg viewBox="0 0 24 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 0C5.4 0 0 5.4 0 12c0 9 12 24 12 24s12-15 12-24c0-6.6-5.4-12-12-12z" fill="#c41e3a"/>
                                <circle cx="12" cy="12" r="5" fill="#fff"/>
                            </svg>
                        </div>
                        <h3>Brooklyn, NY</h3>
                        <p>Serving All Brooklyn Neighborhoods</p>
                        <a href="https://www.google.com/maps/place/Brooklyn,+New+York,+NY" target="_blank" rel="noopener" class="map-btn">View on Google Maps →</a>
                    </div>
                    <div class="borough-card" id="borough-queens">
                        <div class="pin-icon">
                            <svg viewBox="0 0 24 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 0C5.4 0 0 5.4 0 12c0 9 12 24 12 24s12-15 12-24c0-6.6-5.4-12-12-12z" fill="#c41e3a"/>
                                <circle cx="12" cy="12" r="5" fill="#fff"/>
                            </svg>
                        </div>
                        <h3>Queens, NY</h3>
                        <p>Serving All Queens Neighborhoods</p>
                        <a href="https://www.google.com/maps/place/Queens,+New+York,+NY" target="_blank" rel="noopener" class="map-btn">View on Google Maps →</a>
                    </div>
                    <div class="borough-card" id="borough-bronx">
                        <div class="pin-icon">
                            <svg viewBox="0 0 24 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 0C5.4 0 0 5.4 0 12c0 9 12 24 12 24s12-15 12-24c0-6.6-5.4-12-12-12z" fill="#c41e3a"/>
                                <circle cx="12" cy="12" r="5" fill="#fff"/>
                            </svg>
                        </div>
                        <h3>The Bronx, NY</h3>
                        <p>Serving All Bronx Neighborhoods</p>
                        <a href="https://www.google.com/maps/place/Bronx,+New+York,+NY" target="_blank" rel="noopener" class="map-btn">View on Google Maps →</a>
                    </div>'''

new_card = '''<div class="borough-card" id="borough-westchester" style="grid-column: 1 / -1; max-width: 500px; margin: 0 auto;">
                        <div class="pin-icon">
                            <svg viewBox="0 0 24 36" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 0C5.4 0 0 5.4 0 12c0 9 12 24 12 24s12-15 12-24c0-6.6-5.4-12-12-12z" fill="#c41e3a"/>
                                <circle cx="12" cy="12" r="5" fill="#fff"/>
                            </svg>
                        </div>
                        <h3>Westchester County, NY</h3>
                        <p>Serving All 22 Westchester County Towns</p>
                        <a href="https://www.google.com/maps/place/Westchester+County,+NY" target="_blank" rel="noopener" class="map-btn">View on Google Maps →</a>
                    </div>'''

content = content.replace(old_cards, new_card)

# Update the description text
content = content.replace(
    'We proudly serve <strong>Manhattan, Brooklyn, Queens and The Bronx</strong>',
    'We proudly serve <strong>all of Westchester County, NY</strong>'
)

# Replace borough tabs with single Westchester tab
old_tabs = '''<button class="sa-borough-tab active" data-borough="0">Manhattan</button>
                            <button class="sa-borough-tab" data-borough="1">Brooklyn</button>
                            <button class="sa-borough-tab" data-borough="2">Bronx</button>
                            <button class="sa-borough-tab" data-borough="3">Queens</button>'''

new_tabs = '''<button class="sa-borough-tab active" data-borough="0">All Towns</button>'''

content = content.replace(old_tabs, new_tabs)

# Update form placeholder
content = content.replace('123 Main St, Manhattan, NY 10001', '123 Main St, White Plains, NY 10601')

with open('index.html', 'w') as f:
    f.write(content)

print("Fixed! Replaced 4 borough cards with 1 Westchester card")
