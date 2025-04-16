import flet as ft
from fletx import Xview

class page_002(Xview):
    def build(self):
        # ✅ Données dynamiques
        self.liste = [
            {"planete": "a1", "distance": "12"},
            {"planete": "a2", "distance": "14"},
            {"planete": "a3", "distance": "20"},
            {"planete": "a4", "distance": "25"},
        ]

        self.filter_text = ft.TextField(label="Filtrer les planètes", on_change=self.update_table)
        self.sort_column = "planete"
        self.sort_asc = True

        self.table = ft.DataTable(
            columns=[
                ft.DataColumn(
                    label=ft.Text("Planète"),
                    on_sort=lambda e: self.sort_by("planete")
                ),
                ft.DataColumn(
                    label=ft.Text("Distance"),
                    on_sort=lambda e: self.sort_by("distance")
                ),
            ],
            rows=[]  # rempli dynamiquement
        )

        self.update_table(None)  # première mise à jour



        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            scroll=ft.ScrollMode.AUTO,  # <--- permet de scroller si besoin
            controls=[
                ft.Container(
                    expand=True,  # <-- rend la page flexible
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.Container(
                                content=ft.Text("ceci est la page 2", size=30),
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

                            # ✅ Ici, on entoure les Tabs avec un Container expandable
                            ft.Container(
                                expand=True,
                                height=500,
                                content=ft.Tabs(
                                    selected_index=0,
                                    animation_duration=300,
                                    expand=1,  # utile ici
                                    tabs=[
                                        ft.Tab(
                                            text="Tab 1",
                                            icon=ft.Icon(name=ft.Icons.FAVORITE, color=ft.Colors.PINK),
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
                                                                content=ft.Text("Amazing TAB 1 content", size=50, weight=ft.FontWeight.BOLD),
                                                                border_radius=ft.border_radius.all(20),
                                                                bgcolor=ft.colors.PINK,
                                                                padding=45,
                                                            )
                                                        ),
                                                        ft.Text("Texte additionnel " * 50),
                                                    ]
                                                )
                                            )
                                        ),
                                        ft.Tab(
                                            text="Tab 2",
                                            icon=ft.Icon(name=ft.Icons.LOCAL_FIRE_DEPARTMENT, color=ft.Colors.RED),
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
                                                                bgcolor=ft.colors.RED,
                                                                padding=45,
                                                            )
                                                        ),
                                                        ft.Text("Encore du contenu très long " * 50),
                                                    ]
                                                )
                                            )
                                        ),
                                        ft.Tab(
                                            text="Tab 3",
                                            icon=ft.Icon(name=ft.Icons.LOCAL_CAFE, color=ft.Colors.GREEN),
                                            content=ft.Container(
                                                expand=True,
                                                padding=10,
                                                content=ft.Column(
                                                    expand=True,
                                                    controls=[
                                                        ft.Text("Tableau des planètes", size=24, weight=ft.FontWeight.BOLD),
                                                        self.filter_text,
                                                        self.table
                                                    ]
                                                )
                                            )
                                        ),
                                        ft.Tab(
                                            text="Tab 4",
                                            icon=ft.Icon(name=ft.Icons.LOCAL_PHONE, color=ft.Colors.BLUE),
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
                                            icon=ft.Icon(name=ft.Icons.LOCAL_BAR, color=ft.Colors.ORANGE),
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
                                            icon=ft.Icon(name=ft.Icons.ELECTRIC_BIKE, color=ft.Colors.YELLOW),
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

    def sort_by(self, column):
        # Inverser l'ordre si on reclique sur la même colonne
        if self.sort_column == column:
            self.sort_asc = not self.sort_asc
        else:
            self.sort_column = column
            self.sort_asc = True
        self.update_table(None)



    def update_table(self, e):
        filtered = [
            item for item in self.liste
            if self.filter_text.value.lower() in item["planete"].lower()
        ]

        sorted_list = sorted(
            filtered,
            key=lambda x: x[self.sort_column],
            reverse=not self.sort_asc
        )

        self.table.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(item["planete"])),
                    ft.DataCell(ft.Text(item["distance"])),
                ]
            )
            for item in sorted_list
        ]

        self.update()
