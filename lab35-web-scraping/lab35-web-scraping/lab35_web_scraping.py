#!/usr/bin/env python3
# Lab 35: Basic Web Scraping for ML Data
# Author: Auto-generated for educational use

from bs4 import BeautifulSoup
import requests

print("\n--- Task 1: Install and Verify Libraries ---")
print("Libraries imported successfully!")

print("\n--- Task 2: Scrape Sample Data from a Webpage ---")
url = "https://quotes.toscrape.com"
response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the webpage content!")
else:
    print("Failed to fetch the webpage content.")

print("\nPreview of HTML content:\n")
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify()[:500])

print("\n--- Task 3: Parse and Clean the Scraped Data ---")

# Extract quotes, authors, and tags
quotes = [quote.get_text().strip() for quote in soup.find_all("span", class_="text")]
authors = [author.get_text().strip() for author in soup.find_all("small", class_="author")]
tags = [tag.find_all("a", class_="tag") for tag in soup.find_all("div", class_="tags")]

print("\nExtracted Quotes:")
for quote in quotes[:3]:
    print(f"- {quote}")

print("\nExtracted Authors:")
for author in authors[:3]:
    print(f"- {author}")

print("\nExtracted Tags for First 3 Quotes:")
for taglist in tags[:3]:
    print("-", [t.get_text() for t in taglist])

print("\n--- Cleaned Data Summary ---")
print(f"Total Quotes: {len(quotes)}")
print(f"Sample Cleaned Quote: {quotes[0]}")
print(f"Corresponding Author: {authors[0]}")

print("\n--- Lab 35 Completed Successfully ---")
print("You have scraped, parsed, and cleaned data (quotes, authors, tags) for ML use.")