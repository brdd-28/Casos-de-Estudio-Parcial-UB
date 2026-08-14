CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}       SISTEMA DE CONTROL DE VENTAS SEMANAL       {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}\n")

n = int(input(f"{YELLOW}Ingrese el número de empleados a procesar: {RESET}"))
print(f"{CYAN}{'-' * 50}{RESET}")

total_ventas = 0.0
cont_meta = 0
venta_mayor = 0.0

for i in range(1, n + 1):
    venta = float(input(f"{YELLOW}Ingrese el valor de las ventas del empleado {i}: ${RESET}"))
    
    # Acumular total de ventas
    total_ventas = total_ventas + venta
    
    # Determinar empleados que superan la meta de $1.000.000
    if venta > 1000000:
        cont_meta = cont_meta + 1
        print(f"  {GREEN}✔ ¡Meta superada ($1.000.000)!{RESET}")
        
    # Determinar la venta más alta
    if i == 1 or venta > venta_mayor:
        venta_mayor = venta

# Calcular promedio
if n > 0:
    promedio = total_ventas / n
else:
    promedio = 0.0

# Mostrar resultados
print(f"\n{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}           RESULTADOS FINALES DE VENTAS           {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
print(f" Total de ventas            : {GREEN}${total_ventas:,.2f}{RESET}")
print(f" Promedio de ventas         : {GREEN}${promedio:,.2f}{RESET}")
print(f" Empleados que superan meta : {YELLOW}{cont_meta}{RESET}")
print(f" Venta más alta             : {GREEN}${venta_mayor:,.2f}{RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
