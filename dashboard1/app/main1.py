import flet as ft

style_frame: dict = {
    "expand": True,
    "bgcolor": "#1f2128",
    "border_radius": 10,
    "padding": 20,
}

class GraphOne(ft.Container):
    def __init__(self):
        super().__init__(**style_frame)
        


graph_one: ft.Container = GraphOne()

def main(page: ft.Page):
    #page.add(ft.SafeArea(ft.Text("Hello, Flet Dashboard!")))
    page.bgcolor = 'black'
    page.padding = 10
    page.add(
        ft.Row(
            expand= True,
            height= 5.0,
            controls=[
            ft.Column(
                expand= True,
                controls=[graph_one],

            ),
            ft.Column(
                expand= True,
                controls=[graph_one],

            )
              
            ]
        ),
        ft.Row(
            expand= True,
            height= 5.0,
            controls=[
            ft.Column(
                expand= True,
                controls=[graph_one],

            ),
            ft.Column(
                expand= True,
                controls=[graph_one],

            )
              
            ]
        )
        
    )

    



ft.app(target=main)
