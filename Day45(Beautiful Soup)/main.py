import requests
from bs4 import BeautifulSoup

# initialise main variables
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
content = requests.get(url=URL).text
soup = BeautifulSoup(markup=content, features="html.parser")

# parse through the site and collect all h3 with "title" class and reverse list
titles = [title.string for title in soup.select("h3.title")][::-1]

# write all information to the file movies.txt
with open("movies.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(titles))
