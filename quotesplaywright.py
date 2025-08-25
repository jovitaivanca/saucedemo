
from playwright.sync_api import sync_playwright
import pandas as pd


def scrape_quotes():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)  
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/")
        quotes_data = []

        quotes = page.locator('.text').all_text_contents()
        for quote in quotes:
            quotes_data.append(quote)

        browser.close()

        return quotes_data

if __name__ == "__main__":
    scrape_quotes()


def estrak_quotes():
    df = pd.DataFrame(scrape_quotes())
    print(df)
    df.to_excel('quotesplaywright.xlsx', index=False)
estrak_quotes()
