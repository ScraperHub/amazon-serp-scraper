from crawlbase import CrawlingAPI
import pandas as pd
import json

# Initialize the Crawling API with your Crawlbase token
api = CrawlingAPI({ 'token': 'CRAWLBASE_JS_TOKEN' })

# URL of the Amazon search page you want to scrape
amazon_search_url = 'https://www.amazon.com/s?k=games'

# options for Crawling API
options = {
 'scraper': 'amazon-serp'
}

# List to store the scraped product information
product_data = []

def scrape_url(url):
    # Make a request to scrape the Amazon search page with options
    response = api.get(url, options)

    # Check if the request was successful
    if response['status_code'] == 200:
        # Loading JSON from response body after decoding byte data
        response_json = json.loads(response['body'].decode('latin1'))

        # Getting Scraper Results
        scraper_result = response_json['body']

        # Extracting Products from the JSON response
        products = scraper_result.get("products", [])

        for product in products:
            product_info = {
                "url": product.get("url", ""),
                "name": product.get("name", ""),
                "asin": product.get("asin", ""),
                "image": product.get("image", ""),
                "price": product.get("price", ""),
                "isPrime": product.get("isPrime", ""),
                "offer": product.get("offer", ""),
                "customerReview": product.get("customerReview", ""),
                "customerReviewCount": product.get("customerReviewCount", ""),
            }
            product_data.append(product_info)

        # Extract pagination information and return it
        pagination = scraper_result.get("pagination")
        return pagination

    else:
        print("Failed to retrieve the page. Status code:", response['status_code'])
        return None

# Scrape the initial page and get pagination information
pagination_info = scrape_url(amazon_search_url)

# Check if pagination information is available
if pagination_info:
    total_pages = pagination_info.get('totalPages', 1)

    # Start from page 2 since the first page is already scraped
    for page_number in range(2, total_pages + 1):
        page_url = f'{amazon_search_url}&page={page_number}'
        scrape_url(page_url)

# Create a Pandas DataFrame from the extracted data
df = pd.DataFrame(product_data)

# Save the DataFrame to a CSV file
df.to_csv("amazon_products.csv", index=False)