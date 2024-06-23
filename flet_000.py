import flet as ft

def main(page: ft.Page):
    page.title = "Mon aplli"
    
    def quand_clic(e):
        label.value = "TU AS CLIQUE !!"
        page.update()

    label = ft.Text('BONJOUR')
    bouton = ft.ElevatedButton('APPUYER ICI !')
    bouton.on_click = quand_clic
    
    page.add(label, bouton)
    

ft.app(target=main)