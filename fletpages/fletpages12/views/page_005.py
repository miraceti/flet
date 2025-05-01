import flet as ft
from fletx import Xview
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import maindata as md

class page_005(Xview):

    def create_graph1(self):
        
        print(len(md.labels), len(md.counts), len(md.colors_barres))
        #tracage
        plt.figure(5, figsize=(8,6))
        plt.bar(md.labels, md.counts, color=md.colors_barres, edgecolor='black')
        plt.title("Répartition  des méthodes de découverte", fontsize=14)
        plt.xlabel("Méthodes de découverte", fontsize=12, fontweight='bold')
        plt.ylabel("nombre d'éléments", fontsize=12)
        plt.xticks(rotation=45 , fontsize=10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()


        fig1=plt.gcf()

        return fig1
    
    
    def create_graph2(self):
        
        
        #tracage
        md.grouped.plot(kind='bar', stacked=False, figsize=(8,6), colormap='tab20')

        plt.title("Découverte de planètes par méthode et période", fontsize=14)
        plt.xlabel("Période", fontsize=12, fontweight='bold')
        plt.ylabel("Nombre de planètes découvertes", fontsize=12)
        plt.xticks(rotation=45 , fontsize=10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend(title="Méthodes de découverte", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()


        fig2=plt.gcf()

        return fig2

    def build(self):

        fig1 = self.create_graph1()  # on récupère la figure page5
        fig2 = self.create_graph2()  # on récupère la figure page5

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
                            MatplotlibChart(fig2, expand=True)
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

