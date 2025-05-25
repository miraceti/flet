import flet as ft
from fletx import Xview
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from flet.matplotlib_chart import MatplotlibChart
import maindata as md
import pandas as pd


class page_003(Xview):

    def create_graph1(self):
        # Convertir en DataFrame
        df = pd.DataFrame(md.data_table_dict)

        # Remplacer les valeurs None dans 'pl_rade' par 1
        df['pl_rade'] = df['pl_rade'].fillna(0)

        # Supprimer les lignes avec des valeurs manquantes critiques (pl_bmasse ou pl_orbper)
        df = df.dropna(subset=['pl_bmasse', 'pl_orbper'])

        # Préparer les données
        df['size'] = df['pl_rade'] * 10
        methods = df['discoverymethod'].unique()
        colors = {method: plt.cm.tab10(i % 10) for i, method in enumerate(methods)}
        matplotlib.use("svg")  # nécessaire pour Flet

        # Méthodes à afficher
        selected_methods = [
            "Transit",
            "Radial Velocity",
            "Orbital Brightness Modulation",
            "Transit Timing Variation"
        ]

        # Filtrer le DataFrame
        filtered_df = df[df['discoverymethod'].isin(selected_methods)]

        # Redéfinir la palette de couleurs pour les méthodes sélectionnées
        colors = {method: plt.cm.tab10(i) for i, method in enumerate(selected_methods)}

        # Taille fixe pour tous les points
        point_size = 60

        # Tracé
        plt.figure(figsize=(10, 6))

        for method in selected_methods:
            subset = filtered_df[filtered_df['discoverymethod'] == method]
            plt.scatter(
                subset['pl_rade'], subset['pl_dens'],
                s=point_size,
                color=colors[method],
                label=method,
                alpha=0.7,
                edgecolors='w'
            )

        # Légende des méthodes (couleur)
        legend_handles_methods = [
            plt.scatter([], [], s=point_size, color=colors[method], label=method, alpha=0.7, edgecolors='w')
            for method in selected_methods
        ]
        plt.legend(
            handles=legend_handles_methods,
            title="Méthodes de découverte",
            fontsize=10,
            title_fontsize=11,
            loc="lower right",
            bbox_to_anchor=(1, 0)
        )

        # Titre et axes
        plt.title("Planètes découvertes : Rayon vs Densité", fontsize=16)
        plt.xlabel("Rayon (R⊕)", fontsize=14)
        plt.ylabel("Densité (g/cm³)", fontsize=14)
        plt.xscale('log')
        plt.yscale('log')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()

        fig=plt.gcf()
        plt.close(fig)

        return fig
    

    def create_graph2(self):
        # Convertir en DataFrame
        df = pd.DataFrame(md.data_table_dict)

        # Remplacer les valeurs None dans 'pl_rade' par 1
        df['pl_rade'] = df['pl_rade'].fillna(0)

        # Supprimer les lignes avec des valeurs manquantes critiques (pl_bmasse ou pl_orbper)
        df = df.dropna(subset=['pl_bmasse', 'pl_orbper'])

        # Préparer les données
        df['size'] = df['pl_rade'] * 10
        methods = df['discoverymethod'].unique()
        colors = {method: plt.cm.tab10(i % 10) for i, method in enumerate(methods)}
        matplotlib.use("svg")  # nécessaire pour Flet

        # Méthodes à afficher
        selected_methods = [
            "Transit",
            "Radial Velocity",
            "Orbital Brightness Modulation",
            "Transit Timing Variation"
        ]

        # Filtrer le DataFrame par méthode et rayon
        filtered_df = df[
            (df['discoverymethod'].isin(selected_methods)) &
            (df['pl_rade'] <= 100)&  # Éliminer les rayons > 100 R⊕
            (df['pl_dens'] <= 1000)
        ]

        # Redéfinir les couleurs pour les méthodes sélectionnées
        colors = {method: plt.cm.tab10(i) for i, method in enumerate(selected_methods)}

        # Taille fixe pour tous les points
        point_size = 60

        # Tracé
        plt.figure(figsize=(10, 6))

        for method in selected_methods:
            subset = filtered_df[filtered_df['discoverymethod'] == method]
            plt.scatter(
                subset['pl_rade'], subset['pl_dens'],
                s=point_size,
                color=colors[method],
                label=method,
                alpha=0.7,
                edgecolors='w'
            )

        # Légende des méthodes
        legend_handles_methods = [
            plt.scatter([], [], s=point_size, color=colors[method], label=method, alpha=0.7, edgecolors='w')
            for method in selected_methods
        ]
        plt.legend(
            handles=legend_handles_methods,
            title="Méthodes de découverte",
            fontsize=10,
            title_fontsize=11,
            loc="lower right",
            bbox_to_anchor=(1, 0)
        )

        # Titre et axes
        plt.title("Planètes découvertes : Rayon vs Densité (R ≤ 100)", fontsize=16)
        plt.xlabel("Rayon (R⊕)", fontsize=14)
        plt.ylabel("Densité (g/cm³)", fontsize=14)
        plt.xscale('log')
        plt.yscale('log')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()

        fig=plt.gcf()
        plt.close(fig)

        return fig
    
    def create_graph3(self):
        # Convertir en DataFrame
        df = pd.DataFrame(md.data_table_dict)

        # Remplacer les valeurs None dans 'pl_rade' par 1
        df['pl_rade'] = df['pl_rade'].fillna(0)

        # Supprimer les lignes avec des valeurs manquantes critiques (pl_bmasse ou pl_orbper)
        df = df.dropna(subset=['pl_bmasse', 'pl_orbper'])

        # Préparer les données
        df['size'] = df['pl_rade'] * 10
        methods = df['discoverymethod'].unique()
        colors = {method: plt.cm.tab10(i % 10) for i, method in enumerate(methods)}
        matplotlib.use("svg")  # nécessaire pour Flet

        # Méthodes à afficher
        selected_methods = [
            "Transit",
            "Radial Velocity",
            "Orbital Brightness Modulation",
            "Transit Timing Variation"
        ]

        # Filtrer le DataFrame par méthode et rayon
        filtered_df = df[
            (df['discoverymethod'].isin(selected_methods)) &
            (df['pl_rade'] <= 10)&  # Éliminer les rayons > 100 R⊕
            (df['pl_dens'] <= 1000)
        ]

        # Redéfinir les couleurs pour les méthodes sélectionnées
        colors = {method: plt.cm.tab10(i) for i, method in enumerate(selected_methods)}

        # Taille fixe pour tous les points
        point_size = 60

        # Tracé
        plt.figure(figsize=(10, 6))

        for method in selected_methods:
            subset = filtered_df[filtered_df['discoverymethod'] == method]
            plt.scatter(
                subset['pl_rade'], subset['pl_dens'],
                s=point_size,
                color=colors[method],
                label=method,
                alpha=0.7,
                edgecolors='w'
            )

        # Légende des méthodes
        legend_handles_methods = [
            plt.scatter([], [], s=point_size, color=colors[method], label=method, alpha=0.7, edgecolors='w')
            for method in selected_methods
        ]
        plt.legend(
            handles=legend_handles_methods,
            title="Méthodes de découverte",
            fontsize=10,
            title_fontsize=11,
            loc="lower right",
            bbox_to_anchor=(1, 0)
        )

        # Titre et axes
        plt.title("Planètes découvertes : Rayon vs Densité (R ≤ 100)", fontsize=16)
        plt.xlabel("Rayon (R⊕)", fontsize=14)
        plt.ylabel("Densité (g/cm³)", fontsize=14)
        plt.xscale('log')
        plt.yscale('log')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()

        fig=plt.gcf()
        plt.close(fig)

        return fig


    def build(self):

        fig1 = self.create_graph1()  # on récupère la figure
        fig2 = self.create_graph2()  # on récupère la figure
        fig3 = self.create_graph3()  # on récupère la figure

        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("Densités",size=30),
                            alignment=ft.alignment.top_center
                        ),

                        # Les boutons en haut
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=lambda e: self.go("/page_002"),
                                                    color=ft.Colors.WHITE,
                                                    bgcolor=ft.Colors.GREEN),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_004"),
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
    
