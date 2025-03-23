# amazon-serp-scraper

## Description

This repository contains a Python-based scraper for extracting product listings from Amazon search pages. The scraper utilizes the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) with the Amazon SERP scraper to efficiently extract structured product data while bypassing Amazon’s anti-bot measures.

The scraper also handles button-based pagination, ensuring complete data extraction across multiple search result pages.

➡ Read the full blog [here](https://crawlbase.com/blog/scrape-amazon-search-pages-with-crawling-api/) to learn more.

## Scraper Overview

### Amazon Search Page Scraper

The `amazon_search_scraper.py` extracts the following details from Amazon search results:

- **Product Title**
- **ASIN (Amazon Standard Identification Number)**
- **Price**
- **Prime Availability**
- **Offer Details**
- **Customer Review Rating**
- **Number of Reviews**
- **Product Image URL**
- **Product Page Link**

**Note**: The Amazon SERP scraper provides many other values that you may need. See the full response of the scraper [here](https://crawlbase.com/docs/crawling-api/scrapers/#amazon-serp) to learn more.

The scraper automatically handles pagination using the Crawlbase Crawling API, ensuring a comprehensive dataset is collected.

## Environment Setup

Ensure Python is installed on your system. Check the version using:

```bash
python --version
```

Install the required dependencies:

```bash
pip install crawlbase pandas
```

- **Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
- **Pandas** – Used for storing and exporting the scraped data.

## Running the Scraper

### 1. Get Your Crawlbase Access Token

- Sign up on [Crawlbase](https://crawlbase.com/signup) to get an API token.
- This token is required to access the Crawling API for bypassing bot protection.

### 2. Update the Scraper with Your Token

Replace "`CRAWLBASE_JS_TOKEN`" in the script with your Crawlbase Crawling API Token.

### 3. Run the Scraper

```bash
python amazon_search_scraper.py
```

The extracted Amazon product listings will be saved in a CSV file named **amazon_products.csv**.
