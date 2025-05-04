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
        ax.plot(md.liste_annee, md.liste_nb, marker='o', linestyle='-', color='b', label='Nombre par année', linewidth=4.0)
        ax.set_title("Nombre de planètes par année", fontsize=16, fontweight='bold')
        ax.set_xlabel("Année)", fontsize=14, fontweight='bold')
        ax.set_ylabel("nombre de planètes", fontsize=14, fontweight='bold')
        ax.tick_params(axis='x', rotation=45)#, labelsize=12)
        # ✅ Chiffres axes X et Y en gras et plus grands
        for label in ax.get_xticklabels():
            label.set_fontsize(12)
            label.set_fontweight('bold')
        for label in ax.get_yticklabels():
            label.set_fontsize(12)
            label.set_fontweight('bold')
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.legend(loc='upper right', fontsize=12,prop={'weight': 'bold'})
        plt.tight_layout()
        plt.close(fig1)
        return fig1

    def create_graph2(self):
        fig2, ax = plt.subplots(figsize=(8, 6))
        ax.plot(md.bin4_counts_moins1.index, md.bin4_counts_moins1.values, marker='o', linestyle='-', color='r', label='Avec la valeur 1', linewidth=4.0)
        ax.set_title("Distribution du nombre de planètes par tranches de masse ", fontsize=16, fontweight='bold')
        ax.set_xlabel("Tranches de masse (en M_Terre )", fontsize=14, fontweight='bold')
        ax.set_ylabel("Nombre de planètes", fontsize=14, fontweight='bold')
        # ✅ Chiffres axes X et Y en gras et plus grands
        for label in ax.get_xticklabels():
            label.set_fontsize(12)
            label.set_fontweight('bold')
        for label in ax.get_yticklabels():
            label.set_fontsize(12)
            label.set_fontweight('bold')
        ax.grid(True)
        ax.legend(loc='upper right', fontsize=12,prop={'weight': 'bold'})
        plt.tight_layout()
        plt.close(fig2)
        return fig2

    def create_graph3(self):
        # Extraire les rayons valides sous forme numérique
        rayons = pd.to_numeric(
            [item['pl_rade'] for item in md.data_table_dict if item['pl_rade'] is not None],
            errors='coerce'
        )
        rayons = rayons[(rayons > 0) & (rayons <= 30)]  # Ne garder que les rayons ≤ 30 R⊕

        fig3, ax = plt.subplots(figsize=(8, 6))

        # Histogramme
        ax.hist(rayons, bins=30, color='skyblue', edgecolor='black', label='Rayons des exoplanètes (≤ 30 R⊕)')

        # Ajouter des lignes pour les planètes du système solaire
        ax.axvline(x=1.0, color='green', linestyle='--', linewidth=2, label='Terre (1 R⊕)')
        ax.axvline(x=3.9, color='orange', linestyle='--', linewidth=2, label='Neptune (3.9 R⊕)')
        ax.axvline(x=4.0, color='purple', linestyle='--', linewidth=2, label='Uranus (4.0 R⊕)')
        ax.axvline(x=9.4, color='cyan', linestyle='--', linewidth=2, label='Saturne (9.4 R⊕)')
        ax.axvline(x=11.0, color='red', linestyle='--', linewidth=2, label='Jupiter (11.0 R⊕)')

        # Paramètres du graphique
        ax.set_xlabel("Rayon (R⊕)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Nombre de planètes", fontsize=14, fontweight='bold')
        ax.set_title("Distribution des rayons d’exoplanètes (≤ 30 R⊕)", fontsize=16, fontweight='bold')
        ax.set_yscale('log')
        ax.grid(True, which="both", linestyle='--', linewidth=0.5)

        # Légende en gras
        ax.legend(loc='upper right', fontsize=12, prop={'weight': 'bold'})

        plt.tight_layout()
        plt.close(fig3)
        return fig3

    def create_graph4(self):
        # Extraire les rayons valides sous forme numérique
        rayons = pd.to_numeric([item['pl_rade'] for item in md.data_table_dict if item['pl_rade'] is not None], errors='coerce')
        rayons = rayons[(rayons > 0) & (rayons <= 30)]  # Ne prendre que les rayons entre 0 et 30

        fig4, ax = plt.subplots(figsize=(8, 6))

        ax.hist(rayons, bins=30, color='skyblue', edgecolor='black', label='Rayons des exoplanètes (≤ 30 R⊕)')

        ax.set_xlabel("Rayon (R⊕)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Nombre de planètes", fontsize=14, fontweight='bold')
        ax.set_title("Distribution des rayons d’exoplanètes (≤ 30 R⊕)", fontsize=16, fontweight='bold')
        ax.set_yscale('log')
        ax.grid(True, which="both", linestyle='--', linewidth=0.5)
        ax.legend(loc='upper right', fontsize=12, prop={'weight': 'bold'})

        plt.tight_layout()
        plt.close(fig4)
        return fig4
    
    def create_graph5(self):
        # Extraire les rayons valides
        rayons = pd.to_numeric([item['pl_rade'] for item in md.data_table_dict if item['pl_rade'] is not None], errors='coerce')
        rayons = rayons[(rayons > 30) & (rayons < 100)]  # rayons strictement > 30

        fig5, ax = plt.subplots(figsize=(8, 6))
        ax.hist(rayons, bins=10, color='salmon', edgecolor='black', label='Rayons > 30 R⊕')
        ax.set_xlabel("Rayon (R⊕)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Nombre de planètes (log)", fontsize=14, fontweight='bold')
        ax.set_title("Distribution des rayons d’exoplanètes (> 30 R⊕)", fontsize=16, fontweight='bold')
        ax.set_yscale('log')
        # ✅ Chiffres axes X et Y en gras et plus grands
        for label in ax.get_xticklabels():
            label.set_fontsize(12)
            label.set_fontweight('bold')
        for label in ax.get_yticklabels():
            label.set_fontsize(12)
            label.set_fontweight('bold')
        ax.grid(True, which="both", linestyle='--', linewidth=0.5)
        ax.legend(fontsize=12, loc='upper right', prop={'weight': 'bold'})  # légende en gras
        plt.tight_layout()
        plt.close(fig5)
        return fig5

    def build(self):

        fig1 = self.create_graph1()  # on récupère la figure
        fig2 = self.create_graph2()  # on récupère la figure
        fig3 = self.create_graph3()  # on récupère la figure
        fig4 = self.create_graph4()
        fig5 = self.create_graph5()

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
                            MatplotlibChart(fig3, expand=True),
                            MatplotlibChart(fig4, expand=True),
                            MatplotlibChart(fig5, expand=True),
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

