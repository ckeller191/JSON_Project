import json

#import file, create readable

infile = open("US_fires_9_14.json", "r")
outfile = open("readable_fire_14_data.json", "w")

fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)

# make empty lists

lons, lats, brights = [], [], []

relevant_fires = []


index = 0

while index < len(fire_data):
    for f in fire_data:
        if fire_data[index]['brightness'] > 450:
            relevant_fires.append(fire_data[index])
        index += 1



for f in relevant_fires:
    lon = f['longitude']
    lat = f['latitude']
    bri = f['brightness']
    lons.append(lon)
    lats.append(lat)
    brights.append(bri)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{ 'type':'scattergeo',
'lon':lons,
'lat':lats,
'marker':{
    'size':[.05*bright for bright in brights],
    'color':brights,
    'colorscale':'Viridis',
    'reversescale':True,
    'colorbar':{'title':'Brightness'}}}]


my_layout = Layout(title='US Fires - 9/14/2020 through 9/20/2020')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='fires_9_14.html')

