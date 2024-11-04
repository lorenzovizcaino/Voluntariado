import flet as ft
from datetime import datetime, timedelta

def main(page: ft.Page):
    
    page.window_maximized = True  

    # Fecha actual y cálculo del próximo mes
    today = datetime.now()
    next_month = today.replace(day=1) + timedelta(days=32)
    next_month = next_month.replace(day=1)  # Primer día del próximo mes
    
    
    calendar_header = ft.Text(f"{next_month.strftime('%B %Y')}", weight="bold", size=30)

    
    days_of_week = ["L", "M", "X", "J", "V", "S", "D"]
    turnos = ["ND", "T1", "T2", "T3", "T4"]
    header_row = ft.Row([
                        ft.Text(day, 
                                weight="bold", 
                                size=35, 
                                width=20 * 5 + 8,
                                text_align=ft.TextAlign.CENTER,
                                ) for day in days_of_week], 
                        alignment="center")

    
    days_grid = []
    
    # Obtener el primer día de la cuadrícula (inicio en el domingo más cercano al primer día del mes)
    first_day = next_month
    start_day = first_day - timedelta(days=first_day.weekday() % 7)

    def modificar_tabla(e):
        
        print(e.control.key["ch"])
        print(e.control.key["current_day"])

    # Generar las filas de días del calendario
    for week in range(6):  # Hasta 6 filas para cubrir todos los días
        row = []
        for day in range(7):  # 7 días en una semana
            current_day = start_day + timedelta(days=week * 7 + day)

            turnos_row =ft.Row(
                [ft.Text(value=f"{turno}",  width=20, height=20, size=13) for turno in turnos] if current_day.month == next_month.month else "",
                alignment="center",
                spacing=3, 
                
            )

            

            
            checkboxes = []            
            if current_day.month == next_month.month:  
                year=current_day.year
                month=current_day.month
                day=current_day.day
                              
                for ch in range(5):
                    #hacer consulta a la base de datos para cargar los datos
                    checkboxes.append(ft.Checkbox(label="", width=20, key={"ch":ch,"current_day":current_day},height=20, on_change=modificar_tabla))        
            checkboxes_row = ft.Row(
                checkboxes,        
                alignment="center", 
                spacing=2          
            )               
            
            
           

                        
            
            day_text = ft.Text(
                str(current_day.day) if current_day.month == next_month.month else "",
                text_align=ft.TextAlign.CENTER,
                width=20 * 5 + 8,  # 5 casillas de 20 px + 2 px de espacio entre cada una
                size=35
            )
            
            
            day_cell = ft.Column(
                [
                    day_text,
                    turnos_row,
                    checkboxes_row
                ],
                spacing=5,
                alignment="center"
            )
            
            row.append(day_cell)
        days_grid.append(ft.Row(row, alignment="center"))

    
    page.add(
        ft.Column(
            [
                calendar_header,
                header_row,
                *days_grid,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Ejecutar la app de Flet
ft.app(target=main)
