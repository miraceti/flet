import flet as ft
from fletx import Xview

class page_010(Xview):
    def build(self):
        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("ceci est la page 2", size=30),#old 10
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            
                            controls=[
                                    ft.ElevatedButton(
                                        "Go to previous View",
                                        on_click=lambda e: self.go("/page_001"),
                                        color=ft.Colors.WHITE,
                                        bgcolor=ft.Colors.GREEN
                                    ),
                                    ft.ElevatedButton(
                                        "Go to next View",
                                        on_click=lambda e: self.go("/page_003"),
                                        color=ft.Colors.WHITE,
                                        bgcolor=ft.Colors.BLUE
                                    ),
                                ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                )
            ]
        )

