import requests
from pprint import pprint

intelligence_dict = dict()

def hero_intelligence(hero_lis):
    for name in hero_lis:
        resp = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{name}')
        resp_get = resp.json()
        hero = resp_get['results']
        for info in hero:
            if info['name'] == name:
                intelligence = info['powerstats']['intelligence']
                intelligence_dict[info['name']] = int(intelligence)
    return intelligence_dict

def most_intelligence_hero(heroes):
    intel_point = []
    for key, value in heroes.items():
        intel_point.append(value)
    for key, value in heroes.items():
        if max(intel_point) == value:
            print(f'The most intelligence hero is {key}')
#
#
hero_list_data = ['Hulk','Captain America','Thanos']
print(hero_intelligence(hero_list_data))
most_intelligence_hero(intelligence_dict)


