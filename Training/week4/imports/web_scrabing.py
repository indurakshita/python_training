import requests,openpyxl
import json
from bs4 import BeautifulSoup as bs

'''find the place names using web scrabing'''


class WebScrabing:
    def __init__(self):
        
        self.response  = None
        self.soup = None
        self.tem_place = []
        self.tem1_img = []
        self.tem2_img = []
        self.place_image = []
    def excel_file(self):
        self.excel = openpyxl.Workbook()
        self.sheet = self.excel.active
        self.sheet.title = "Top 50 places in India"
        self.sheet.append(["place","images"])

    def save_html(self):
        self.response = requests.get("https://www.indiantravelstore.com/blog/places-to-visit-in-india-before-you-turn-40")
        if self.response.status_code == 200:
            
            with open("places.html",'w') as f:
                
                f.write(self.response.text)
        else:
            return None
    @property    
    def get_html(self):
        try:
            with open("places.html",'r') as f:
                html = f.read()  
                self.soup =bs(html,"html.parser") 
                return self.soup 
        except Exception as e:
            print(e)

    def tem_place_image(self): 
        try:
            if self.soup:
                divs = self.soup.find("div",class_="dropcaps")
                for div in divs.find_all('h3'):
                    self.tem1_img.append(str(tem1))
                    
                
                for div in divs.find_all('h3'):
                    place = div.find_next("b").text
                    self.tem_place.append(place)
                    tem2 = div.find('img')
                    self.tem2_img.append(str(tem2))
                
                
                self.place_image= {place:(img1,img2)for place,img1,img2 in zip(self.tem_place,self.tem1_img,self.tem2_img)}
                return self.place_image
                # for k,v in self.place_image.items():
                #     self.sheet.append(['k','v'])  
                    
                #     v1 =list(v)     
                #     for i in v1:
                #         if i == 'None':
                #             v1.remove(i)
                #             v=tuple(v1)
                            
                #             self.place_image[place]=v
                #     self.place_image
                return self.place_image
        except Exception as e:
            print(e)
        if self.excel_file():
            try:
                self.excel.save("top places")
            except Exception as e:
                print(e)
        
    
    def dump_json(self):
        try:
            with open("place_image.json",'w')as f:
                json.dump(self.place_image,f)
        except Exception as e:
            print(f"Error : {e}")



web = WebScrabing()
web.excel_file() 
web.save_html()
web.get_html
web.tem_place_image()
web.dump_json()



