print("==================================================")
print("     SISTEMA DE CONTROL DE ATENCIÓN AL CLIENTE    ")
print("==================================================\n")

# Acumuladores, contadores y variables
total_clientes = 0
mayor_atenciones = 0
trabajador_estrella = 1
cont_mas_30 = 0
cont_menos_15 = 0

for i in range(1, 6):
    clientes = int(input(f"Ingrese la cantidad de clientes atendidos por el Trabajador {i}: "))
    
    # Acumulador
    total_clientes = total_clientes + clientes
    
    # Determinar mayor número de atenciones
    if i == 1 or clientes > mayor_atenciones:
        mayor_atenciones = clientes
        trabajador_estrella = i
        
    # Estructura SI-SINO y Contadores
    if clientes > 30:
        cont_mas_30 = cont_mas_30 + 1
    elif clientes < 15:
        cont_menos_15 = cont_menos_15 + 1
        
# Calcular promedio
promedio = total_clientes / 5

# Resultados
print("\n" + "=" * 50)
print("       REPORTE DE ATENCIÓN AL CLIENTE        ")
print("==================================================")
print(f" Total de clientes atendidos         : {total_clientes}")
print(f" Promedio de atenciones por trabajador: {promedio:.2f}")
print(f" Trabajador con mayor atención       : Trabajador {trabajador_estrella} ({mayor_atenciones} clientes)")
print(f" Trabajadores con > 30 clientes      : {cont_mas_30}")
print(f" Trabajadores con < 15 clientes      : {cont_menos_15}")
print("==================================================")
