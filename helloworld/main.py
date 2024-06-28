from flet import *

def main(page:Page):
    page.add(

        SafeArea(
            content=Text("Hello from flet", size=30, color="white")
        )
    )

app(main)