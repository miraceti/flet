import flet as ft
from flet import Page, Column, Text, TextField, ElevatedButton
import requests
import json


def main(page: ft.Page):
    #page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    page.title = "Web Scrapper"

    url1 = "https://66519df220f4f4c4427831b4.mockapi.io/users"

    url_field = TextField(value=url1, hint_text="URL", text_align="left", autofocus=True)
    result_txt = Text(value="", text_align="left")


    def scrape(e):
        url = url_field.value
        url_field.value=""

        response = requests.get(url)
        json_data = json.loads(response.text)

        names = [item["name"] for item in json_data]

        result_txt.value = "\n".join(names)

        page.update()

    page.add(
        Column(
            [
                url_field,
                ElevatedButton(text="Scrape", on_click=scrape),
                ft.Divider(),
                result_txt,
            ]

        )
    )


ft.app(main)
