import flet as ft
from datetime import datetime, timedelta

def main(page: ft.Page):
    # Fecha actual y cálculo del próximo mes
    today = datetime.now()
    next_month = today.replace(day=1) + timedelta(days=32)
    next_month = next_month.replace(day=1)  # Primer día del próximo mes
    
    # Encabezado con el mes y año siguiente
    calendar_header = ft.Text(f"{next_month.strftime('%B %Y')}", style="headlineMedium", weight="bold")

    # Días de la semana
    days_of_week = ["L", "M", "X", "J", "V", "S", "D"]
    header_row = ft.Row([ft.Text(day, weight="bold") for day in days_of_week], alignment="center")

    # Crear la grilla de días
    days_grid = []
    
    # Obtener el primer día de la cuadrícula (inicio de semana de `next_month`)
    first_day = next_month
    start_day = first_day - timedelta(days=first_day.weekday() + 1)

    # Generar las filas de días del calendario
    for week in range(6):  # Hasta 6 filas para cubrir todos los días
        row = []
        for day in range(7):  # 7 días en una semana
            current_day = start_day + timedelta(days=week * 7 + day)
            day_text = ft.Text(
                str(current_day.day) if current_day.month == next_month.month else "",
                text_align=ft.TextAlign.CENTER,
                width=40,
            )
            row.append(day_text)
        days_grid.append(ft.Row(row, alignment="center"))

    # Agregar los elementos al layout de la página
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
