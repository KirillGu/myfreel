import requests
from bs4 import BeautifulSoup
import pandas

#URL = f'https://search.naver.com/search.naver?where=news&query={item}&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall'

top_comp = pandas.read_excel('Listofcompany.xlsx', )
#print(top_players)
tc = top_comp['Name'].tolist()
#comp_csv = top_comp.to_csv(index=False)
#print(tc)
itemm = []
datee = []
newspaperr = []
title_of_newss = []
linkk = []
summaryy = []

for item in tc:
    #print(item)
    comp_url = requests.get(f'https://search.naver.com/search.naver?where=news&query={item}&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall')
    soup = BeautifulSoup(comp_url.text, 'html.parser')
    in_soup = soup.find('div', class_='info_group').find('a')
    date_soup = soup.find('span', class_='info')
    title_soup = soup.find('a', class_='news_tit')
    summ_soup = soup.find('div', class_='news_dsc')
    link_soup = soup.find('div', class_='group_news').find('ul').find('li').find('div').find('a')



    ds = date_soup.text
    il = in_soup.text
    ts = title_soup.text
    ss = summ_soup.text
    l_s = (link_soup.get('data-url'))

    itemm.append(item)
    datee.append(ds)
    newspaperr.append(il)
    title_of_newss.append(ts)
    linkk.append(l_s)
    summaryy.append(ss)




df = pandas.DataFrame({
'Item': itemm,
'Date': datee,
'Newspaper': newspaperr,
'Title of news': title_of_newss,
'Link': linkk,
'Summary': summaryy


})

df.to_excel('News.xlsx')

print('Complite')
