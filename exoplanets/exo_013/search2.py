import flet as ft
from flet import *

def main (page: Page):
    page.window_width= 300

    you_select = Row([])

    animal_list = [
        {"name":"dog","like":20, "type":"a"},   {"name":"cat","like":30,"type":"a"},        
        {"name":"pig","like":40,"type":"a"},        {"name":"bird","like":50, "type":"a"},        
        {"name":"snake","like":60, "type":"a"},        {"name":"rabit","like":70, "type":"a"},
        {"name":"lion","like":80, "type":"a"},        {"name":"zebra","like":90, "type":"a"},
        {"name":"tiger","like":10, "type":"a"},

    ]

    def resultselect(e):
        you_select.controls.clear()
        you_select.controls.append(
            Row([
                Text(e.control.title.value, size=25),
                Text(e.control.subtitle.value, size=25),
            ])
        )
        page.update()

    def find_animal(e):
        print(e.control.value)

        search_text = e.control.value.lower()
        ct_search.content.controls.clear()

        found=False
        for animal in animal_list:
            if search_text in animal['name'].lower():
                ct_search.content.controls.append(
                    ListTile(
                        title=Text(animal['name'], size=25, color="green"),
                        subtitle=Text(str(animal['like'])+str(animal['type']), size=15, color="blue"),
                        on_click=resultselect
                    )
                )
                found=True

            if not found:
                ct_search.content.controls.append(
                    Text("data not found", size=30, weight="bold")
                )

            if e.control.value !="":
                ct_search.visible = True
            else:
                ct_search.visible = False

            page.update()


    ct_input = TextField(label="Search planet", on_change=find_animal)

    ct_search = Container(
        visible = False,
        bgcolor="yellow400",
        width=350,
        padding=10,
        content=Column()
    )

    page.add(
        Column([
            ct_input,
            ct_search,
            Row([
                Text("Result your select", size=30),
                you_select
            ])

        ])
    )

ft.app(target=main)