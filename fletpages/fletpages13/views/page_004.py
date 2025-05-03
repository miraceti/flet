import flet as ft
from fletx import Xview
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import maindata as md
import pandas as pd


class page_004(Xview):
    def create_graph1(self):
        fig1, ax = plt.subplots(figsize=(8, 6))
        ax.plot(md.liste_annee, md.liste_nb, marker='o', linestyle='-', color='b', label='Nombre par année', linewidth=2.5)
        ax.set_title("Nombre de planètes par année", fontsize=16, fontweight='bold')
        ax.set_xlabel("Année)", fontsize=14, fontweight='bold')
        ax.set_ylabel("nombre de planètes", fontsize=14, fontweight='bold')
        ax.tick_params(axis='x', rotation=45, labelsize=12)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.legend(loc='upper right', fontsize=12)
        plt.tight_layout()
        plt.close(fig1)
        return fig1

    def create_graph2(self):
        fig2, ax = plt.subplots(figsize=(8, 6))
        ax.plot(md.bin4_counts_moins1.index, md.bin4_counts_moins1.values, marker='o', linestyle='-', color='r', label='Avec la valeur 1', linewidth=2.5)
        ax.set_title("Distribution du nombre de planètes par tranches de masse ", fontsize=16, fontweight='bold')
        ax.set_xlabel("Tranches de masse (en M_Terre )", fontsize=14, fontweight='bold')
        ax.set_ylabel("Nombre de planètes", fontsize=14, fontweight='bold')
        ax.grid(True)
        ax.legend(loc='upper right', fontsize=12)
        plt.tight_layout()
        plt.close(fig2)
        return fig2

    def create_graph3(self):
        # Extraire les rayons valides sous forme numérique
        rayons = pd.to_numeric([item['pl_rade'] for item in md.data_table_dict if item['pl_rade'] is not None], errors='coerce')
        rayons = rayons[(rayons > 0) & (rayons < 100)]  # éliminer les valeurs extrêmes ou nulles

        fig3, ax = plt.subplots(figsize=(8, 6))

        # Histogramme automatique
        ax.hist(rayons, bins=100, color='skyblue', edgecolor='black', label='Rayons des exoplanètes')

        # Axe Y en log si besoin
        ax.set_yscale('log')  # ou commente-le pour une échelle normale

        ax.set_xlabel("Rayon (R⊕)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Nombre de planètes (log)", fontsize=14, fontweight='bold')
        ax.set_title("Distribution des rayons d’exoplanètes", fontsize=16, fontweight='bold')
        ax.grid(True, which="both", linestyle='--', linewidth=0.5)
        ax.legend(loc='upper right', fontsize=12)
        plt.tight_layout()
        plt.close(fig3)
        return fig3


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
                            content=ft.Text("Années - Masses - Rayons", size=30),
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

