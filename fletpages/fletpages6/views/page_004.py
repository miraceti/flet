import flet as ft
from fletx import Xview
import matplotlib.pyplot as plt
import mplcursors
import numpy as np
from flet.matplotlib_chart import MatplotlibChart


class page_004(Xview):
    def create_graph(self):
    
        # Données
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Création du graphique
        fig, ax = plt.subplots()
        ax.plot(x, y)

        # Ajouter des curseurs interactifs
        mplcursors.cursor(ax, hover=True)
        return fig


    def build(self):

        fig = self.create_graph()  # on récupère la figure

        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("ceci est la page 4", size=30),
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=lambda e: self.go("/page_003")),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_005")),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        # Utiliser un Column avec scroll activé
                        ft.Column(
                            controls=[
                            MatplotlibChart(fig, expand=True)
                            ],
                            scroll=ft.ScrollMode.AUTO,  # Active le scroll si nécessaire
                            expand=True,  # Prend tout l'espace disponible
                            height=600,   # Ajuster la hauteur ici
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                )
            ]
        )

