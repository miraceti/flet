import flet as ft
import flet_route
from flet_route import Params, Basket

def home(page: ft.Page, params: Params, basket: Basket):
    
    
    return ft.View(
        "/",

        controls = [

            ft.Text("This is the Home view"),
            ft.ElevatedButton("Go to page1", on_click= lambda _: page.go("/page1/10")),
            ft.ElevatedButton("Go to page2", on_click= lambda _: page.go("/page2/FletApp")),
        ]
    )