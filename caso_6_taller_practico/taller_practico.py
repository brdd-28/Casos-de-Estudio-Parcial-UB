CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}         TALLER PRÁCTICO DE CODIFICACIÓN          {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}\n")

cantidad = int(input(f"{YELLOW}Ingrese la cantidad de ventas a procesar: {RESET}"))
print(f"{CYAN}{'-' * 50}{RESET}")

total = 0.0

for contador in range(1, cantidad + 1):
    venta = float(input(f"{YELLOW}Ingrese la venta {contador}: ${RESET}"))
    total = total + venta
    
    if venta >= 1000000:
        print(f"  {GREEN}-> Meta alcanzada{RESET}")
    else:
        print(f"  {YELLOW}-> Meta no alcanzada{RESET}")
        
if cantidad > 0:
    promedio = total / cantidad
else:
    promedio = 0.0

print(f"\n{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}             RESULTADOS FINALES                   {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
print(f" Total general de ventas : {GREEN}${total:,.2f}{RESET}")
print(f" Promedio de ventas      : {GREEN}${promedio:,.2f}{RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
