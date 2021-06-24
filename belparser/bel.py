import pandas
from bs4 import BeautifulSoup as Soup
import requests



start_url = 'https://www.infobel.com/en/belgium'
res = requests.get(start_url)
sou = Soup(res.content, 'html.parser')
name_cat = sou.find_all('span', class_='list-item-text')

category = []
hrefs_business = []
name_business = []
adress_business = []
mobile_tel = []
telephone_business = []
email_business = []
website = []
fax = []
a = 0
sif = 0
for nc in name_cat:
    info_nc = nc.text
    a += 1
    #print(info_nc) # Категория
    print(a)
    fin = info_nc.replace(' ', '')
    fin = fin.replace('&', '_').lower()
    print(fin)

    site_url = f'https://www.infobel.com/en/belgium/business/{a}0000/{fin}/'
    for num_page in range (1, 51):

        response = requests.get(site_url + str(num_page))
        soup = Soup(response.content, 'html.parser')

        link = soup.find_all('a', class_='btn primary-button pull-right')
        for links in link:
            text_web = []
            info = links.get('href')
            #print(info)
            href_business = 'https://www.infobel.com' + info # ссылка бизнесов
            res_busi = requests.get(href_business)
            soup_busi = Soup(res_busi.content, 'html.parser')
            name_busi = soup_busi.find('h2', class_='customer-item-name') # Название бизнеса
            adre_busin = soup_busi.find('span', class_='customer-info-detail highlighted address') #Adress
            all_info = soup_busi.find_all('span', class_='customer-info-detail')
            #mob_tel = soup_busi.find('div', id='phones-region_BE100131178') #mobtel
            ema_inf = soup_busi.find('a', id='source-email_BE100131178') #email
            fax_tel_mob = soup_busi.find('div', id='phones-region_BE100656159').find_all(class_='detail-text') #fax.tel.mobtel
            tfm = []
            if len(fax_tel_mob) == 1:
                for n in fax_tel_mob:
                    tfm.append(n.text)
                tlf.append('none')
                tlf.append('none')
                mobile_tel.append(tfm[0])
                telephone_business.append(tfm[1])
                fax.append(tfm[2])
            elif len(fax_tel_mob) == 2:
                for n in fax_tel_mob:
                    tlf.append(n.text)
                tlf.append('none')
                mobile_tel.append(tfm[0])
                telephone_business.append(tfm)[1]
                fax.append(tfm[2])
            else:
                for n in fax_tel_mob:
                    tlf.append(n.text)
                mobile_tel.append(tfm[0])
                telephone_business.append(tfm)[1]
                fax.append(tfm[2])


            web_busi = soup_busi.find('a', rel='noopener external')
            web = web_busi.get('href') # веб сайт
            category.append(info_nc)
            hrefs_business.append(href_business)
            name_business.append(name_busi.text)
            adress_business.append(adre_busin.text)
            email_business.append(ema_inf.text)
            website.append(web)


df = pandas.DataFrame({
'Link': hrefs_business,
'Category': category,
'Company': name_business,
'Street': adress_business,
'Mobile': mobile_tel,
'Telephone': telephone_business,
'Fax': fax,
'Email': email_business,
'Website': website


})

df.to_excel('busbel.xlsx')

print('Complite')
