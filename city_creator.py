import json
import os.path
from os import path

new_cities = {'cities':[]}
city = ''
print('Type in cities... \ntype \'stop\' to stop')

while city != 'stop':
    city = input()
    if city != 'stop':
        new_cities['cities'].append(city)
    print(new_cities)

if path.exists('cities.json') == False:
    with open('cities.json', 'a') as outfile:
        new_cities['cities'] = list(set(new_cities['cities']))
        json.dump(new_cities, outfile, indent=2)
        print('Original .json being created')
else:
    with open('cities.json', 'r') as f:
        cities = json.load(f)
    for city in cities['cities']:
        new_cities['cities'].append(city)
    with open('cities.json', 'w') as outfile:
        new_cities['cities'] = list(set(new_cities['cities']))
        json.dump(new_cities, outfile, indent=2)
    print('Original .json updated')

