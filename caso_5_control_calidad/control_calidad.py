print("==================================================")
print("          SISTEMA DE CONTROL DE CALIDAD           ")
print("==================================================\n")

total_aprobados = 0
total_defectuosos = 0
total_inspeccionados = 10

for i in range(1, total_inspeccionados + 1):
    print("-" * 50)
    print(f" Inspección Producto {i} de {total_inspeccionados}")
    print("-" * 50)
    codigo = input(" Código del producto : ")
    resultado = int(input(" Resultado (1=Aprobado, 0=Defectuoso): "))
            
    if resultado == 1:
        total_aprobados = total_aprobados + 1
    else:
        total_defectuosos = total_defectuosos + 1
        
# Calcular porcentaje de defectuosos
porcentaje_defectuosos = (total_defectuosos / total_inspeccionados) * 100.0

# Mostrar informe
print("\n" + "=" * 50)
print("       INFORME FINAL DE CONTROL DE CALIDAD        ")
print("==================================================")
print(f" Total de productos inspeccionados : {total_inspeccionados}")
print(f" Total de productos aprobados      : {total_aprobados}")
print(f" Total de productos defectuosos    : {total_defectuosos}")
print(f" Porcentaje de defectuosos         : {porcentaje_defectuosos:.2f}%")
print("-" * 50)

# Evaluación de estado / alerta
if porcentaje_defectuosos > 10:
    print(" >> ALERTA: Revisar proceso de producción")
else:
    print(" >> PROCESO: Dentro del nivel permitido")
print("==================================================")
