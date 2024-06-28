import flet as ft
from flet_route import Routing, path
from views.home import home
from views.page1 import page1
from views.page2 import page2



def main(page: ft.Page):
    
    # elm1 = ft.Text("Hello  World", color="green")
    # elm2 = ft.Text("On developpe une appli multipage", color="blue")

    # page.controls.append(elm1)
    # page.add(elm2)

    # page.update()

    app_routes=[

        path(url = "/", clear=True,  view=home),
        path(url="/page1/:my_id", clear=True,  view=page1),
        path(url="/page2/:name", clear=True,  view=page2),
    
    ]

    Routing(page=page, 
            app_routes=app_routes)
    
    page.go(page.route)

ft.app(target=main)