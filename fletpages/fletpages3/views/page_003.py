import flet as ft
from fletx import Xview
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from flet.matplotlib_chart import MatplotlibChart


class page_003(Xview):

    def create_graph(self):
    
        matplotlib.use("svg")  # nécessaire pour Flet

        # Données
        np.random.seed(19680801)
        dt = 0.01
        t = np.arange(0, 30, dt)
        nse1 = np.random.randn(len(t))
        nse2 = np.random.randn(len(t))
        s1 = np.sin(2 * np.pi * 10 * t) + nse1
        s2 = np.sin(2 * np.pi * 10 * t) + nse2

        # Création du graph
        fig, axs = plt.subplots(2, 1)
        axs[0].plot(t, s1, t, s2)
        axs[0].set_xlim(0, 2)
        axs[0].set_xlabel("time")
        axs[0].set_ylabel("s1 and s2")
        axs[0].grid(True)

        axs[1].cohere(s1, s2, 256, 1.0 / dt)
        axs[1].set_ylabel("coherence")
        
        fig.tight_layout()

        return fig

    def build(self):

        fig = self.create_graph()  # on récupère la figure

        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("ceci est la page 3",size=30),
                            alignment=ft.alignment.top_center
                        ),

                        # Les boutons en haut
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=lambda e:self.go("/page_002")),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),

                        # Le graphique en dessous
                        ft.Container(
                            content=MatplotlibChart(fig, expand=True),
                            expand=True,
                            padding=10
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                )
            ]
        )
    
