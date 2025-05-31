import flet as ft
from fletx import Xapp, route
from views.home_view import HomeView
from views.page_001 import page_001
from views.page_002 import page_002
from views.page_003 import page_003
from views.page_004 import page_004
from views.page_005 import page_005
from views.page_006 import page_006
from views.page_007 import page_007
from views.page_008 import page_008
from views.page_009 import page_009
from views.page_010 import page_010


def main(page:ft.Page):
    page.title=" EXOPLANETES  -  INFORMATIONS"
     # Icône personnalisée
    page.window.icon = "/assets/icon.png"  # Chemin vers ton icône personnalisée

    Xapp(
        page=page,
        routes=[
            route(route="/", view=HomeView),
            route(route="/page_001", view=page_001),
            route(route="/page_002", view=page_002),
            route(route="/page_003", view=page_003),
            route(route="/page_004", view=page_004),
            route(route="/page_005", view=page_005),
            route(route="/page_006", view=page_006),
            route(route="/page_007", view=page_007),
            route(route="/page_008", view=page_008),
            route(route="/page_009", view=page_009),
            route(route="/page_010", view=page_010),
            # route(route="/page_011", view=page_002),
            # route(route="/page_012", view=page_003),
        ]
    )
    

ft.app(target=main,assets_dir="assets")
