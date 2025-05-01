import flet as ft
from fletx import Xview
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import maindata as md

class page_006(Xview):


    def create_graph(self):
    
        matplotlib.use("svg")  # nécessaire pour Flet

        # Tracer le graphique
        plt.figure(figsize=(10, 6))
        for method in md.unique_methods:
            # Filtrer les données par méthode
            x_vals = [md.x[i] for i in range(len(md.x)) if md.methods[i] == method]
            y_vals = [md.y[i] for i in range(len(md.y)) if md.methods[i] == method]
            size_vals = [md.sizes[i] for i in range(len(md.sizes)) if md.methods[i] == method]
            plt.scatter(x_vals, y_vals, s=size_vals, color=md.colors_methods[method], label=method, alpha=0.7, edgecolors='w')

        # Ajouter des détails au graphique
        plt.title("Planètes découvertes : Distance vs Masse", fontsize=16)
        plt.xlabel("Distance (sy_dist)", fontsize=14)
        plt.ylabel("Masse (pl_bmasse)", fontsize=14)
        plt.legend(title="Méthodes de découverte", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()

        fig=plt.gcf()

        return fig


    def build(self):

        fig1 = self.create_graph()  # on récupère la figure
        fig2 = self.create_graph()  # on récupère la figure

        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("ceci est la page 6", size=30),
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=lambda e: self.go("/page_005"),
                                                    color=ft.colors.WHITE,
                                                    bgcolor=ft.colors.GREEN),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_007"),
                                                    color=ft.colors.WHITE,
                                                    bgcolor=ft.colors.BLUE),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        # Utiliser un Column avec scroll activé
                        ft.Column(
                            controls=[
                            MatplotlibChart(fig1, expand=True),
                            
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

