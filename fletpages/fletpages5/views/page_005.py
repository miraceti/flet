import flet as ft
from fletx import Xview
import numpy as np
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import maindata as md

class page_005(Xview):

    def create_graph(self):
        

        #tracage
        plt.figure(5, figsize=(8,6))
        plt.bar(md.labels, md.counts, color=md.colors, edgecolor='black')
        plt.title("Répartition  des méthodes de découverte", fontsize=14)
        plt.xlabel("Méthodes de découverte", fontsize=12, fontweight='bold')
        plt.ylabel("nombre d'éléments", fontsize=12)
        plt.xticks(rotation=45 , fontsize=10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()


        fig=plt.gcf()

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
                            content=ft.Text("ceci est la page 5", size=30),
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=lambda e: self.go("/page_004")),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_006")),
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
                            height=800,   # Ajuster la hauteur ici
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                )
            ]
        )

