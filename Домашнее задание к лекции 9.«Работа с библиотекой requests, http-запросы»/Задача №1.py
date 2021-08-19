import requests

def calculations(heroes_list):
    max_intelligence = 0
    max_id = 99
    for id, heroe in enumerate(heroes_list):
        heroe_for_calc = requests.get(f"https://www.superheroapi.com/api.php/2619421814940190/search/{heroe}").json()['results']
        for results in heroe_for_calc:
            heroes_powerstats = requests.get(f"https://www.superheroapi.com/api.php/2619421814940190/{results['id']}/powerstats").json()
            intelligence = int(heroes_powerstats['intelligence'])
            if intelligence > max_intelligence:
                max_intelligence = intelligence
                max_id = id
    coolest = heroes_list[max_id]
    print(coolest)

if __name__ ==  '__main__':
    calculations(["Thanos","Captain%20America","Hulk"])