print("==================================================")
print("       SISTEMA DE CONTROL DE VENTAS SEMANAL       ")
print("==================================================\n")

n = int(input("Ingrese el número de empleados a procesar: "))
print("-" * 50)

total_ventas = 0.0
cont_meta = 0
venta_mayor = 0.0

for i in range(1, n + 1):
    venta = float(input(f"Ingrese el valor de las ventas del empleado {i}: $"))
    
    # Acumular total de ventas
    total_ventas = total_ventas + venta
    
    # Determinar empleados que superan la meta de $1.000.000
    if venta > 1000000:
        cont_meta = cont_meta + 1
        
    # Determinar la venta más alta
    if i == 1 or venta > venta_mayor:
        venta_mayor = venta

# Calcular promedio
if n > 0:
    promedio = total_ventas / n
else:
    promedio = 0.0

# Mostrar resultados
print("\n" + "=" * 50)
print("           RESULTADOS FINALES DE VENTAS           ")
print("==================================================")
print(f" Total de ventas            : ${total_ventas:,.2f}")
print(f" Promedio de ventas         : ${promedio:,.2f}")
print(f" Empleados que superan meta : {cont_meta}")
print(f" Venta más alta             : ${venta_mayor:,.2f}")
print("==================================================")
