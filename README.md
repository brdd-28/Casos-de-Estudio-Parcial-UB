# Casos de Estudio - Parcial UB

Repositorio oficial que contiene la solución estructurada y completa de los casos de estudio y talleres prácticos requeridos para el primer parcial. Cada caso se encuentra organizado en su respectiva carpeta e incluye:
* **Análisis detallado** (Entradas, Procesos, Salidas, Variables).
* **Pseudocódigo estructurado**.
* **Diagramas lógicos / de flujo**.
* **Código fuente en Python** (`.py`).
* **Pruebas de escritorio** con datos de prueba reales.

---

## 📂 Índice de Casos de Estudio

### 1. [Caso de estudio 1: Control de ventas](./caso_1_control_ventas/)
* **Descripción:** Algoritmo para solicitar el número de empleados y sus ventas semanales, calculando el total, promedio, cantidad de empleados que superan la meta de $1.000.000 y la venta más alta.
* **Archivos:** [`README.md`](./caso_1_control_ventas/README.md) | [`control_ventas.py`](./caso_1_control_ventas/control_ventas.py)

### 2. [Caso de estudio 2: Control de inventario](./caso_2_control_inventario/)
* **Descripción:** Control de existencias de un producto durante 7 días, calculando total, promedio, día con mayor stock, conteo de días con inventario inferior a 20 unidades y alertas para inventarios menores a 10 unidades.
* **Archivos:** [`README.md`](./caso_2_control_inventario/README.md) | [`control_inventario.py`](./caso_2_control_inventario/control_inventario.py)

### 3. [Caso de estudio 3: Nómina de empleados](./caso_3_nomina_empleados/)
* **Descripción:** Cálculo de salario semanal para varios empleados, considerando horas normales y horas extras (con un recargo del 25% si superan las 40 horas), mostrando desgloses individuales y el total pagado por la organización.
* **Archivos:** [`README.md`](./caso_3_nomina_empleados/README.md) | [`nomina_empleados.py`](./caso_3_nomina_empleados/nomina_empleados.py)

### 4. [Caso de estudio 4: Atención al cliente](./caso_4_atencion_cliente/)
* **Descripción:** Registro y análisis de atención al cliente de 5 trabajadores utilizando simultáneamente variables, estructuras condicionales `SI-SINO`, bucles `PARA`, contadores y acumuladores.
* **Archivos:** [`README.md`](./caso_4_atencion_cliente/README.md) | [`atencion_cliente.py`](./caso_4_atencion_cliente/atencion_cliente.py)

### 5. [Caso de estudio 5: Control de calidad](./caso_5_control_calidad/)
* **Descripción:** Inspección de 10 productos fabricados (1 = aprobado, 0 = defectuoso) determinando totales, porcentajes de defectos y generando alertas críticas si el porcentaje supera el 10%.
* **Archivos:** [`README.md`](./caso_5_control_calidad/README.md) | [`control_calidad.py`](./caso_5_control_calidad/control_calidad.py)

### 6. [Caso de estudio 6: Taller práctico de codificación](./caso_6_taller_practico/)
* **Descripción:** Conversión de pseudocódigo secuencial e iterativo a código Python ejecutable con validación de metas de ventas.
* **Archivos:** [`README.md`](./caso_6_taller_practico/README.md) | [`taller_practico.py`](./caso_6_taller_practico/taller_practico.py)

---

## 🚀 Instrucciones de Ejecución

Para ejecutar cualquiera de los scripts en Python desde la terminal:

```bash
python3 caso_1_control_ventas/control_ventas.py
python3 caso_2_control_inventario/control_inventario.py
python3 caso_3_nomina_empleados/nomina_empleados.py
python3 caso_4_atencion_cliente/atencion_cliente.py
python3 caso_5_control_calidad/control_calidad.py
python3 caso_6_taller_practico/taller_practico.py
```

---
*Fecha de entrega final (en físico y plataforma): **18 de Agosto**.*
