import flet as ft
from fletx import Xview

class HomeView(Xview):
    def build(self):
        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text("ceci est la page HOME",size=30),
                            alignment=ft.alignment.top_center
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Go to Next View", on_click=lambda e:self.go("/page_001")),
                            ],
                            alignment=ft.MainAxisAlignment.END
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                )
            ]
            )
                        
                       
            
