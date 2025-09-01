from mail_manager import MailManager
from website_scraper import WebsiteScraper


if __name__ == '__main__':
    # initialize managers
    scraper = WebsiteScraper()
    mail_manager = MailManager()

    # get product price from the site and form a message text
    product_price = scraper.get_full_price()
    mail_text = f"New price for the product you search, only {product_price}."

    # send message
    mail_manager.send_message(message_body=mail_text)
