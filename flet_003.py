import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Lottie(
            src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
            repeat=False,
            reverse=False,
            animate=True
        )
    )

ft.app(target=main)