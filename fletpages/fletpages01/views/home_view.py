import flet as ft
from fletx import Xview

class HomeView(Xview):
    def build(self):
        return ft.View(
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[ft.Text("ceci est la page HOME",size=30),
            ft.ElevatedButton("Go to Next View", on_click=lambda e:self.go("/page_001"))
            ]
            )
                        
                       
            
