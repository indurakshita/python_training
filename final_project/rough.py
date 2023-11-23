from client import booklink
from bs4 import BeautifulSoup
from pydantic import BaseModel,Field

from alive_progress import alive_it
import requests
import json



class BookDetails:
    
    def __init__(self, book_links):
        self.book_links = book_links
        self.product_details = []

    def get_book_details(self):
        for link in alive_it(self.book_links):
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')
            divs = soup.find("div", class_="content")
            if not divs:
                continue
            #image  
            image = divs.find('img')['src'].replace("../../", "https://books.toscrape.com/")

            #bookname
            book_name = divs.find('img')['alt']

            #price
            temp = divs.find('div', class_="col-sm-6 product_main")
            temp_price = temp.select_one("p", class_="price_color").text
            price = temp_price.replace("Â£", "$")

            #rating
            p = temp.find('p', class_="star-rating")
            rating = p['class'][1] if "class" in p.attrs else None

            #Book description
            des = divs.find('div', id="product_description", class_="sub-header")
            if des:
                description_paragraph = des.find_next('p')
                if description_paragraph:
                    pro_description = description_paragraph.text.removesuffix("...more")
                else:
                    pro_description = "Description paragraph not found"
            else:
                pro_description = "Description element not found"

            # print(f"i-{image},name-{book_name},price-{price},rating-{rating},descrip-{pro_description}")
            # Book information   
            product_information = {}
            books ={}
            tables = divs.find('table', class_="table table-striped").find_all('tr')
            for table in tables:
                tab_head = table.find('th').text
                tab_data = table.find('td').text
                if "Price" in tab_head:
                    tab_data = tab_data.replace('Â£', '$')
                elif "Tax" in tab_head:
                    tab_data = tab_data.replace('Â£', '$')
                product_information[tab_head] = tab_data
            books ={        "book_id":len(books)+1,
                            "name":book_name,
                            "image":image,
                            "pric":price,
                            "rating":rating,
                            "pro_description":pro_description,
                            "product_information":product_information
                    }
            self.product_details.append(books)   
        return self.product_details

    def save_to_json(self, filename):
        with open(filename, "w") as f:
            json.dump(self.product_details, f, indent=4)

if __name__ == "__main__":
    bookdetail = BookDetails(book_links=booklink)
    bookdetail.get_book_details()
    bookdetail.save_to_json("books_detail.json")
