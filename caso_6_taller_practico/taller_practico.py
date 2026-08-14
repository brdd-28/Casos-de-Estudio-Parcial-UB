print("==================================================")
print("         TALLER PRÁCTICO DE CODIFICACIÓN          ")
print("==================================================\n")

cantidad = int(input("Ingrese la cantidad de ventas a procesar: "))
print("-" * 50)

total = 0.0

for contador in range(1, cantidad + 1):
    venta = float(input(f"Ingrese la venta {contador}: $"))
    total = total + venta
    
    if venta >= 1000000:
        print("  -> Meta alcanzada")
    else:
        print("  -> Meta no alcanzada")
        
if cantidad > 0:
    promedio = total / cantidad
else:
    promedio = 0.0

print("\n" + "=" * 50)
print("             RESULTADOS FINALES                   ")
print("==================================================")
print(f" Total general de ventas : ${total:,.2f}")
print(f" Promedio de ventas      : ${promedio:,.2f}")
print("==================================================")
