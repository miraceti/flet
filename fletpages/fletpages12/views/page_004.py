import flet as ft
from fletx import Xview
import matplotlib.pyplot as plt
import mplcursors
import numpy as np
from flet.matplotlib_chart import MatplotlibChart
import maindata as md


class page_004(Xview):
    def create_graph1(self):
        fig1, ax = plt.subplots(figsize=(8, 6))
        ax.plot(md.bin4_counts.index, md.bin4_counts.values, marker='o', linestyle='-', color='b', label='sans masse 1T')
        ax.set_title("Nombre de planètes par tranches de masse hors 1T", fontsize=16, fontweight='bold')
        ax.set_xlabel("tranches de masse (en M terre sans valeur 1)", fontsize=14, fontweight='bold')
        ax.set_ylabel("nombre de planètes", fontsize=14, fontweight='bold')
        ax.tick_params(axis='x', rotation=45, labelsize=12)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.legend()
        plt.tight_layout()
        plt.close(fig1)
        return fig1

    def create_graph2(self):
        fig2, ax = plt.subplots(figsize=(8, 6))
        ax.plot(md.bin4_counts_moins1.index, md.bin4_counts_moins1.values, marker='o', linestyle='-', color='r', label='Avec la valeur 1')
        ax.set_title("Distribution du nombre de planètes par tranches de masse (Avec la valeur 1)")
        ax.set_xlabel("Tranches de masse (en M_Terre sans la valeur 1)")
        ax.set_ylabel("Nombre de planètes")
        ax.grid(True)
        ax.legend()
        plt.tight_layout()
        plt.close(fig2)
        return fig2

    def create_graph3(self):
    
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

        fig1 = self.create_graph1()  # on récupère la figure
        fig2 = self.create_graph2()  # on récupère la figure
        fig3 = self.create_graph3()  # on récupère la figure

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
                                ft.ElevatedButton("Go to previous View", on_click=lambda e: self.go("/page_003"),
                                                    color=ft.Colors.WHITE,
                                                    bgcolor=ft.Colors.GREEN),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_005"),
                                                    color=ft.Colors.WHITE,
                                                    bgcolor=ft.Colors.BLUE),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        # Utiliser un Column avec scroll activé
                        ft.Column(
                            controls=[
                            MatplotlibChart(fig1, expand=True),
                            MatplotlibChart(fig2, expand=True),
                            MatplotlibChart(fig3, expand=True)
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

