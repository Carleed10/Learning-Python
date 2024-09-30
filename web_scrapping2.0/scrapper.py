import requests
from bs4 import BeautifulSoup


try:
    response = requests.get('https://trello.com/')
except requests.exceptions.RequestException as e:
    print("An error occured ", e)
else:
    if response.status_code == 200:
        print(response.content)
        with open("trello-landing-page.html", "w") as f:
            # print(type(response.content))
            soup = BeautifulSoup(response.content, 'html.parser')
            f.write(soup.prettify())