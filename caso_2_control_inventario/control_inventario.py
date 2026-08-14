CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}      SISTEMA DE CONTROL DE INVENTARIO (7 DÍAS)   {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}\n")

total_unidades = 0
cont_inferior_20 = 0
mayor_cantidad = 0
dia_mayor = 0

for dia in range(1, 8):
    cantidad = int(input(f"{YELLOW}Ingrese la cantidad de productos disponibles el día {dia}: {RESET}"))
    
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
        print(f" {RED}>> ALERTA: Stock crítico el día {dia} ({cantidad} unidades){RESET}")

# Calcular promedio
promedio = total_unidades / 7

# Mostrar resultados
print(f"\n{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}           INFORME DE CONTROL DE INVENTARIO       {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
print(f" Total de unidades registradas    : {GREEN}{total_unidades}{RESET}")
print(f" Promedio de unidades por día     : {GREEN}{promedio:,.2f}{RESET}")
print(f" Día con mayor stock              : {GREEN}Día {dia_mayor} ({mayor_cantidad} unidades){RESET}")
print(f" Días con inventario menor a 20   : {YELLOW}{cont_inferior_20}{RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
