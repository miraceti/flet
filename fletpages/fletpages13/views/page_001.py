import flet as ft
from fletx import Xview
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import maindata as md
import pandas as pd
import numpy as np

class page_001(Xview):

    def build(self):

        # Génération du graphique en camembert pour les masses
        def create_mass_distribution_pie():
            # Extraction brute des masses
            raw_masses = [item['pl_bmasse'] for item in md.data_table_dict]

            # Convertir les masses connues en float
            masses_known = pd.Series(pd.to_numeric(
                [m for m in raw_masses if m is not None],
                errors='coerce'
            )).dropna()

            count_unknown = len(raw_masses) - len(masses_known)

            # Filtrer les masses valides (> 0)
            masses_known = masses_known[masses_known > 0]

            # Comptages par tranche
            count_lt_2     = (masses_known < 2).sum()
            count_2_5      = ((masses_known >= 2) & (masses_known < 5)).sum()
            count_5_10     = ((masses_known >= 5) & (masses_known < 10)).sum()
            count_10_100   = ((masses_known >= 10) & (masses_known < 100)).sum()
            count_100_1000 = ((masses_known >= 100) & (masses_known <= 1000)).sum()
            count_gt_1000  = (masses_known > 1000).sum()

            # Préparer les données
            counts = [
                count_lt_2,
                count_2_5,
                count_5_10,
                count_10_100,
                count_100_1000,
                count_gt_1000,
                count_unknown
            ]

            total = sum(counts)

            labels = [
                f'<2 M⊕\n{count_lt_2} ({count_lt_2 / total:.1%})',
                f'2–5 M⊕\n{count_2_5} ({count_2_5 / total:.1%})',
                f'5–10 M⊕\n{count_5_10} ({count_5_10 / total:.1%})',
                f'10–100 M⊕\n{count_10_100} ({count_10_100 / total:.1%})',
                f'100–1000 M⊕\n{count_100_1000} ({count_100_1000 / total:.1%})',
                f'>1000 M⊕\n{count_gt_1000} ({count_gt_1000 / total:.1%})',
                f'Inconnue\n{count_unknown} ({count_unknown / total:.1%})'
            ]

            colors = [
                '#FF0000',  # Rouge vif  # <2
                '#00FF00',  # Vert fluo  # 2–5
                '#00BFFF',  # Bleu clair # 5–10
                '#00008B',  # Bleu foncé # 10–100
                '#FFA500',  # Orange     # RUPTURE
                '#FF69B4',  # Rose       # >1000
                '#AAAAAA' , # Gris      # Inconnue   
            ]

            # Création du graphique
            fig, ax = plt.subplots(figsize=(10, 10))
            wedges, texts = ax.pie(counts, labels=labels, colors=colors, startangle=140, labeldistance=1.4 )

            # Appliquer style aux labels
            for text in texts:
                text.set_fontsize(14)           # Taille de police
                text.set_fontweight('bold')     # Style gras

            # ax.set_title("Répartition des planètes par tranches de masse", fontsize=14, fontweight='bold')
            ax.set_title(
                "Répartition des planètes par tranches de masse",
                fontsize=20,
                fontweight='bold',
                backgroundcolor='lightgreen',  # ✅ couleur de fond
                color='black',                # ✅ couleur du texte (optionnel)
                pad=10                        # ✅ espace entre le titre et le graphique
            )
            ax.axis('equal')  # Assure un cercle parfait

            plt.tight_layout()
            plt.close(fig)
            return fig

        # Génération du graphique en camembert pour les rayons
        def create_radius_distribution_pie():
            rayons = pd.to_numeric(
                [item['pl_rade'] for item in md.data_table_dict],
                errors='coerce'
            )
            rayons_series = pd.Series(rayons)

            bins = {
                "0.0–1.0 R⊕": ((rayons_series > 0.0) & (rayons_series <= 1.0)),
                "1.0–1.5 R⊕": ((rayons_series > 1.0) & (rayons_series <= 1.5)),
                "1.5–2.0 R⊕": ((rayons_series > 1.5) & (rayons_series <= 2.0)),
                "2.0–3.0 R⊕": ((rayons_series > 2.0) & (rayons_series <= 3.0)),
                "3.0–4.0 R⊕": ((rayons_series > 3.0) & (rayons_series <= 4.0)),
                "4.0–10.0 R⊕": ((rayons_series > 4.0) & (rayons_series <= 10.0)),
                "10.0–100.0 R⊕": ((rayons_series > 10.0) & (rayons_series <= 100.0)),
                "Inconnu": rayons_series.isna()
            }

            labels = list(bins.keys())
            counts = [np.sum(cond) for cond in bins.values()]
            total = np.sum(counts)

            label_percentages = [
                f"{label} - {count/total:.1%}" for label, count in zip(labels, counts)
            ]

            colors = [
                'red', 'limegreen', 'deepskyblue', 'navy', 'orange',
                'hotpink', 'cyan',  'purple'
            ]

            fig, ax = plt.subplots(figsize=(10, 10))
            wedges, texts = ax.pie(
                counts,
                labels=label_percentages,
                colors=colors[:len(counts)],
                startangle=140,
                labeldistance=1.4  # augmente la distance entre le centre et les labels
            )

            for text in texts:
                text.set_fontsize(14)
                text.set_fontweight('bold')

            # ax.set_title("Répartition des planètes par tranches de rayon", fontsize=20, fontweight='bold')
            ax.set_title(
                "Répartition des planètes par tranches de rayon",
                fontsize=20,
                fontweight='bold',
                backgroundcolor='lightgreen',  # ✅ couleur de fond
                color='black',                # ✅ couleur du texte (optionnel)
                pad=10                        # ✅ espace entre le titre et le graphique
            )
            ax.axis('equal')
            plt.tight_layout()
            plt.close(fig)
            return fig

        # Génération du graphique en camembert pour les distances
        def create_distance_distribution_pie():
            # Extraction brute des distances
            raw_distances = [item['sy_dist'] for item in md.data_table_dict]

            # Convertir les distances connues en float
            distances_known = pd.Series(pd.to_numeric(
                [d for d in raw_distances if d is not None],
                errors='coerce'
            )).dropna()

            count_unknown = len(raw_distances) - len(distances_known)

            # Filtrer les distances valides (>= 10 pcs)
            distances_known = distances_known[distances_known >= 1]

            # Définir les tranches
            bins = {
                "0–10 pcs": ((distances_known >= 0) & (distances_known < 10)),
                "10–25 pcs": ((distances_known >= 10) & (distances_known < 25)),
                "25–50 pcs": ((distances_known >= 25) & (distances_known < 50)),
                "50–100 pcs": ((distances_known >= 50) & (distances_known < 100)),
                "100–250 pcs": ((distances_known >= 100) & (distances_known < 250)),
                "250–500 pcs": ((distances_known >= 250) & (distances_known < 500)),
                "500–1000 pcs": ((distances_known >= 500) & (distances_known < 1000)),
                "1000–2500 pcs": ((distances_known >= 1000) & (distances_known < 2500)),
                ">2500 pcs": (distances_known >= 2500),
                "Inconnu": pd.Series([True] * count_unknown)
            }

            labels = list(bins.keys())
            counts = [np.sum(cond) for cond in bins.values()]
            total = np.sum(counts)

            label_percentages = [
                f"{label}\n{count} ({count/total:.1%})" for label, count in zip(labels, counts)
            ]

            colors = [
                '#FF0000',    # Rouge vif  # 0–10
                '#00FF00',    # Vert fluo  # 10–25
                '#00BFFF',    # Bleu clair # 25–50
                '#00008B',    # Bleu foncé # 50–100
                '#FFA500',    # Orange     # 100–250
                '#FF69B4',    # Rose       # 250–500
                '#FF8B00',    # vert foncé # 500–1000
                '#0069B4',    # Rose       # 1000–2500
                '#00FFFF',    # Cyan       # >2500
                '#AAAAAA'     # gris         # Inconnu
            ]

            # Création du graphique
            fig, ax = plt.subplots(figsize=(10, 10))
            wedges, texts = ax.pie(
                counts,
                labels=label_percentages,
                colors=colors[:len(counts)],
                startangle=140,
                labeldistance=1.4,  # augmente la distance entre le centre et les labels
            )

            # Appliquer style aux labels
            for text in texts:
                text.set_fontsize(14)
                text.set_fontweight('bold')

            ax.set_title("Répartition des planètes par tranches de distance", fontsize=14, fontweight='bold')
            ax.set_title(
                "Répartition des planètes par tranches de distance",
                fontsize=20,
                fontweight='bold',
                backgroundcolor='lightgreen',  # ✅ couleur de fond
                color='black',                # ✅ couleur du texte (optionnel)
                pad=10                        # ✅ espace entre le titre et le graphique
            )
            ax.axis('equal')
            plt.tight_layout()
            plt.close(fig)
            return fig

        # Créer les figures
        fig_mass_pie = create_mass_distribution_pie()
        fig_radius_pie = create_radius_distribution_pie()
        fig_distance_pie = create_distance_distribution_pie()

        def generate_planet_rows(planet_list):
            rows = []
            for planet in planet_list:
                rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Container(
                                    content=ft.Text(str(planet.get("pl_name", "-")), size=10, color=ft.Colors.WHITE),
                                    width=50
                                )
                            ),
                            ft.DataCell(
                                ft.Container(
                                    content=ft.Text(f"{planet.get('sy_dist', '-'):.2f}", size=10, color=ft.Colors.WHITE),
                                    width=50
                                )
                            ),
                            ft.DataCell(
                                ft.Container(
                                    content=ft.Text(
                                        f"{planet.get('pl_bmasse', '-'):.2f}" if planet.get("pl_bmasse") else "-",
                                        size=10,
                                        color=ft.Colors.WHITE
                                    ),
                                    width=50
                                )
                            ),
                            ft.DataCell(
                                ft.Container(
                                    content=ft.Text(
                                        f"{planet.get('pl_rade', '-'):.2f}" if planet.get("pl_rade") else "-",
                                        size=10,
                                        color=ft.Colors.WHITE
                                    ),
                                    width=50
                                )
                            ),
                        ]
                    )
                )
            return rows


        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(
                    expand=True,
                    controls=[
                        ft.Container(
                            content=ft.Text("Les répartitions", size=30),
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=self.back,
                                                  color=ft.Colors.WHITE,
                                                  bgcolor=ft.Colors.GREEN),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_002"),
                                                  color=ft.Colors.WHITE,
                                                  bgcolor=ft.Colors.BLUE),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Container(
                            expand=True,
                            content=ft.ListView(
                                expand=True,
                                spacing=10,
                                padding=10,
                                controls=[
                                    MatplotlibChart(fig_mass_pie, expand=True),
                                    ft.Container(
                                        content=ft.DataTable(
                                            columns=[
                                                ft.DataColumn(
                                                    label=ft.Text("PLANÈTE", color=ft.Colors.WHITE), 
                                                    numeric=False,
                                                    tooltip="Nom de la planète",
                                                    on_sort=None
                                                ),
                                                ft.DataColumn(
                                                    label=ft.Text("Distance (pc)", color=ft.Colors.WHITE, size=10), 
                                                    tooltip="Distance en parsecs",
                                                    on_sort=None
                                                ),
                                                ft.DataColumn(
                                                    label=ft.Text("Masse", color=ft.Colors.WHITE, size=10), 
                                                    tooltip="Masse en M⊕",
                                                    on_sort=None
                                                ),
                                                ft.DataColumn(
                                                    label=ft.Text("Rayon", color=ft.Colors.WHITE, size=10), 
                                                    tooltip="Rayon en R⊕",
                                                    on_sort=None
                                                ),
                                            ],
                                            rows=generate_planet_rows(md.plus_proches_planetes),
                                            bgcolor=ft.Colors.BLACK,
                                            border=ft.border.all(1, ft.Colors.WHITE)
                                        ),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.PURPLE,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    MatplotlibChart(fig_distance_pie, expand=True),
                                    MatplotlibChart(fig_radius_pie, expand=True),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.ORANGE,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.YELLOW,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.Colors.PINK,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                ]
                            )
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                )
            ]
        )