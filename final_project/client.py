import requests
from bs4 import BeautifulSoup as bs
from alive_progress import alive_it


class BooksUrlList:
    def __init__(self,baseurl):
        self.baseurl = baseurl
         
        self.page_links = []
        self.book_link = []

    def get_page_url(self):  
        try:
            response = requests.get(self.baseurl)
            if response.status_code == 200:
                soup = bs(response.text,"html.parser")
                pages=soup.find("ul",class_="pager")   
                if pages:
                    single_page_link = pages.find('li', class_='next').find('a').get('href') 
                    url_first_part, url_sec_part = single_page_link.split('-')            
                self.page_links=[f"{self.baseurl}{url_first_part}-{new_page_number}.{url_sec_part.split('.')[-1]}"for new_page_number in alive_it(range(1,51))]
                return self.page_links
        except Exception as e:
            print(f"Error is:{e}")
                     
    def get_books_url(self): 
        pages= self.page_links
        try:
            for page in alive_it(pages):     
                page_response = requests.get(page)
                soup =bs(page_response.text,'html.parser') 
                if soup:
                    divs=soup.findAll("div", class_="image_container") 
                    for div in divs:
                        temp_book_link = div.find("a").get("href")
                        bk_link = f"{self.baseurl}catalogue/"+temp_book_link 
                        if bk_link:
                            self.book_link.append(bk_link)    
                                    
            return (self.book_link)
        except Exception as e:
            print(f"Error is:{e}")
    
bookurl=BooksUrlList(baseurl="https://books.toscrape.com/")
bookurl.get_page_url()
booklink= bookurl.get_books_url()

    
    



