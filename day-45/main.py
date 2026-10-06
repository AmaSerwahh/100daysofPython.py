from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

response = requests.get(
    'https://www.empireonline.com/movies/features/best-teen-movies/',
    headers=headers
)

soup = BeautifulSoup(response.text, 'html.parser')

movie_list = []
all_movies = soup.find_all('h3 strong')
for movie in all_movies:
    movie_title = movie.text
    movie_list.append(movie_title)

print(movie_list)
movies = movie_list[::-1]

with open('movies.txt', 'a') as data:
    for movie in movies:
        data.write(movie + '\n')

