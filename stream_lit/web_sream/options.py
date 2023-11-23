
def language_mapping(language):
    if language:
        lang = {
            ("english","englis","inglish","inglis",'en'): "en",
            ("tamil","thamil",'ta') : "ta"
        }
        for l in lang:
            
            if language.casefold() in l:
                language = lang[l]
                break

    language = language or 'en'
    return language

def country_mapping(country):
    if country:
        coun = {
            ("india","bharath","barath",'in'): "in",
            ("america","usa",'united states',"united states of america",'us') : "us"
        }
        for c in coun:
            if country.casefold() in c:
                country = coun[c]
                break

    country = country or 'in'
    return country

# def query_mapping(query):
    
#     if query:
#         l_query = ["pizza",'pasta','history']
#         for q in l_query:
#             if query.casefold() in q:
#                 query = q
#     return query 
            
                

