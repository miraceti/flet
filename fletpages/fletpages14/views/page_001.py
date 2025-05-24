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
            fig, ax = plt.subplots(figsize=(12, 12))
            #wedges, texts = ax.pie(counts, labels=labels, colors=colors, startangle=140, labeldistance=1.3 )

            wedges, texts = ax.pie(
                counts,
                labels=labels,
                colors=colors,
                startangle=140,
                labeldistance=1.3  # ✅ plus proche du graphique
            )

            # Appliquer style aux labels
            for text in texts:
                text.set_fontsize(24)           # Taille de police
                text.set_fontweight('bold')     # Style gras
                # text.set_bbox(dict(facecolor='white', edgecolor='none', pad=1.0))

            # Exemple de repositionnement manuel :
            texts[0].set_position((texts[0].get_position()[0] + 0.15, texts[0].get_position()[1] + 0.05))
            texts[1].set_position((texts[1].get_position()[0] + 0.15, texts[1].get_position()[1] - 0.05))
            texts[2].set_position((texts[2].get_position()[0] + 0.30, texts[2].get_position()[1]))
            texts[3].set_position((texts[3].get_position()[0] + 0.30, texts[3].get_position()[1]))

            texts[6].set_position((texts[6].get_position()[0], texts[6].get_position()[1] - 0.50))

            # ax.set_title("Répartition des planètes par tranches de masse", fontsize=14, fontweight='bold')
            ax.set_title(
                "Répartition des planètes par tranches de masse",
                fontsize=30,
                fontweight='bold',
                backgroundcolor='lightgreen',  # ✅ couleur de fond
                color='black',                # ✅ couleur du texte (optionnel)
                pad=10                        # ✅ espace entre le titre et le graphique
            )
            ax.axis('equal')  # Assure un cercle parfait

            fig.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.15)  # ✅ ajuste les marges manuellement

            #plt.tight_layout()
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

            fig, ax = plt.subplots(figsize=(12, 12))
            wedges, texts = ax.pie(
                counts,
                labels=label_percentages,
                colors=colors[:len(counts)],
                startangle=140,
                labeldistance=1.01 , # augmente la distance entre le centre et les labels
                textprops={'fontsize': 18}
            )

            for text in texts:
                text.set_fontsize(24)
                text.set_fontweight('bold')

            texts[0].set_position((texts[0].get_position()[0] + 0.50, texts[0].get_position()[1]))

            texts[3].set_position((texts[3].get_position()[0] - 0.30, texts[3].get_position()[1] - 0.50))
            texts[4].set_position((texts[4].get_position()[0] - 0.30, texts[4].get_position()[1] - 0.10))

            # ax.set_title("Répartition des planètes par tranches de rayon", fontsize=20, fontweight='bold')
            ax.set_title(
                "Répartition des planètes par tranches de rayon",
                fontsize=30,
                fontweight='bold',
                backgroundcolor='lightgreen',  # ✅ couleur de fond
                color='black',                # ✅ couleur du texte (optionnel)
                pad=10                        # ✅ espace entre le titre et le graphique
            )
            ax.axis('equal')

            fig.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.15)  # ✅ ajuste les marges manuellement

            #plt.tight_layout()
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
            fig, ax = plt.subplots(figsize=(12, 12))
            wedges, texts = ax.pie(
                counts,
                labels=label_percentages,
                colors=colors[:len(counts)],
                startangle=140,
                labeldistance=1.05,  # augmente la distance entre le centre et les labels
            )

            # Appliquer style aux labels
            for text in texts:
                text.set_fontsize(24)
                text.set_fontweight('bold')

            # Exemple de repositionnement manuel :
            texts[0].set_position((texts[0].get_position()[0], texts[0].get_position()[1]))
            texts[1].set_position((texts[1].get_position()[0], texts[1].get_position()[1] - 0.05))
            texts[2].set_position((texts[2].get_position()[0], texts[2].get_position()[1]))

            texts[7].set_position((texts[7].get_position()[0] + 0.50, texts[7].get_position()[1] + 0.05))
            texts[8].set_position((texts[8].get_position()[0] + 0.20, texts[8].get_position()[1] + 0.20))
            texts[9].set_position((texts[9].get_position()[0]       , texts[9].get_position()[1] + 0.10))

            ax.set_title("Répartition des planètes par tranches de distance", fontsize=14, fontweight='bold')
            ax.set_title(
                "Répartition des planètes par tranches de distance",
                fontsize=30,
                fontweight='bold',
                backgroundcolor='lightgreen',  # ✅ couleur de fond
                color='black',                # ✅ couleur du texte (optionnel)
                pad=40                        # ✅ espace entre le titre et le graphique
            )
            ax.axis('equal')

            fig.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.15)  # ✅ ajuste les marges manuellement

            #plt.tight_layout()
            plt.close(fig)
            return fig
        
        # Génération du graphique en camembert pour les densite
        def create_densite_distribution_pie():
            # Extraction brute des distances
            raw_densite = [item['pl_dense'] for item in md.data_table_dict]

            # Convertir les distances connues en float
            densite_known = pd.Series(pd.to_numeric(
                [d for d in raw_densite if d is not None],
                errors='coerce'
            )).dropna()

            count_unknown = len(raw_densite) - len(densite_known)

            # Filtrer les densites valides (>= 10 pcs)
            densite_known = densite_known[densite_known >= 1]

            # Définir les tranches
            bins = {
                "0–2 gcm3": ((densite_known >= 0) & (densite_known < 2)),
                "2–3 gcm3": ((densite_known >= 2) & (densite_known < 3)),
                "3–4 gcm3": ((densite_known >= 3) & (densite_known < 4)),
                "4–5 gcm3": ((densite_known >= 4) & (densite_known < 5)),
                "5–8 gcm3": ((densite_known >= 5) & (densite_known < 8)),
                "8–10 gcm3": ((densite_known >= 8) & (densite_known < 10)),
                "10-25 gcm3": ((densite_known >= 10) & (densite_known < 25)),
                "25–50 gcm3": ((densite_known >= 25)& (densite_known < 50)),
                ">50 gcm3": (densite_known >= 50),
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
            fig, ax = plt.subplots(figsize=(12, 12))
            wedges, texts = ax.pie(
                counts,
                labels=label_percentages,
                colors=colors[:len(counts)],
                startangle=140,
                labeldistance=1.05,  # augmente la distance entre le centre et les labels
            )

            # Appliquer style aux labels
            for text in texts:
                text.set_fontsize(24)
                text.set_fontweight('bold')

            # Exemple de repositionnement manuel :
            texts[0].set_position((texts[0].get_position()[0] + 0.70, texts[0].get_position()[1] + 0.50))
            texts[1].set_position((texts[1].get_position()[0] + 0.60, texts[1].get_position()[1] + 0.40))
            texts[2].set_position((texts[2].get_position()[0], texts[2].get_position()[1] + 0.40))

            texts[3].set_position((texts[3].get_position()[0], texts[3].get_position()[1] + 0.30))
            texts[4].set_position((texts[4].get_position()[0], texts[4].get_position()[1] + 0.20))
            texts[5].set_position((texts[5].get_position()[0], texts[5].get_position()[1] + 0.10))

            texts[7].set_position((texts[7].get_position()[0] + 0.50, texts[7].get_position()[1] - 0.40))
            texts[8].set_position((texts[8].get_position()[0] + 0.90, texts[8].get_position()[1] ))
            texts[9].set_position((texts[9].get_position()[0] - 0.80, texts[9].get_position()[1] + 0.10))

            ax.set_title("Répartition des planètes par tranches de densités", fontsize=14, fontweight='bold')
            ax.set_title(
                "Répartition des planètes par tranches de densités",
                fontsize=30,
                fontweight='bold',
                backgroundcolor='lightgreen',  # ✅ couleur de fond
                color='black',                # ✅ couleur du texte (optionnel)
                pad=40                        # ✅ espace entre le titre et le graphique
            )
            ax.axis('equal')

            fig.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.15)  # ✅ ajuste les marges manuellement

            #plt.tight_layout()
            plt.close(fig)
            return fig
        
        # Génération du graphique en camembert pour les temperatures
        def create_temperature_distribution_pie():
            # Extraction brute des distances
            raw_temperature = [item['pl_eqt'] for item in md.data_table_dict]

            # Convertir les temperatures connues en float
            temperature_known = pd.Series(pd.to_numeric(
                [d for d in raw_temperature if d is not None],
                errors='coerce'
            )).dropna()

            count_unknown = len(raw_temperature) - len(temperature_known)

            # Filtrer les distances valides (>= 10 pcs)
            temperature_known = temperature_known[temperature_known >= 1]

            # Définir les tranches
            bins = {
                "0–200 K": ((temperature_known >= 0) & (temperature_known < 200)),
                "200–250 K": ((temperature_known >= 200) & (temperature_known < 250)),
                "250–300 K": ((temperature_known >= 250) & (temperature_known < 300)),
                "300–350 K": ((temperature_known >= 300) & (temperature_known < 350)),
                "350–400 K": ((temperature_known >= 350) & (temperature_known < 400)),
                "400–500 K": ((temperature_known >= 400) & (temperature_known < 500)),
                "500–750 K": ((temperature_known >= 500) & (temperature_known < 750)),
                "750–1000 K": ((temperature_known >= 750) & (temperature_known < 1000)),
                ">1000 K": (temperature_known >= 1000),
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
            fig, ax = plt.subplots(figsize=(12, 12))
            wedges, texts = ax.pie(
                counts,
                labels=label_percentages,
                colors=colors[:len(counts)],
                startangle=140,
                labeldistance=1.05,  # augmente la distance entre le centre et les labels
            )

            # Appliquer style aux labels
            for text in texts:
                text.set_fontsize(24)
                text.set_fontweight('bold')

            # Exemple de repositionnement manuel :
            texts[0].set_position((texts[0].get_position()[0] + 0.40, texts[0].get_position()[1] + 0.40))
            texts[1].set_position((texts[1].get_position()[0] + 0.20, texts[1].get_position()[1] + 0.20))

            texts[2].set_position((texts[2].get_position()[0], texts[2].get_position()[1] + 0.00))
            texts[3].set_position((texts[3].get_position()[0], texts[3].get_position()[1] - 0.10))

            texts[4].set_position((texts[4].get_position()[0] + 0.20, texts[4].get_position()[1] - 0.20))
            texts[5].set_position((texts[5].get_position()[0] + 0.10, texts[5].get_position()[1] - 0.20))

            texts[6].set_position((texts[6].get_position()[0] + 0.60, texts[6].get_position()[1] + 0.20))
            texts[7].set_position((texts[7].get_position()[0] - 0.20, texts[7].get_position()[1] + 0.40))
            texts[8].set_position((texts[8].get_position()[0] - 0.60, texts[8].get_position()[1] - 0.10))
            texts[9].set_position((texts[9].get_position()[0] + 0.30, texts[9].get_position()[1] - 0.30))

            ax.set_title("Répartition des planètes par tranches de température", fontsize=14, fontweight='bold')
            ax.set_title(
                "Répartition des planètes par tranches de température",
                fontsize=28,
                fontweight='bold',
                backgroundcolor='lightgreen',  # ✅ couleur de fond
                color='black',                # ✅ couleur du texte (optionnel)
                pad=40                        # ✅ espace entre le titre et le graphique
            )
            ax.axis('equal')

            fig.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.15)  # ✅ ajuste les marges manuellement

            #plt.tight_layout()
            plt.close(fig)
            return fig

        # Créer les figures
        fig_mass_pie = create_mass_distribution_pie()
        fig_radius_pie = create_radius_distribution_pie()
        fig_distance_pie = create_distance_distribution_pie()
        fig_densite_pie = create_densite_distribution_pie()
        fig_temperature_pie = create_temperature_distribution_pie()

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
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.BLACK,
                                        width=440,  # ✅ élargi pour éviter tout tronquage
                                        height=300,
                                        border_radius=10,
                                        padding=10,
                                        content=ft.Column(
                                            spacing=5,
                                            controls=[
                                                ft.Row(
                                                    controls=[
                                                        ft.Text("PLANÈTE", size=12, weight=ft.FontWeight.BOLD, width=120, color=ft.colors.WHITE),
                                                        ft.Text("Distance (pc)", size=12, weight=ft.FontWeight.BOLD, width=80, color=ft.colors.WHITE),
                                                        ft.Text("Masse", size=12, weight=ft.FontWeight.BOLD, width=60, color=ft.colors.WHITE),
                                                        ft.Text("Rayon", size=12, weight=ft.FontWeight.BOLD, width=80, color=ft.colors.WHITE),  # ✅ élargi
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                ),
                                                ft.Container(
                                                    height=240,
                                                    content=ft.ListView(
                                                        spacing=5,
                                                        auto_scroll=False,
                                                        controls=[
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Text(p["pl_name"], width=120, color=ft.colors.WHITE),
                                                                    ft.Text(f"{p['sy_dist']:.2f}" if p["sy_dist"] is not None else "-", width=80, color=ft.colors.WHITE),
                                                                    ft.Text(f"{p['pl_bmasse']:.2f}" if p["pl_bmasse"] is not None else "-", width=60, color=ft.colors.WHITE),
                                                                    ft.Text(f"{p['pl_rade']:.2f}" if p["pl_rade"] is not None else "-", width=80, color=ft.colors.WHITE),
                                                                ],
                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            )
                                                            for p in md.plus_proches_planetes[:100]
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),

                                    MatplotlibChart(fig_distance_pie, expand=True),
                                    MatplotlibChart(fig_radius_pie, expand=True),
                                    ft.Container(
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.BLACK,
                                        width=440,  # ✅ élargi pour éviter tout tronquage
                                        height=300,
                                        border_radius=10,
                                        padding=10,
                                        content=ft.Column(
                                            spacing=5,
                                            controls=[
                                                ft.Row(
                                                    controls=[
                                                        ft.Text("PLANÈTE", size=12, weight=ft.FontWeight.BOLD, width=120, color=ft.colors.WHITE),
                                                        ft.Text("Distance (pc)", size=12, weight=ft.FontWeight.BOLD, width=80, color=ft.colors.WHITE),
                                                        ft.Text("Temp(K)", size=12, weight=ft.FontWeight.BOLD, width=60, color=ft.colors.WHITE),
                                                        ft.Text("Densité", size=12, weight=ft.FontWeight.BOLD, width=60, color=ft.colors.WHITE),  # ✅ élargi
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                ),
                                                ft.Container(
                                                    height=240,
                                                    content=ft.ListView(
                                                        spacing=5,
                                                        auto_scroll=False,
                                                        controls=[
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Text(p["pl_name"], width=120, color=ft.colors.WHITE),
                                                                    ft.Text(f"{p['sy_dist']:.2f}" if p["sy_dist"] is not None else "-", width=80, color=ft.colors.WHITE),
                                                                    ft.Text(f"{p['pl_eqt']:.2f}" if p["pl_eqt"] is not None else "-", width=60, color=ft.colors.WHITE),
                                                                    ft.Text(f"{p['pl_dense']:.2f}" if p["pl_dense"] is not None else "-", width=60, color=ft.colors.WHITE),
                                                                ],
                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            )
                                                            for p in md.plus_proches_planetes[:100]
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    MatplotlibChart(fig_temperature_pie, expand=True),
                                    MatplotlibChart(fig_densite_pie, expand=True),
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