import requests
import json
from mapping import Article
from options import language_mapping,country_mapping

def get_response(q=None,country=None,language=None):
    language = language_mapping(language)
    country = country_mapping(country)
    # q = query_mapping(q)

    response = requests.get(f"https://newsdata.io/api/1/news?apikey=pub_31338ad3686c1bddb35f5255be5a3af31049b&q={q}&country={country}&language={language}")
    print(response.url)
    if response.status_code != 200:
        return 
    return [Article(**response) for response in response.json()["results"]]
   

    # responses = []
    # for response in response.json()["results"]:
    #     responses.append(Article(**response))
    
    # return responses
  
        
    
        
