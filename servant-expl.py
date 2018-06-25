import requests
from bs4 import BeautifulSoup

url = ''

print('''1 - Abrir tier list de 5 estrelas.
2 - Abrir tier list de 4 estrelas.
3 - Abrir tier list de 1-3 estrelas
Digite qualquer outra tecla pra sair.''')

op = input()
if op == '1':
    url = 'https://grandorder.gamepress.gg/5-star-tier-list'
elif op == '2':
    url = 'https://grandorder.gamepress.gg/4-star-tier-list'
elif op == '3':
    url = 'https://grandorder.gamepress.gg/13-star-tier-list'

nome = input('Digite o nome do servo: ')

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser') #Verificar outras alternativas depois
a = soup.find_all('div') #ir no site e inspecionar depois de selecionar o que vai ser clicado/analisado
for i in a:
    n = i.get('class') #geralmente a classe vai ser o parâmetro de pesquisa no código fonte do site
    if n != None:
        if 'show-expl' in n: # show-expl é o elemento que aparece em tod botao de expllicacao de servo
            servo = i.get('id')
            if servo == nome:
                dado = i.get('data-content')
                #dado = dado.replace(dado[5],dado[5] + '\n')
                print(dado)
