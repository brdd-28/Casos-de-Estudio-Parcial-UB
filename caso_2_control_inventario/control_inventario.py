print("==================================================")
print("      SISTEMA DE CONTROL DE INVENTARIO (7 DÍAS)   ")
print("==================================================\n")

total_unidades = 0
cont_inferior_20 = 0
mayor_cantidad = 0
dia_mayor = 0

for dia in range(1, 8):
    cantidad = int(input(f"Ingrese la cantidad de productos disponibles el día {dia}: "))
    
    # Acumular total
    total_unidades = total_unidades + cantidad
    
    # Identificar día con mayor cantidad
    if dia == 1 or cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        dia_mayor = dia
        
    # Contar días con inventario inferior a 20
    if cantidad < 20:
        cont_inferior_20 = cont_inferior_20 + 1
        
    # Generar alerta si inventario < 10
    if cantidad < 10:
        print(f" >> ALERTA: Stock crítico el día {dia} ({cantidad} unidades)")

# Calcular promedio
promedio = total_unidades / 7

# Mostrar resultados
print("\n" + "=" * 50)
print("           INFORME DE CONTROL DE INVENTARIO       ")
print("==================================================")
print(f" Total de unidades registradas    : {total_unidades}")
print(f" Promedio de unidades por día     : {promedio:,.2f}")
print(f" Día con mayor stock              : Día {dia_mayor} ({mayor_cantidad} unidades)")
print(f" Días con inventario menor a 20   : {cont_inferior_20}")
print("==================================================")
