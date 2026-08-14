CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}          SISTEMA DE CONTROL DE CALIDAD           {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}\n")

total_aprobados = 0
total_defectuosos = 0
total_inspeccionados = 10

for i in range(1, total_inspeccionados + 1):
    print(f"{CYAN}{'-' * 50}{RESET}")
    print(f"{BOLD} Inspección Producto {i} de {total_inspeccionados}{RESET}")
    print(f"{CYAN}{'-' * 50}{RESET}")
    codigo = input(f"{YELLOW} Código del producto : {RESET}")
    resultado = int(input(f"{YELLOW} Resultado (1=Aprobado, 0=Defectuoso): {RESET}"))
            
    if resultado == 1:
        total_aprobados = total_aprobados + 1
        print(f"  {GREEN}✔ Producto Aprobado{RESET}")
    else:
        total_defectuosos = total_defectuosos + 1
        print(f"  {RED}✖ Producto Defectuoso{RESET}")
        
# Calcular porcentaje de defectuosos
porcentaje_defectuosos = (total_defectuosos / total_inspeccionados) * 100.0

# Mostrar informe
print(f"\n{CYAN}{'=' * 50}{RESET}")
print(f"{BOLD}{BLUE}       INFORME FINAL DE CONTROL DE CALIDAD        {RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
print(f" Total de productos inspeccionados : {total_inspeccionados}")
print(f" Total de productos aprobados      : {GREEN}{total_aprobados}{RESET}")
print(f" Total de productos defectuosos    : {RED}{total_defectuosos}{RESET}")
print(f" Porcentaje de defectuosos         : {YELLOW}{porcentaje_defectuosos:.2f}%{RESET}")
print(f"{CYAN}{'-' * 50}{RESET}")

# Evaluación de estado / alerta
if porcentaje_defectuosos > 10:
    print(f" {RED}>> ALERTA: Revisar proceso de producción{RESET}")
else:
    print(f" {GREEN}>> PROCESO: Dentro del nivel permitido{RESET}")
print(f"{CYAN}{'=' * 50}{RESET}")
