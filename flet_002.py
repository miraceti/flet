import flet as ft

from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive

#nombre d'exoplanetes
p9=NasaExoplanetArchive.query_criteria(table="pscomppars", select="count(*)", order="hostname") 
#print("\nP9  Nombre d'exoplanetes\n",p9)
print(p9[0][0])
nb_exo = p9[0][0]


def main(page: ft.Page):
    page.title = "EXOPLANETES"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.SafeArea(ft.Text("Hello, Flet! \nil y a \n\n" + str(nb_exo) + " \n\nexoplanètes de découvertes actuellement")))


ft.app(main)
