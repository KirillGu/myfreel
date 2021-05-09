import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/List_of_schools_in_the_Auckland_Region'

wiki = requests.get(URL)

soup = BeautifulSoup(wiki.text, 'html.parser')


in_soup = soup.find_all('a', class_='external text')
for ite in in_soup:
    info = ite.get('href')
    #print(info)
    req = requests.get(info)

    sou = BeautifulSoup(req.text, 'html.parser')
    #get info
    sou_principal = sou.find('span', id='schoolPrincipal')
    sou_name = sou.find('h1', class_='visually-hidden')
    sou_tel = sou.find('span', id='schoolPhone')
    sou_web = sou.find('span', id='schoolWebsite')
    for web in sou_web:
        web_site = web.get('href')
    #print(sou_tel.text)
    #print(sou_name.text)
    #print(sou_principal.text)
    #print(web_site)
    text = (' Name: {0} ----> Principal: {1} ----> Tel: {2} ----> {3} '.format(sou_name.text, sou_principal.text, sou_tel.text, web_site))
    with open('info_sch.txt', 'a') as file:
        file.write(text + '\n')

print('Complite')
