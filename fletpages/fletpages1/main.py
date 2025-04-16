import flet as ft
from fletx import Xapp, route
from views.home_view import HomeView
from views.next_view import NextView
from views.page_001 import page_001
from views.page_002 import page_002
from views.page_003 import page_003

def main(page:ft.Page):
    page.title=" FletX Routing Example"

    Xapp(
        page=page,
        routes=[
            route(route="/", view=HomeView),
            route(route="/page_001", view=page_001),
            route(route="/page_002", view=page_002),
            route(route="/page_003", view=page_003),
        ]
    )
    

ft.app(target=main)
