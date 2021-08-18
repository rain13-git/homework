import requests

url_hulk = "https://superheroapi.com/api/2619421814940190/search/Hulk"
Hulk = requests.get(url_hulk)
Hulk = Hulk.json()

url_thanos = "https://superheroapi.com/api/2619421814940190/search/Thanos"
Thanos = requests.get(url_thanos)
Thanos = Thanos.json()

url_cap_am = "https://www.superheroapi.com/api.php/2619421814940190/search/Captain%20America"
Cap_am = requests.get(url_cap_am)
Cap_am = Cap_am.json()

#c = character
def calculations():
    Hulk_url = "https://www.superheroapi.com/api.php/2619421814940190/332/powerstats"
    Hulk = requests.get(Hulk_url).json()

    Cap_am_url = "https://www.superheroapi.com/api.php/2619421814940190/149/powerstats"
    Cap_am = requests.get(Cap_am_url).json()

    Thanos_ulr = "https://www.superheroapi.com/api.php/2619421814940190/655/powerstats"
    Thanos = requests.get(Thanos_ulr).json()

    if Hulk['intelligence'] > Cap_am['intelligence'] > Thanos['intelligence']:
        print('Cамый умный - Thanos')
    elif Hulk['intelligence'] > Thanos['intelligence'] > Cap_am['intelligence']:
        print('Cамый умный - Thanos')
    elif Cap_am['intelligence'] > Hulk['intelligence'] > Thanos['intelligence']:
        print('Cамый умный - Captain America')
    elif Cap_am['intelligence'] > Thanos['intelligence'] > Hulk['intelligence']:
        print('Cамый умный - Captain America')
    elif Thanos['intelligence'] > Cap_am['intelligence'] > Hulk['intelligence']:
        print('Cамый умный - Hulk')
    elif Thanos['intelligence'] > Hulk['intelligence'] > Cap_am['intelligence']:
        print('Cамый умный - Hulk')

if __name__ ==  '__main__':
    calculations()