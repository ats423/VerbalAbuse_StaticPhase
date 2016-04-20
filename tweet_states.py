# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:56:56 2016

@authors: Sara Arango and Neil Verosh
"""

import json
import geojson
import numpy as np


json_data1=open('us.json').read()
State = geojson.loads(json_data1)

def point_inside_polygon(x,y,poly):
# From http://www.ariel.com.au/a/python-point-int-poly.html

    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

json_data2=open('Tweets_Geolocation.json').read()
Tweets = geojson.loads(json_data2)

json_data3=open('centroids-tweets.json').read()
twtState = json.loads(json_data3)

for state in twtState['features']:
    state['properties']['count'] = 0. 

ct = 0
for twt in Tweets:
    x = twt['coordinates']['coordinates'][0]
    y = twt['coordinates']['coordinates'][1]
    ct += 1
    for st in State['features']:
        poly = st['geometry']['coordinates'][0]
        if len(np.shape(np.array(poly))) == 2:
            poly = st['geometry']['coordinates'][0]
            if point_inside_polygon(x,y,poly):
                for state in twtState['features']:
                    if state['properties']['name']==st['properties']['name']:
                        state['properties']['count'] += 1.  
                        
        elif len(np.shape(np.array(poly))) == 3:
            poly = st['geometry']['coordinates'][0][0]
            if point_inside_polygon(x,y,poly):
                for state in twtState['features']:
                    if state['properties']['name']==st['properties']['name']:
                        state['properties']['count'] += 1.    
            
tot_dens = 0.00
for state in twtState['features']:
    state['properties']['twtDensity'] = state['properties']['count'] / state['properties']['population']
    tot_dens += state['properties']['twtDensity']

for state in twtState['features']:
    state['properties']['twtDensity'] = state['properties']['twtDensity'] / tot_dens
    
with open('twtDensity.json', 'w') as fp:
    json.dump(twtState, fp)
    
    
"""  

dic = {'type': "FeatureCollection","features":[]}

for state in State['features']:
    dic['features'].append({'geometry': {'coordinates': state['geometry']['coordinates'], 'type': 'Polygon'}, 'type': 'Feature','properties':{'prop0': state['properties']['name'], 'prop1': {'this': 'that'}}})



{ "type": "FeatureCollection",
"features": [
    {"type": "Feature",
    "geometry": {
    "type": "Polygon",
    "coordinates": 

         },
         "properties": {
             "prop0": "value0",
             "prop1": {"this": "that"}
}}]}





{ "type": "FeatureCollection",
"features": [
    {"type": "Feature",
    "geometry": {
    "type": "Polygon",
    "coordinates": [
        [[-87.359296, 35.00118],
          [-85.606675, 34.984749],
          [-85.431413, 34.124869],
          [-85.184951, 32.859696],
          [-85.069935, 32.580372],
          [-84.960397, 32.421541],
          [-85.004212, 32.322956],
          [-84.889196, 32.262709],
          [-85.058981, 32.13674],
          [-85.053504, 32.01077],
          [-85.141136, 31.840985],
          [-85.042551, 31.539753],
          [-85.113751, 31.27686],
          [-85.004212, 31.003013],
          [-85.497137, 30.997536],
          [-87.600282, 30.997536],
          [-87.633143, 30.86609],
          [-87.408589, 30.674397],
          [-87.446927, 30.510088],
          [-87.37025, 30.427934],
          [-87.518128, 30.280057],
          [-87.655051, 30.247195],
          [-87.90699, 30.411504],
          [-87.934375, 30.657966],
          [-88.011052, 30.685351],
          [-88.10416, 30.499135],
          [-88.137022, 30.318396],
          [-88.394438, 30.367688],
          [-88.471115, 31.895754],
          [-88.241084, 33.796253],
          [-88.098683, 34.891641],
          [-88.202745, 34.995703],
          [-87.359296, 35.00118]]
          ]
         },
         "properties": {
             "prop0": "value0",
             "prop1": {"this": "that"}
}}]}

"""
