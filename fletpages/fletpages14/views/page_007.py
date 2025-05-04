import flet as ft
from fletx import Xview

class page_007(Xview):
    def build(self):
        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("ceci est la page 7", size=30),
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to previous View", on_click=lambda e: self.go("/page_006"),
                                                    color=ft.colors.WHITE,
                                                    bgcolor=ft.colors.GREEN),
                                ft.ElevatedButton("Go to next View", on_click=lambda e: self.go("/page_008"),
                                                    color=ft.colors.WHITE,
                                                    bgcolor=ft.colors.BLUE),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                )
            ]
        )

