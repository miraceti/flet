import flet as ft
from fletx import Xview
import maindata as md

class page_002(Xview):
    def build(self):
        # Configuration des tableaux
        self.table_configs = {
            "distance": {
                "liste": sorted(
                    [
                        {
                            "pl_name": item["pl_name"],
                            "sy_dist": round(item["sy_dist"], 2) if item["sy_dist"] is not None else 0,
                        }
                        for item in md.planetes_tries_sy_dist
                    ],
                    key=lambda x: (x["sy_dist"] == 0, x["sy_dist"])
                ),
                "table": "self.table_distance",
                "columns": [
                    {"key": "pl_name", "label": "Planète", "type": "text"},
                    {"key": "sy_dist", "label": "Distance (ps)", "type": "number"},
                ],
                "filter_text": None,  # Sera initialisé
                "sort_column": "pl_name",
                "sort_asc": True,
            },
            "rayon": {
                "liste": sorted(
                    [
                        {
                            "pl_name": item["pl_name"],
                            "pl_rade": round(item["pl_rade"], 2) if item["pl_rade"] is not None else 0,
                        }
                        for item in md.planetes_tries_sy_dist
                    ],
                    key=lambda x: (x["pl_rade"] == 0, x["pl_rade"])
                ),
                "table": "self.table_rayon",
                "columns": [
                    {"key": "pl_name", "label": "Planète", "type": "text"},
                    {"key": "pl_rade", "label": "Rayon", "type": "number"},
                ],
                "filter_text": None,  # Sera initialisé
                "sort_column": "pl_name",
                "sort_asc": True,
            },
            "annee": {
                "liste": sorted(
                    [
                        {
                            "pl_name": item["pl_name"],
                            "disc_year": round(item["disc_year"], 2) if item["disc_year"] is not None else 0,
                        }
                        for item in md.planetes_tries_disc_year
                    ],
                    key=lambda x: (x["disc_year"] == 0, x["disc_year"])
                ),
                "table": "self.table_annee",
                "columns": [
                    {"key": "pl_name", "label": "Planète", "type": "text"},
                    {"key": "disc_year", "label": "Année", "type": "number"},
                ],
                "filter_text": None,  # Sera initialisé
                "sort_column": "pl_name",
                "sort_asc": True,
            },
        }

        # Initialisation des tableaux et champs de filtrage
        for table_id, config in self.table_configs.items():
            # Créer un champ de filtrage distinct par tableau
            config["filter_text"] = ft.TextField(
                label=f"Filtrer les planètes ({table_id})",
                on_change=lambda e, tid=table_id: self.update_table(e, tid)
            )
            # Créer le DataTable
            table = ft.DataTable(
                columns=[
                    ft.DataColumn(
                        label=ft.Text(
                            col["label"],
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.WHITE,
                        ),
                        on_sort=lambda e, col_key=col["key"], tid=table_id: self.sort_by(col_key, tid)
                    )
                    for col in config["columns"]
                ],
                rows=[],
                bgcolor=ft.colors.BLACK,
                column_spacing=5,
                horizontal_lines=ft.BorderSide(1, ft.colors.WHITE),
                vertical_lines=ft.BorderSide(1, ft.colors.WHITE),
                data_row_min_height=50,
                heading_row_height=60,
            )
            # Assigner le tableau à l'attribut correspondant
            if table_id == "distance":
                self.table_distance = table
            elif table_id == "annee":
                self.table_annee = table
            elif table_id == "rayon":
                self.table_rayon = table
            # Mettre à jour le tableau initialement
            self.update_table(None, table_id)

        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.Container(
                                content=ft.Text("Informations exoplanètes", size=30),
                                alignment=ft.alignment.top_center
                            ),
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        "Go to previous View",
                                        on_click=lambda e: self.go("/page_001"),
                                        color=ft.colors.WHITE,
                                        bgcolor=ft.colors.GREEN
                                    ),
                                    ft.ElevatedButton(
                                        "Go to next View",
                                        on_click=lambda e: self.go("/page_003"),
                                        color=ft.colors.WHITE,
                                        bgcolor=ft.colors.BLUE
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                            ft.Container(
                                expand=True,
                                height=800,
                                content=ft.Tabs(
                                    selected_index=0,
                                    animation_duration=300,
                                    expand=1,
                                    tabs=[
                                        ft.Tab(
                                            text="Année",
                                            icon=ft.Icon(name=ft.Icons.FAVORITE, color=ft.colors.PINK),
                                            content=ft.Container(
                                                expand=True,
                                                padding=10,
                                                content=ft.Column(
                                                    expand=True,
                                                    scroll=ft.ScrollMode.AUTO,
                                                    controls=[
                                                        ft.Text("Année de découverte", size=24, weight=ft.FontWeight.BOLD),
                                                        self.table_configs["annee"]["filter_text"],
                                                        ft.Container(
                                                            height=800,
                                                            bgcolor=ft.colors.PINK,
                                                            content=ft.Column(
                                                                scroll=ft.ScrollMode.AUTO,
                                                                controls=[self.table_annee]
                                                            )
                                                        ),
                                                    ]
                                                )
                                            )
                                        ),
                                        ft.Tab(
                                            text="Rayon",
                                            icon=ft.Icon(name=ft.Icons.LOCAL_FIRE_DEPARTMENT, color=ft.colors.RED),
                                            content=ft.Container(
                                                expand=True,
                                                content=ft.Column(
                                                    expand=True,
                                                    scroll=ft.ScrollMode.AUTO,
                                                    controls=[
                                                        ft.Text("Année de découverte", size=24, weight=ft.FontWeight.BOLD),
                                                        self.table_configs["rayon"]["filter_text"],
                                                        ft.Container(
                                                            height=800,
                                                            bgcolor=ft.colors.PINK,
                                                            content=ft.Column(
                                                                scroll=ft.ScrollMode.AUTO,
                                                                controls=[self.table_rayon]
                                                            )
                                                        ),
                                                    ]
                                                )
                                            )
                                        ),
                                        ft.Tab(
                                            text="Distance",
                                            icon=ft.Icon(name=ft.Icons.LOCAL_CAFE, color=ft.colors.GREEN),
                                            content=ft.Container(
                                                expand=True,
                                                padding=10,
                                                content=ft.Column(
                                                    expand=True,
                                                    scroll=ft.ScrollMode.AUTO,
                                                    controls=[
                                                        ft.Text("Distances des exoplanètes", size=24, weight=ft.FontWeight.BOLD),
                                                        self.table_configs["distance"]["filter_text"],
                                                        ft.Container(
                                                            height=800,
                                                            bgcolor=ft.colors.GREEN,
                                                            content=ft.Column(
                                                                scroll=ft.ScrollMode.AUTO,
                                                                controls=[self.table_distance]
                                                            )
                                                        ),
                                                    ]
                                                )
                                            )
                                        ),
                                        ft.Tab(
                                            text="Tab 4",
                                            icon=ft.Icon(name=ft.Icons.LOCAL_PHONE, color=ft.colors.BLUE),
                                            content=ft.Container(
                                                expand=True,
                                                content=ft.ListView(
                                                    expand=True,
                                                    spacing=10,
                                                    padding=20,
                                                    controls=[
                                                        ft.Card(
                                                            elevation=30,
                                                            content=ft.Container(
                                                                content=ft.Text("Amazing TAB 12 content", size=50, weight=ft.FontWeight.BOLD),
                                                                border_radius=ft.border_radius.all(20),
                                                                bgcolor=ft.colors.BLUE,
                                                                padding=45,
                                                            )
                                                        ),
                                                        ft.Text("Encore du contenu très long " * 50),
                                                    ]
                                                )
                                            )
                                        ),
                                        ft.Tab(
                                            text="Tab 5",
                                            icon=ft.Icon(name=ft.Icons.LOCAL_BAR, color=ft.colors.ORANGE),
                                            content=ft.Container(
                                                expand=True,
                                                content=ft.ListView(
                                                    expand=True,
                                                    spacing=10,
                                                    padding=20,
                                                    controls=[
                                                        ft.Card(
                                                            elevation=30,
                                                            content=ft.Container(
                                                                content=ft.Text("Amazing TAB 12 content", size=50, weight=ft.FontWeight.BOLD),
                                                                border_radius=ft.border_radius.all(20),
                                                                bgcolor=ft.colors.ORANGE,
                                                                padding=45,
                                                            )
                                                        ),
                                                        ft.Text("Encore du contenu très long " * 50),
                                                    ]
                                                )
                                            )
                                        ),
                                        ft.Tab(
                                            text="Tab 6",
                                            icon=ft.Icon(name=ft.Icons.LOCAL_AIRPORT, color=ft.Colors.PURPLE),
                                            content=ft.Container(
                                                expand=True,
                                                content=ft.ListView(
                                                    expand=True,
                                                    spacing=10,
                                                    padding=20,
                                                    controls=[
                                                        ft.Card(
                                                            elevation=30,
                                                            content=ft.Container(
                                                                content=ft.Text("Amazing TAB 12 content", size=50, weight=ft.FontWeight.BOLD),
                                                                border_radius=ft.border_radius.all(20),
                                                                bgcolor=ft.colors.PURPLE,
                                                                padding=45,
                                                            )
                                                        ),
                                                        ft.Text("Encore du contenu très long " * 50),
                                                    ]
                                                )
                                            )
                                        ),
                                        ft.Tab(
                                            text="Tab 7",
                                            icon=ft.Icon(name=ft.Icons.ELECTRIC_BIKE, color=ft.colors.YELLOW),
                                            content=ft.Container(
                                                expand=True,
                                                content=ft.ListView(
                                                    expand=True,
                                                    spacing=10,
                                                    padding=20,
                                                    controls=[
                                                        ft.Card(
                                                            elevation=30,
                                                            content=ft.Container(
                                                                content=ft.Text("Amazing TAB 12 content", size=50, weight=ft.FontWeight.BOLD),
                                                                border_radius=ft.border_radius.all(20),
                                                                bgcolor=ft.colors.YELLOW,
                                                                padding=45,
                                                            )
                                                        ),
                                                        ft.Text("Encore du contenu très long " * 50),
                                                    ]
                                                )
                                            )
                                        ),
                                    ],
                                )
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                    )
                )
            ]
        )

    def sort_by(self, column, table_id):
        config = self.table_configs[table_id]
        if config["sort_column"] == column:
            config["sort_asc"] = not config["sort_asc"]
        else:
            config["sort_column"] = column
            config["sort_asc"] = True
        print(f"Sorting {table_id} by {column}, ascending: {config['sort_asc']}")  # Débogage
        self.update_table(None, table_id)

    def update_table(self, e, table_id):
        config = self.table_configs[table_id]
        liste = config["liste"]
        filter_text = config["filter_text"]
        sort_column = config["sort_column"]
        sort_asc = config["sort_asc"]
        columns = config["columns"]

        # Filtrage
        filtered = [
            item for item in liste
            if filter_text.value.lower() in item["pl_name"].lower()
        ]

        # Tri
        def sort_key(item):
            value = item[sort_column]
            # Gérer les types pour le tri
            for col in columns:
                if col["key"] == sort_column and col["type"] == "number":
                    return float(value) if value is not None else float('inf')
            return value.lower() if isinstance(value, str) else value

        sorted_list = sorted(
            filtered,
            key=sort_key,
            reverse=not sort_asc
        )

        # Sélectionner le tableau
        table = getattr(self, "table_" + table_id)

        # Débogage
        print(f"Updating table {table_id} with {len(sorted_list)} rows, first few: {[item.get(config['columns'][1]['key'], '') for item in sorted_list[:5]]}")

        # Mettre à jour les lignes
        table.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(
                            str(item[col["key"]]),
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.GREEN if table_id == "distance" else ft.colors.PINK,
                        )
                    )
                    for col in columns
                ]
            )
            for item in sorted_list
        ]

        self.update()