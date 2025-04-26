import flet as ft
from fletx import Xview

class page_001(Xview):
    def build(self):
        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(
                    expand=True,  # << Permet aux enfants d'utiliser expand
                    controls=[
                        ft.Container(
                            content=ft.Text("ceci est la page 1", size=30),
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=self.back,
                                                  color=ft.colors.WHITE,
                                                  bgcolor=ft.colors.GREEN),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_002"),
                                                  color=ft.colors.WHITE,
                                                  bgcolor=ft.colors.BLUE),
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
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.AMBER,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.PURPLE,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.RED,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.GREEN,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.ORANGE,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.YELLOW,
                                        width=300,
                                        height=300,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.Text("Non clickable"),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.PINK,
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
