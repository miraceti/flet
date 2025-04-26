import flet as ft

def main(page:ft.Page):
    page.title=" My first page"
    page.add(ft.Text("ici la première page"))

ft.app(target=main)
