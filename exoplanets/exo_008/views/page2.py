import flet as ft
import flet_route
from flet_route import Params, Basket

def page2(page: ft.Page, params:Params, basket:Basket):

    return ft.View(

        "/page2/:name",

        controls = [

            ft.Text("This is the page 2 view"),
            ft.ElevatedButton(" Go back to Home page", on_click= lambda _: page.go("/"))
        ]
    )