import requests

from bs4 import BeautifulSoup

response = requests.get('https://www.netwr3r4flix.com/')

if response.status_code == 200:
    with open("netflix.html", "w", encoding="utf-8") as f:
        soup = BeautifulSoup(response.content, 'html.parser')
        f.write(soup.prettify())
        print(soup.find_all("h1"))
else:

    print("an error occured", response.status_code)