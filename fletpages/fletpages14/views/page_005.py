import flet as ft
from fletx import Xview
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import maindata as md

class page_005(Xview):

    def create_graph1(self):
        
        print(len(md.labels), len(md.counts), len(md.colors_barres))
        #tracage
        fig, ax = plt.subplots(figsize=(8,6))
        ax.bar(md.labels, md.counts, color=md.colors_barres, edgecolor='black')
        ax.set_title("Répartition  des méthodes de découverte", fontsize=20, fontweight='bold')
        ax.set_xlabel("Méthodes de découverte", fontsize=14, fontweight='bold')
        ax.set_ylabel("nombre de planètes", fontsize=14, fontweight='bold')
        ax.tick_params(axis='x', rotation=45, labelsize=12)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        fig.tight_layout()
        plt.close(fig)
        return fig
    
    
    def create_graph2(self):
        
        fig, ax = plt.subplots(figsize=(8,6))
        md.grouped.plot(kind='bar', stacked=False, ax=ax, colormap='tab20')
        ax.set_title("Découverte de planètes par méthode et période", fontsize=14, fontweight='bold')
        ax.set_xlabel("Période", fontsize=12, fontweight='bold')
        ax.set_ylabel("Nombre de planètes découvertes", fontsize=14, fontweight='bold')
        ax.tick_params(axis='x', rotation=45, labelsize=12)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.legend(title="Méthodes de découverte", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)
        fig.tight_layout()
        plt.close(fig)
        return fig
    
    def create_graph3(self):
        fig, ax = plt.subplots(figsize=(8,6))
        ax.plot(np.random.rand(10), marker='o')
        ax.set_title("Graphique 3")
        ax.grid(True)
        fig.tight_layout()
        plt.close(fig)
        return fig

    def create_graph4(self):
        fig, ax = plt.subplots(figsize=(8,6))
        ax.pie([30, 40, 30], labels=['A', 'B', 'C'], autopct='%1.1f%%')
        ax.set_title("Graphique 4")
        fig.tight_layout()
        plt.close(fig)
        return fig

    def build(self):

        fig1 = self.create_graph1()  # on récupère la figure page5
        fig2 = self.create_graph2()  # on récupère la figure page5
        fig3 = self.create_graph3()
        fig4 = self.create_graph4()

        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("Méthodes de découvertes", size=30),
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=lambda e: self.go("/page_004"),
                                                    color=ft.colors.WHITE,
                                                    bgcolor=ft.colors.GREEN),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_006"),
                                                    color=ft.colors.WHITE,
                                                    bgcolor=ft.colors.BLUE),
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

