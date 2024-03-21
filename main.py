import requests
from bs4 import BeautifulSoup
import pandas

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇
request = requests.get(URL)
content = request.text

soup = BeautifulSoup(content, "html.parser")
#print(soup)
all_movies = soup.find_all(name="h3", class_="title")
titles = [i.getText() for i in all_movies]
ordered_title = titles[::-1]



with open("saved_data.txt", "w", encoding="utf-8") as data_file:
    for i in ordered_title:
        data_file.write(f"{i }\n")






