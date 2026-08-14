CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}          SISTEMA DE NÓMINA DE EMPLEADOS          {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}\n")

n = int(input(f"{YELLOW}Ingrese el número de empleados a procesar: {RESET}"))

total_empresa = 0.0

for i in range(1, n + 1):
    print(f"\n{CYAN}{'-' * 50}{RESET}")
    print(f"{BOLD}{BLUE}               DATOS DEL EMPLEADO {i}             {RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")
    nombre = input(f"{YELLOW} Nombre del empleado : {RESET}")
    horas_trabajadas = float(input(f"{YELLOW} Horas trabajadas    : {RESET}"))
    valor_hora = float(input(f"{YELLOW} Valor de la hora ($): {RESET}"))
    
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
    print(f"\n{CYAN}{'-' * 50}{RESET}")
    print(f"{BOLD}{GREEN}       REPORTE SALARIAL: {nombre.upper()}       {RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")
    print(f" Horas normales trabajadas : {horas_normales}")
    print(f" Horas extras realizadas   : {YELLOW}{horas_extras}{RESET}")
    print(f" Pago por horas normales   : ${salario_normal:,.2f}")
    print(f" Pago por horas extras     : ${pago_extras:,.2f}")
    print(f" Salario total a pagar     : {GREEN}${salario_total:,.2f}{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")

print(f"\n{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}              RESUMEN FINANCIERO EMPRESA          {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
print(f" Total pagado por la empresa : {GREEN}${total_empresa:,.2f}{RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
