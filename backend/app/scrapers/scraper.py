from app.utils.web_scraper import fetch_page, parse_html, extract_data

def run_scraper():
    #url = 'https://example.com'  # Replace with the URL of the site you want to scrape
    url = 'https://blogs.nvidia.com/blog/category/generative-ai/'  # Replace with the URL of the site you want to scrape
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; ExampleBot/1.0)'}

    # Step 1: Fetch the page
    html_content = fetch_page(url, headers=headers)
    if not html_content:
        print("Failed to retrieve the web page.")
        return

    # Step 2: Parse the HTML
    soup = parse_html(html_content)

    # Step 3: Extract data using CSS selectors
    # Example: Extract all paragraphs <p> from the page
    paragraphs = extract_data(soup, 'p')

    # Step 4: Process and print the extracted data
    for i, paragraph in enumerate(paragraphs, start=1):
        print(f"Paragraph {i}: {paragraph.get_text()}")

if __name__ == "__main__":
    run_scraper()
