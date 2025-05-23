import flet as ft
from fletx import Xview

class page_002(Xview):
    def build(self):
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
                                                                bgcolor=ft.colors.LIGHT_GREEN,
                                                                padding=45,
                                                            )
                                                        ),
                                                        ft.Text("Encore du contenu très long " * 50),
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
