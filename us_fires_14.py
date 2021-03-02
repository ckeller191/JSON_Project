import json

#import file, create readable

infile = open("US_fires_9_14.json", "r")
outfile = open("readable_fire_14_data.json", "w")

fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)

# make empty lists

lons, lats, brights = [], [], []

list_of_fires = fire_data


index = 0

while index < len(list_of_fires):
    for f in list_of_fires:
        if list_of_fires[index]['brightness'] > 450:
            lon = f['longitude']
            lat = f['latitude']
            bri = f['brightness']
            lons.append(lon)
            lats.append(lat)
            brights.append(bri)
    index += 1

print(lons[:10])

"""
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{ 'type':'scattergeo',
'lon':lons,
'lat':lats,
'marker':{
    'size':[5*bright for bright in brights],
    'color':brights,
    'colorscale':'Viridis',
    'reversescale':True,
    'colorbar':{'title':'Brightness'}}}]


my_layout = Layout(title='US Fires - 9/1/2020 through 9/13/2020')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='fires_9_1.html')

"""