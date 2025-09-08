import requests
import re
from bs4 import BeautifulSoup

def clean_price(price: str) -> str:
    """
    Function for cleaning a string with a price.

    :param price: unformatted price with additives
    :return: only the price with a dollar sign
    """
    return (price.replace('+ 1 bd', '')
            .replace('1bd', '')
            .replace('+', '')
            .replace('/mo', '')
            .replace(' ', '')
            .strip())


class WebScraper:
    def __init__(self) -> None:
        """
        The class scraps the Zillow clone website.
        """
        self.url ="https://appbrewery.github.io/Zillow-Clone/"

    def get_links_prices_addresses(self) -> tuple[list, list, list]:
        """
        The function gets apartments` links, prices, and addresses.

        :return: lists with web links, prices, and addresses
        """
        content = requests.get(url=self.url).text
        soup = BeautifulSoup(markup=content, features="html.parser")

        links = [href["href"] for href in soup.select("a.StyledPropertyCardDataArea-anchor")]
        prices = [clean_price(price.string) for price in soup.select("span.PropertyCardWrapper__StyledPriceLine")]
        addresses = [address.string.strip() for address in soup.select("address")]

        return links, prices, addresses
