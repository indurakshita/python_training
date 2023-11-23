import requests
from bs4 import BeautifulSoup
import csv

# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
# print(r.url)
# print(r.status_code)
# soup = BeautifulSoup(r.content,'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
'find paragraph'
'logic 1'
# for paragraph in soup.find_all('p'):
#     print(paragraph.string)
#     print(paragraph.text)
'logic 2'
# body = soup.body
# for paragraph in body.find_all('p'):
#     print(paragraph.text)

"find href"
'logic 1'
# nav = soup.nav
# for url in nav.find_all('a'):
#     print(url.get('href'))
'logic 1'
# for url in soup.find_all('a'):
#     print(url.get('href'))

"find div"
# for div in soup.find_all('div', class_='body'):
#     print(div.text)

"find table"
# table = soup.find('table')
# print(table)
'find row and column'
# table_rows = table.find_all('tr')
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)

"get the images"

# images_list = [] 
  
# images = soup.select('img') 

# for image in images: 
    
#     src = image.get('src') 
#     alt = image.get('alt') 
#     images_list.append({"src": src, "alt": alt}) 
    
      
# for image in images_list: 
#     print(image)

