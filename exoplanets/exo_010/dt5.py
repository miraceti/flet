import flet as ft

def main(page: ft.Page):
    def updateOnTap(e):
        e.control.content.value = "Hello Eric"
        page.update()

    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("prenom")),
                ft.DataColumn(ft.Text("Nom")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(
                            "John",
                            on_tap=updateOnTap
                            ),             
                        ),
                        ft.DataCell(
                            ft.Text(
                            "Smith",
                            ),             
                        ),
                    ],
                ),
            ],
        ),
    )

ft.app(target=main)