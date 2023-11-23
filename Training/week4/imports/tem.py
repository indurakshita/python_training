import requests
import json
from bs4 import BeautifulSoup as bs

'''find the place names using web scrabing'''


class WebScrabing:
    def __init__(self):
        
        self.response  = None
        self.soup = None
        self.place_name = []
        self.images = []
        self.place_image = {}

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

    def get_place(self):
        tem1_place_img = {}
       
        try:

            if self.soup:
                divs= self.soup.find('div', class_="dropcaps") 
                if divs:
       
                    for div in divs.find_all('h3'):
                        tem1_place =div.find_next('b').text.strip()
                        if '.' in tem1_place:
                            print(tem1_place)
                    #     tem1_place_img[.split('.').text] = div.find('img')
                    # print(tem1_place_img)

            #         for index, place in enumerate(places[:50], start=1):
            #             place_name = place.get_text(strip=True)
            #             img = place.find('img')
            #             img_url = img['src'] if img and 'src' in img.attrs else 'Image not found'

            #             print(f"{place_name} - {img_url}")
            #     else:
            #         print("Place container not found on the webpage.")
            # else:
            #     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
                
                     
            #     for div in divs.find_all('h3'):
            #         b_element = div.find_next('b')
            #         img_element = div.find_next('img')
                    
            #         if b_element is not None and img_element is not None:
            #             place = b_element.text.strip()
            #             img_url = img_element.get('src')  # Assuming 'src' attribute contains the image URL
                        
            #             print(f"{place} - {img_url}")
            #         else:
            #             # Handle the case where either <b> or <img> element is not found
            #             print("One or more elements not found.")

                    # places = div.find_next('b').text.strip()
                    # self.place_name.append(places)
                    # images=div.find_next('img').parent
                    
                        
                
                # if self.place_name and self.images:
                #     for place, image in zip(self.place_name, self.images):
                #         self.place_image[place] = image
                #     # print(self.place_image)

              
        except Exception as e:
            print(e)

    
    # def dict_place_img(self):
    #     if self.places and self.images:
    #         for place, image in zip(self.places, self.images):
                 
    #                 self.place_image[place] = image  
    #         print(self.place_image)

                        
                    
            
            # print(self.place_image)
            # return self.place_image

    def dump_json(self):
        
        with open("place_image.json",'w') as f:

            json.dump(self.place_image,f)


web = WebScrabing()
web.save_html()
web.get_html
web.get_place()
# web.get_image()

# web.dict_place_img()
# # web.dump_json()

