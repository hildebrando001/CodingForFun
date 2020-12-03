#/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

def get_pokemons(url='https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset': offset} if offset else {}

    response = requests.get(url, params=args)

    if response.status_code == 200:
        payload = response.json()
        pokemons = payload.get('results', [])

        if pokemons:
            for pokemon in pokemons:
                name = pokemon['name']
                print(name)

        next = input("Continuar listando? [Y/N]").lower()
        if next =='y' or next=='Y':
            get_pokemons(offset=offset+20)

url = 'https://pokeapi.co/api/v2/pokemon-form/'
get_pokemons()