from flet import *
from flet_route import Params, Basket
from .navcom import bar_item

class About(UserControl):
    def __init__(self):
        super().__init__()

    def view(self, page:Page,params:Params,basket:Basket):
        return View(
            controls=[
                Text("About", size=30, weight="bold"),
                bar_item(page)
            ]

        )