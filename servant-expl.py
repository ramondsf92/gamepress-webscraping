import requests
from bs4 import BeautifulSoup

nome = input()
url = 'https://grandorder.gamepress.gg/5-star-tier-list'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser') #Verify other alternatives later
a = soup.find_all('div') #Go to website and inspect after selecting what will be clicked/analized
for i in a:
    n = i.get('class') #class will be the main search parameter in source code
    if n != None:
        if 'show-expl' in n: # show-expl is the class name that appears at all div we need
            servo = i.get('id')
            if servo == nome:
                dado = i.get('data-content')
                print(dado)
