import flet as ft

def main(page: ft.Page):
    col1=str("col1")
    col2=str("col2")
    col3=str("col3")
    page.add(
        ft.DataTable(
            width=280,
            bgcolor="yellow",
            heading_row_height=20,
            heading_row_color="#5e0b66",
            data_row_min_height=35,
            data_row_max_height=35,
            data_row_color =({"hovered":"0x30FF0000"}),
            border_radius=30,
            columns=[
                ft.DataColumn(ft.Text(str(col1),
                                        color="yellow",
                                        weight="bold")),
                ft.DataColumn(ft.Text(str(col2),
                                        color="yellow",
                                        weight="bold",
                                        )),
                ft.DataColumn(ft.Text(str(col3),
                                        color="yellow",
                                        weight="bold"
                                        )),
                                        
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cel11")),
                        ft.DataCell(ft.Text("cel12")),
                        ft.DataCell(ft.Text("cel13")), 
                        # ft.DataCell(ft.Text("cel14")),                                                             
                    ],   
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cel21")),
                        ft.DataCell(ft.Text("cel22")),
                        ft.DataCell(ft.Text("cel23")), 
                        # ft.DataCell(ft.Text("cel24")),                                                             
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cel31")),
                        ft.DataCell(ft.Text("cel32")),
                        ft.DataCell(ft.Text("cel33")), 
                    #    ft.DataCell(ft.Text("cel43")),                                                             
                    ],
                ),    
            ],

        )
    )
    
ft.app(target=main)