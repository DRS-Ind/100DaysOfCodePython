import requests
from bs4 import BeautifulSoup


class BillboardParser:
    def __init__(self, year: str) -> None:
        """
        The manager parses the Billboard site to find and collect the Hot 100 songs in a certain year.

        :param year: searched year
        """
        self.year = year
        self.url = "/".join(["https://www.billboard.com/charts/hot-100", self.year])
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                          "like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }

    def parse_site(self) -> list:
        """
        The function parses the site and gets all song names.

        :return: list with song names
        """
        content = requests.get(url=self.url, headers=self.header).text
        soup = BeautifulSoup(markup=content, features="html.parser")
        attributes = {
                "id": "title-of-a-story",
                "class": "c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 "
                         "lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 "
                         "u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 "
                         "lrv-u-margin-b-00@mobile-max"
            }
        result = [title.string[14:-5] for title in soup.find_all(name="h3", attrs=attributes)]
        return result
