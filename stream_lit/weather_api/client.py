import requests
from mapping import Current,Location
from pprint import pprint
def get_response(place):
    
	url = "https://weatherapi-com.p.rapidapi.com/current.json"
	place = place or "coimbatore"
	querystring = {'q':place}

	headers = {
		"X-RapidAPI-Key": "a37bd030e7msh91a64a815db01f8p1e46b3jsn13c4aec2e158",
		"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	if response.status_code != 200:
		return 
	# pprint(response.json())
	if (response.json()):
		location = response.json()['location']
		
		current = response.json()['current']
		current= Current(**current,location=Location(**location))
		
		return current

		
		
	

