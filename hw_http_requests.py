import requests
from pprint import pprint


response = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk')
response_1 = requests.get('https://superheroapi.com/api/2619421814940190/search/Thanos')
response_2 = requests.get('https://superheroapi.com/api/2619421814940190/search/Captain_America')

Hulk = response.json()
Thanos = response_1.json()
Captain_America = response_2.json()

intelligence_dict = dict()
def intelligence_hero(resp, name):
    hero = resp['results']
    for info in hero:
        if info['name'] == name:
            intelligence = info['powerstats']['intelligence']
        # intelligence_list.append(intelligence)
            intelligence_dict[info['name']] = int(intelligence)
            return intelligence_dict

def most_intelligence_hero(heroes):
    intel_point = []
    for key, value in heroes.items():
        intel_point.append(value)
    for key, value in heroes.items():
        if max(intel_point) == value:
            print(f'The most intelligence hero is {key}')



intelligence_hero(Hulk, 'Hulk')
intelligence_hero(Thanos, 'Thanos')
intelligence_hero(Captain_America, 'Captain America')

most_intelligence_hero(intelligence_dict)

