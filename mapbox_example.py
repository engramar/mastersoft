import plotly.plotly as py
from plotly.graph_objs import *

#mapbox_access_token = 'Bf0W5YziXabqHGnJR8nr'
mapbox_access_token = 'pk.eyJ1IjoiZW5ncmFtYXIiLCJhIjoiY2o4YXpqNjlnMDhsYTJ3cDYyenVrY2FtNCJ9.XTFWmcvOXipEb9Fc7oxkWg'

data = Data([
    Scattermapbox(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
        marker=Marker(
            size=11
        ),
        text=['Montreal'],
    )
])

layout = Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=45,
            lon=-73
        ),
        pitch=0,
        zoom=5
    ),
)

fig = dict(data=data, layout=layout)
py.plot(fig, filename='Montreal Mapbox')
