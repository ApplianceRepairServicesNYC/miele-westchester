#!/usr/bin/env python3
import os

towns = [
    ("ardsley", "Ardsley"),
    ("bronxville", "Bronxville"),
    ("dobbs-ferry", "Dobbs Ferry"),
    ("eastchester", "Eastchester"),
    ("elmsford", "Elmsford"),
    ("fairview", "Fairview"),
    ("harrison", "Harrison"),
    ("hartsdale", "Hartsdale"),
    ("hastings-on-hudson", "Hastings-on-Hudson"),
    ("irvington", "Irvington"),
    ("larchmont", "Larchmont"),
    ("mamaroneck", "Mamaroneck"),
    ("mount-vernon", "Mount Vernon"),
    ("new-rochelle", "New Rochelle"),
    ("pelham-manor", "Pelham Manor"),
    ("rye", "Rye"),
    ("scarsdale", "Scarsdale"),
    ("tarrytown", "Tarrytown"),
    ("valhalla", "Valhalla"),
    ("village-of-pelham", "Village of Pelham"),
    ("white-plains", "White Plains"),
    ("yonkers", "Yonkers"),
]

template = '''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <link rel="preload" as="image" href="/assets/images/appliances/hero-appliances.webp?v=3" fetchpriority="high">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Miele Appliance Repair in {town_name}, NY | Same-Day Service</title>
    <meta name="description" content="Professional Miele appliance repair services in {town_name}, Westchester County, NY. Same-day washer, dryer, refrigerator, dishwasher, and oven repair by certified technicians.">
    <meta name="keywords" content="Miele appliance repair {town_name}, Miele washer repair {town_name} NY, Miele dryer repair, Miele refrigerator repair, Miele dishwasher repair, Miele oven repair, same day Miele repair Westchester">
    <meta name="author" content="Miele Appliance Repair Westchester">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://miele-westchester.pages.dev/ny/{town_slug}/">
    <link rel="sitemap" href="https://miele-westchester.pages.dev/sitemap.xml">
    <meta property="og:title" content="Miele Appliance Repair {town_name} NY">
    <meta property="og:description" content="Fast, reliable Miele appliance repair in {town_name}, Westchester County NY. Same-day repair for washers, dryers, ovens, refrigerators & more.">
    <meta property="og:url" content="https://miele-westchester.pages.dev/ny/{town_slug}/">
    <meta property="og:type" content="website">
    <link rel="icon" type="image/png" href="/favicon.png" sizes="180x180">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Miele Appliance Repair {town_name}",
        "@id": "https://miele-westchester.pages.dev/ny/{town_slug}/",
        "url": "https://miele-westchester.pages.dev/ny/{town_slug}/",
        "priceRange": "$$",
        "address": {{
            "@type": "PostalAddress",
            "addressLocality": "{town_name}",
            "addressRegion": "NY",
            "addressCountry": "US"
        }},
        "areaServed": {{
            "@type": "City",
            "name": "{town_name}"
        }},
        "aggregateRating": {{
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "247"
        }}
    }}
    </script>
    <style>
        :root {{ --blue: #003087; --red: #e41e26; --gray: #f8f9fa; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; color: #333; background: #fff; line-height: 1.6; }}
        h1, h2, h3 {{ font-weight: 700; color: var(--blue); }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        header {{ background: var(--blue); color: white; padding: 20px 0; position: fixed; width: 100%; top: 0; z-index: 1000; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }}
        .nav-wrapper {{ display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 1.5rem; font-weight: 700; color: white; text-decoration: none; }}
        .cta-btn {{ background: var(--red); color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: 600; }}
        .cta-btn:hover {{ background: #c41e3a; }}
        .hero {{ background: linear-gradient(135deg, var(--blue) 0%, #001a4d 100%); color: white; padding: 140px 0 80px; text-align: center; }}
        .hero h1 {{ font-size: 2.5rem; margin-bottom: 20px; }}
        .hero p {{ font-size: 1.2rem; opacity: 0.9; max-width: 600px; margin: 0 auto 30px; }}
        .services {{ padding: 80px 0; background: var(--gray); }}
        .services h2 {{ text-align: center; margin-bottom: 50px; }}
        .services-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; }}
        .service-card {{ background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); }}
        .service-card h3 {{ margin-top: 0; }}
        .why-us {{ padding: 80px 0; }}
        .why-us h2 {{ text-align: center; margin-bottom: 50px; }}
        .features {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; }}
        .feature {{ text-align: center; padding: 20px; }}
        .feature-icon {{ font-size: 3rem; margin-bottom: 15px; }}
        .contact {{ padding: 80px 0; background: var(--blue); color: white; text-align: center; }}
        .contact h2 {{ color: white; margin-bottom: 30px; }}
        footer {{ background: #001a4d; color: white; padding: 40px 0; text-align: center; }}
        footer a {{ color: #fff; opacity: 0.8; }}
        .breadcrumb {{ padding: 100px 0 20px; background: var(--gray); }}
        .breadcrumb a {{ color: var(--blue); text-decoration: none; }}
        @media (max-width: 768px) {{ .hero h1 {{ font-size: 1.8rem; }} .hero {{ padding: 120px 0 60px; }} }}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <nav class="nav-wrapper">
                <a href="/" class="logo">Miele Repair Westchester</a>
                <a href="#contact" class="cta-btn">Get Free Estimate</a>
            </nav>
        </div>
    </header>

    <div class="breadcrumb">
        <div class="container">
            <a href="/">Home</a> &raquo; <a href="/ny/">Westchester County</a> &raquo; {town_name}
        </div>
    </div>

    <section class="hero">
        <div class="container">
            <h1>Miele Appliance Repair in {town_name}, NY</h1>
            <p>Professional Miele appliance repair services in {town_name}, Westchester County. Same-day service available for all Miele appliances.</p>
            <a href="#contact" class="cta-btn">Schedule Service Today</a>
        </div>
    </section>

    <section class="services">
        <div class="container">
            <h2>Miele Appliances We Repair in {town_name}</h2>
            <div class="services-grid">
                <div class="service-card">
                    <h3>Miele Washer Repair</h3>
                    <p>Expert repair for all Miele washing machine models in {town_name}. We fix spin issues, drainage problems, error codes, and more.</p>
                </div>
                <div class="service-card">
                    <h3>Miele Dryer Repair</h3>
                    <p>Professional Miele dryer repair service. We handle heating issues, drum problems, and ventilation repairs in {town_name}.</p>
                </div>
                <div class="service-card">
                    <h3>Miele Dishwasher Repair</h3>
                    <p>Fast Miele dishwasher repair in {town_name}. Fixing leaks, cleaning issues, pump failures, and electronic problems.</p>
                </div>
                <div class="service-card">
                    <h3>Miele Refrigerator Repair</h3>
                    <p>Certified Miele refrigerator repair for {town_name} residents. Cooling issues, ice maker repairs, and compressor service.</p>
                </div>
                <div class="service-card">
                    <h3>Miele Oven & Range Repair</h3>
                    <p>Expert Miele oven and range repair in {town_name}. Heating elements, igniters, thermostats, and control board repairs.</p>
                </div>
                <div class="service-card">
                    <h3>Miele Cooktop Repair</h3>
                    <p>Professional Miele cooktop repair service. Induction, gas, and electric cooktop repairs in {town_name}, NY.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="why-us">
        <div class="container">
            <h2>Why Choose Us for Miele Repair in {town_name}?</h2>
            <div class="features">
                <div class="feature">
                    <div class="feature-icon">⚡</div>
                    <h3>Same-Day Service</h3>
                    <p>Fast response times for {town_name} residents. Most repairs completed same day.</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">🔧</div>
                    <h3>Certified Technicians</h3>
                    <p>Factory-trained experts specializing in Miele appliances.</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">✓</div>
                    <h3>Genuine Parts</h3>
                    <p>We use only authentic Miele replacement parts for lasting repairs.</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">💰</div>
                    <h3>Upfront Pricing</h3>
                    <p>No hidden fees. Free estimates for {town_name} service calls.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="contact" id="contact">
        <div class="container">
            <h2>Schedule Miele Repair in {town_name}</h2>
            <p>Contact us today for fast, reliable Miele appliance repair service in {town_name}, Westchester County.</p>
            <a href="/" class="cta-btn">Request Service</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>Miele Appliance Repair Westchester County</p>
            <p>Serving {town_name} and all of Westchester County, NY</p>
            <p><a href="/">Home</a> | <a href="/ny/">Service Areas</a></p>
            <p>&copy; 2024 Miele Appliance Repair Westchester. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>'''

# Create town pages
for slug, name in towns:
    town_dir = f"ny/{slug}"
    os.makedirs(town_dir, exist_ok=True)

    page_content = template.format(town_name=name, town_slug=slug)

    with open(f"{town_dir}/index.html", "w") as f:
        f.write(page_content)

    print(f"Created: {town_dir}/index.html")

# Create NY index page (list of all towns)
ny_index = '''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Miele Appliance Repair Westchester County NY | All Service Areas</title>
    <meta name="description" content="Miele appliance repair services throughout Westchester County, NY. Same-day service in Yonkers, White Plains, New Rochelle, Scarsdale, and all towns.">
    <link rel="canonical" href="https://miele-westchester.pages.dev/ny/">
    <link rel="icon" type="image/png" href="/favicon.png">
    <style>
        :root { --blue: #003087; --red: #e41e26; --gray: #f8f9fa; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; color: #333; background: #fff; line-height: 1.6; }
        h1, h2 { font-weight: 700; color: var(--blue); }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
        header { background: var(--blue); color: white; padding: 20px 0; position: fixed; width: 100%; top: 0; z-index: 1000; }
        .nav-wrapper { display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 1.5rem; font-weight: 700; color: white; text-decoration: none; }
        .cta-btn { background: var(--red); color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: 600; }
        .hero { background: linear-gradient(135deg, var(--blue) 0%, #001a4d 100%); color: white; padding: 140px 0 80px; text-align: center; }
        .hero h1 { font-size: 2.5rem; margin-bottom: 20px; }
        .towns { padding: 80px 0; }
        .towns h2 { text-align: center; margin-bottom: 50px; }
        .towns-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }
        .town-link { display: block; background: var(--gray); padding: 20px; border-radius: 8px; text-decoration: none; color: var(--blue); font-weight: 600; text-align: center; transition: all 0.3s; }
        .town-link:hover { background: var(--blue); color: white; }
        footer { background: #001a4d; color: white; padding: 40px 0; text-align: center; }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <nav class="nav-wrapper">
                <a href="/" class="logo">Miele Repair Westchester</a>
                <a href="/#contact" class="cta-btn">Get Free Estimate</a>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <h1>Miele Appliance Repair Service Areas</h1>
            <p>Serving all of Westchester County, NY</p>
        </div>
    </section>

    <section class="towns">
        <div class="container">
            <h2>Select Your Town</h2>
            <div class="towns-grid">
'''

for slug, name in sorted(towns, key=lambda x: x[1]):
    ny_index += f'                <a href="/ny/{slug}/" class="town-link">{name}</a>\n'

ny_index += '''            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Miele Appliance Repair Westchester. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>'''

with open("ny/index.html", "w") as f:
    f.write(ny_index)

print("Created: ny/index.html")
print(f"\nTotal pages created: {len(towns) + 1}")
