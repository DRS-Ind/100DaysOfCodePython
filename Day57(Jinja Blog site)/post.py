import requests


class Post:
    def __init__(self) -> None:
        self.url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.all_posts = self.get_all_posts()

    def get_all_posts(self) -> list:
        response = requests.get(url=self.url).json()
        return response

    def get_post(self, post_id: int) -> dict:
        return self.all_posts[post_id - 1]
