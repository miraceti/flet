import flet as ft
from fletx import Xview
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import maindata as md
import pandas as pd


class page_006(Xview):


    def create_graph1(self):
    
        matplotlib.use("svg")  # nécessaire pour Flet

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

        # Tracer le graphique
        plt.figure(figsize=(10, 6))
        point_size=60
        # Tracé des points par méthode
        for method in methods:
            subset = df[df['discoverymethod'] == method]
            plt.scatter(
                subset['pl_orbper'], subset['pl_bmasse'],
                #s=subset['size'],
                s=point_size,
                color=colors[method],
                label=method,
                alpha=0.7,
                edgecolors='w'
            )

        # 🎯 Légende des méthodes (en bas à droite)
        legend_handles_methods = [
            plt.scatter([], [], s=100, color=colors[method], label=method, alpha=0.7, edgecolors='w')
            for method in methods
        ]
        legend_methods = plt.legend(
            handles=legend_handles_methods,
            title="Méthodes de découverte",
            fontsize=10,
            title_fontsize=11,
            loc="lower right",
            bbox_to_anchor=(1, 0)
        )
        plt.gca().add_artist(legend_methods)

        # 🎯 Légende des tailles (plus haut, au-dessus)
        size_legend_values = [1, 2, 3]
        size_legend_handles = [
            plt.scatter([], [], s=rade * 10, color='gray', alpha=0.6, label=f"{rade} R⊕", edgecolors='w')
            for rade in size_legend_values
        ]
        legend_sizes = plt.legend(
            handles=size_legend_handles,
            title="Rayon planète (R⊕)",
            fontsize=10,
            title_fontsize=11,
            loc="lower right",
            bbox_to_anchor=(1, 0.50)  # ↖️ Ajusté pour apparaître clairement au-dessus
        )
        plt.gca().add_artist(legend_sizes)

        # Détails du graphique
        plt.title("Planètes découvertes : Masse vs période orbitale", fontsize=16)
        plt.xlabel("Période orbitale (jours)", fontsize=14)
        plt.ylabel("Masse (pl_bmasse)", fontsize=14)
        plt.xscale('log')
        plt.yscale('log')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()

        fig=plt.gcf()
        plt.close(fig)

        return fig

    def create_graph2(self):
    
        matplotlib.use("svg")  # nécessaire pour Flet

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

        # Tracer le graphique
        plt.figure(figsize=(10, 6))
        point_size = 60
        # Tracé des points par méthode
        for method in methods:
            subset = df[
                (df['discoverymethod'] == method)&
                (df['pl_rade'] <= 100) &
                (df['pl_rade'] > 0)
                ]
            plt.scatter(
                subset['pl_orbper'], subset['pl_rade'],
                #s=subset['size'],
                s = point_size,
                color=colors[method],               label=method,
                alpha=0.7,
                edgecolors='w'
            )

        # 🎯 Légende des méthodes (en bas à droite)
        legend_handles_methods = [
            plt.scatter([], [], s=100, color=colors[method], label=method, alpha=0.7, edgecolors='w')
            for method in methods
        ]
        legend_methods = plt.legend(
            handles=legend_handles_methods,
            title="Méthodes de découverte",
            fontsize=10,
            title_fontsize=11,
            loc="lower right",
            bbox_to_anchor=(1, 0)
        )
        plt.gca().add_artist(legend_methods)

        # 🎯 Légende des tailles (plus haut, au-dessus)
        size_legend_values = [1, 2, 3]
        size_legend_handles = [
            plt.scatter([], [], s=rade * 10, color='gray', alpha=0.6, label=f"{rade} R⊕", edgecolors='w')
            for rade in size_legend_values
        ]
        legend_sizes = plt.legend(
            handles=size_legend_handles,
            title="Rayon planète (R⊕)",
            fontsize=10,
            title_fontsize=11,
            loc="lower right",
            bbox_to_anchor=(1, 0.50)  # ↖️ Ajusté pour apparaître clairement au-dessus
        )
        plt.gca().add_artist(legend_sizes)

        # Détails du graphique
        plt.title("Planètes découvertes : Rayon inf 100 vs période orbitale", fontsize=16)
        plt.xlabel("Période orbitale (jours)", fontsize=14)
        plt.ylabel("Rayon (pl_rade)", fontsize=14)
        plt.xscale('log')
        plt.yscale('log')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()

        fig=plt.gcf()
        plt.close(fig)

        return fig
    
    def create_graph3(self):
    
        matplotlib.use("svg")  # nécessaire pour Flet

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

        # Tracer le graphique
        plt.figure(figsize=(10, 6))
        point_size = 60
        # Tracé des points par méthode
        for method in methods:
            subset = df[
                (df['discoverymethod'] == method)&
                (df['pl_rade'] <= 10) &
                (df['pl_rade'] > 0)
                ]
            plt.scatter(
                subset['pl_orbper'], subset['pl_rade'],
                #s=subset['size'],
                s = point_size,
                color=colors[method],               label=method,
                alpha=0.7,
                edgecolors='w'
            )

        # 🎯 Légende des méthodes (en bas à droite)
        legend_handles_methods = [
            plt.scatter([], [], s=100, color=colors[method], label=method, alpha=0.7, edgecolors='w')
            for method in methods
        ]
        legend_methods = plt.legend(
            handles=legend_handles_methods,
            title="Méthodes de découverte",
            fontsize=10,
            title_fontsize=11,
            loc="lower right",
            bbox_to_anchor=(1, 0)
        )
        plt.gca().add_artist(legend_methods)

        # 🎯 Légende des tailles (plus haut, au-dessus)
        size_legend_values = [1, 2, 3]
        size_legend_handles = [
            plt.scatter([], [], s=rade * 10, color='gray', alpha=0.6, label=f"{rade} R⊕", edgecolors='w')
            for rade in size_legend_values
        ]
        legend_sizes = plt.legend(
            handles=size_legend_handles,
            title="Rayon planète (R⊕)",
            fontsize=10,
            title_fontsize=11,
            loc="lower right",
            bbox_to_anchor=(1, 0.50)  # ↖️ Ajusté pour apparaître clairement au-dessus
        )
        plt.gca().add_artist(legend_sizes)

        # Détails du graphique
        plt.title("Planètes découvertes : Rayon inf 10 vs période orbitale", fontsize=16)
        plt.xlabel("Période orbitale (jours)", fontsize=14)
        plt.ylabel("Rayon (pl_rade)", fontsize=14)
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
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("Périodes orbitales", size=30),
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
                            MatplotlibChart(fig2, expand=True),
                            MatplotlibChart(fig3, expand=True),
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

