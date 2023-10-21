import requests

def get_random_anime_quote():
    url = "https://animechan.xyz/api/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

quote_data = get_random_anime_quote()



