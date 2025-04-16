import flet as ft
from fletx import Xview

class NextView(Xview):
    def build(self):
        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Text("ceci est la page NEXT",size=30),
                ft.ElevatedButton("Go to previous View", on_click=self.back)
            ]
        )
    
