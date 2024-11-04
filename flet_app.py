import flet as ft


def main(page:ft.Page):
    page.title="Somos Voluntarios"
    page.theme_mode=ft.ThemeMode.LIGHT
    

    
    

    # Función para actualizar la vista según la ruta
    def cambiar_ruta(route):
        page.views.clear()  # Limpia las vistas actuales
        if page.route == "/login":
            page.views.append(login_user())
        elif page.route == "/new_user":
            page.views.append(new_user())
        elif page.route == "/admin":
            page.views.append(admin())
        page.update()

    #definimos la vista de login
    def login_user():
        
        def new_user(e):
            page.go("/new_user")

        
        titulo=ft.Text(value="Inicio de sesion:", size=22,weight=ft.FontWeight.BOLD)
        usuario=ft.TextField(label="Usuario")
        password=ft.TextField(label="Contraseña")
        btn_logear=ft.FloatingActionButton("Login", on_click= new_user, bgcolor=ft.colors.GREEN_300,width=140,height=30)
        btn_new_user=ft.FloatingActionButton("Crear nuevo usuario", on_click= new_user, bgcolor=ft.colors.ORANGE_300,width=140,height=30)
        fila=ft.Row(controls=[btn_logear, btn_new_user])
        columna=ft.Column(controls=[titulo, usuario,password,fila], width=300)
        return ft.View("/login",
                       controls=[columna],
                       horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                       vertical_alignment=ft.MainAxisAlignment.CENTER)





    def new_user():
        page.title="Somos Voluntarios"
        titulo=ft.Text(value="Pagina newUser")

        return ft.View("/new_user",
                       controls=[titulo])




    def admin():
        pass

    page.on_route_change=cambiar_ruta
    page.go("/login")


if __name__ == "__main__":
    ft.app(target=main)