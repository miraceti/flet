import flet as ft
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive

style_frame: dict = {
    "expand": True,
    "bgcolor": "#1f2128",
    "border_radius": 10,
    "padding": 20,
}

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("EXOPLANET 001")))
    page.title = "EXOPLANETES"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.SafeArea(ft.Text("Hello, Flet! \nil y a \n\n" + str(nb_exo) + " \n\nexoplanètes de découvertes actuellement")))
   


#nombre d'exoplanetes
p9=NasaExoplanetArchive.query_criteria(table="pscomppars", select="count(*)", order="hostname") 
#print("\nP9  Nombre d'exoplanetes\n",p9)
print(p9[0][0])
nb_exo = p9[0][0]

ft.app(main)
