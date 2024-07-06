import flet as ft

def main(page: ft.Page):
    wv = ft.WebView(
        "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+count(pl_name)+from+ps+where+default_flag=1&format=json",
        expand=True,
        on_page_started=lambda _: print("Page started"),
        on_page_ended=lambda _: print("Page ended"),
        on_web_resource_error=lambda e: print("Page error:", e.data),
    )
    page.add(wv)

ft.app(main)