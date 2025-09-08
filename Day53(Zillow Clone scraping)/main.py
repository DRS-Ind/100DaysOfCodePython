from webscraper import WebScraper
from google_form_manager import GFormManager


if __name__ == '__main__':
    scraper = WebScraper()
    g_form_manager = GFormManager()

    hrefs, prices, addresses = scraper.get_links_prices_addresses()

    for addresse in addresses:
        print(addresse)

    # g_form_manager.send_info(hrefs=hrefs, prices=prices, addresses=addresses)
