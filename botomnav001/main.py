from flet import *
from flet_route import Routing, path
from pages.home import Home
from pages.about import About

def main(page: Page):
    page.window_width = 400

    theme = Theme()
    theme.page_transitions_linux = PageTransitionTheme.NONE
    page.theme = theme
    page.update()

    app_routes = [
        path(
            url="/",
            clear=True,
            view=Home().view
            ),
        path(
            url="/about",
            clear=True,
            view=About().view
            ),

    ]
    Routing(
        page=page,
        app_routes=app_routes
         )
    page.go(page.route)

    
app(target=main)