CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}     SISTEMA DE CONTROL DE ATENCIÓN AL CLIENTE    {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}\n")

# Acumuladores, contadores y variables
total_clientes = 0
mayor_atenciones = 0
trabajador_estrella = 1
cont_mas_30 = 0
cont_menos_15 = 0

for i in range(1, 6):
    clientes = int(input(f"{YELLOW}Ingrese la cantidad de clientes atendidos por el Trabajador {i}: {RESET}"))
    
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
print(f"\n{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}       REPORTE DE ATENCIÓN AL CLIENTE        {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
print(f" Total de clientes atendidos         : {GREEN}{total_clientes}{RESET}")
print(f" Promedio de atenciones por trabajador: {GREEN}{promedio:,.2f}{RESET}")
print(f" Trabajador con mayor atención       : {GREEN}Trabajador {trabajador_estrella} ({mayor_atenciones} clientes){RESET}")
print(f" Trabajadores con > 30 clientes      : {YELLOW}{cont_mas_30}{RESET}")
print(f" Trabajadores con < 15 clientes      : {RED}{cont_menos_15}{RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
