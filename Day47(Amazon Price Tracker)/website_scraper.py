import requests
from bs4 import BeautifulSoup


class WebsiteScraper:
    def __init__(self) -> None:
        """
        The class is responsible for parsing the site.
        """
        self.url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
        self.headers = {
            "Accept-Language": "ua-UA,ua;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/139.0.0.0 Safari/537.36"
        }
        self.soup = self._prepare_soup()

    def _prepare_soup(self) -> BeautifulSoup:
        """
        The function prepares the site for parsing.

        :return: BeautifulSoup type
        """
        content = requests.get(url=self.url, headers=self.headers).text
        return BeautifulSoup(markup=content, features="html.parser")

    def get_full_price(self) -> float:
        """
        The function gets the product price from the site.

        :return: float product price
        """
        decimal_part = self.soup.find(name="span", class_="a-price-whole").get_text()
        fraction_part = self.soup.find(name="span", class_="a-price-fraction").get_text()
        return float("".join([decimal_part, fraction_part]))
