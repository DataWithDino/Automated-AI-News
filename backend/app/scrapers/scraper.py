from urllib.parse import urljoin
from app.utils.web_scraper import fetch_page, parse_html

def run_scraper():
    url = 'https://machinelearning.apple.com/research/introducing-apple-foundation-models'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    # Step 1: Fetch the page
    html_content = fetch_page(url, headers=headers)
    if not html_content:
        print("Failed to retrieve the web page.")
        return

    # Step 2: Parse the HTML
    soup = parse_html(html_content)

    # Step 3: Attempt to find the main content area using different selectors
    main_content = soup.find('article')  # Try finding an <article> tag
    if not main_content:
        print("No <article> tag found, trying a <div> with a specific class...")
        main_content = soup.find('div', class_='content')  # Adjust the class name based on inspection
    if not main_content:
        print("No <div class='content'> found, trying a fallback...")
        main_content = soup.find('body')  # Fallback to <body> if nothing else works

    if not main_content:
        print("Failed to find the main content area.")
        return

    # Step 4: Iterate over the children of the main content
    for element in main_content.descendants:
        if element.name == 'p':
            print(f"Paragraph: {element.get_text()}")
        elif element.name == 'img':
            img_url = element.get('src')
            if img_url:
                full_img_url = urljoin(url, img_url)
                print(f"Image URL: {full_img_url}")

if __name__ == "__main__":
    run_scraper()


