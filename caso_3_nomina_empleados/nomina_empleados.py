print("==================================================")
print("          SISTEMA DE NÓMINA DE EMPLEADOS          ")
print("==================================================\n")

n = int(input("Ingrese el número de empleados a procesar: "))

total_empresa = 0.0

for i in range(1, n + 1):
    print("\n" + "-" * 50)
    print(f"               DATOS DEL EMPLEADO {i}             ")
    print("-" * 50)
    nombre = input(" Nombre del empleado : ")
    horas_trabajadas = float(input(" Horas trabajadas    : "))
    valor_hora = float(input(" Valor de la hora ($): "))
    
    # Cálculo de horas normales y extras
    if horas_trabajadas <= 40:
        horas_normales = horas_trabajadas
        horas_extras = 0.0
    else:
        horas_normales = 40.0
        horas_extras = horas_trabajadas - 40.0
        
    # Cálculos de pago
    salario_normal = horas_normales * valor_hora
    pago_extras = horas_extras * (valor_hora * 1.25)
    salario_total = salario_normal + pago_extras
    
    # Acumular total pagado por la empresa
    total_empresa = total_empresa + salario_total
    
    # Mostrar resultados individuales
    print("\n" + "-" * 50)
    print(f"       REPORTE SALARIAL: {nombre.upper()}       ")
    print("-" * 50)
    print(f" Horas normales trabajadas : {horas_normales}")
    print(f" Horas extras realizadas   : {horas_extras}")
    print(f" Pago por horas normales   : ${salario_normal:,.2f}")
    print(f" Pago por horas extras     : ${pago_extras:,.2f}")
    print(f" Salario total a pagar     : ${salario_total:,.2f}")
    print("-" * 50)

print("\n" + "=" * 50)
print("              RESUMEN FINANCIERO EMPRESA          ")
print("==================================================")
print(f" Total pagado por la empresa : ${total_empresa:,.2f}")
print("==================================================")
