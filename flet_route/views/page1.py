import flet as ft
from flet_route import Params, Basket

def page1(page: ft.Page, params:Params, basket:Basket):

    return ft.View(

        "/page1/:my_id",

        controls = [

            ft.Text("This is the page 1 view"),
            ft.ElevatedButton(" Go back to Home page", on_click= lambda _: page.go("/"))
        ]
    )