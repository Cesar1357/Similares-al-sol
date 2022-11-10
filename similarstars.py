import plotly.express as px
import pandas as pd

star_mass = []
star_rad = []
info = pd.read_csv('./Nuevo.csv')
stars = pd.DataFrame(info)

for star_data in stars:
    if(star_data[4] >= 0.7 and star_data[4] <= 1.0):
        star_mass.append(star_data[4])
        star_rad.append(star_data[5])

fig = px.scatter(x=star_mass,y=star_rad)
fig.show()
print(star_mass)
print(star_rad)
