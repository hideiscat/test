import csv

import requests
from bs4 import BeautifulSoup

HEADER = ['title', 'txt', 'cast'] 

url = 'https://eiga.com/now/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
movies = soup.find_all('section')

with open('movies.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for movie in movies:
        textBox = movie.find('div', class_='list-block list-block2')

        title = textBox.find('h2', class_='title').text
        txt = textBox.find('p', class_='txt').text
        cast = textBox.find('ul', class_='cast-staff').text

        print(title)
        print(txt)
        print(cast)
        
        row = [title, txt, cast]
        writer.writerow(row)