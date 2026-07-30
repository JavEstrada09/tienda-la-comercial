# -*- coding: utf-8 -*-
"""
Programa de cálculo de comisiones de La Comercial.
Calcula la comisión y el bono mensual de cada vendedor.
"""

LIMITE_COMISION_ALTA = 30000
LIMITE_BONO = 50000

COMISION_BAJA = 0.05
COMISION_ALTA = 0.08
BONO = 500

VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(ventas):
    """Calcula la comisión según el monto vendido."""
    if ventas > LIMITE_COMISION_ALTA:
        return round(ventas * COMISION_ALTA, 2)

    return round(ventas * COMISION_BAJA, 2)


def calcular_bono(ventas):
    """Determina si el vendedor recibe bono."""
    if ventas > LIMITE_BONO:
        return BONO

    return 0


def imprimir_reporte(vendedores):
    """Imprime el reporte de comisiones del mes."""
    total_pagar = 0

    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)

    for nombre, ventas in vendedores:
        comision = calcular_comision(ventas)
        bono = calcular_bono(ventas)

        total = round(comision + bono, 2)
        total_pagar += total

        print(f"{nombre}: Q {total:.2f}")

    print("-" * 44)
    print(f"Total a pagar: Q {total_pagar:.2f}")


def procesar_comisiones():
    """Punto de entrada del programa."""
    imprimir_reporte(VENDEDORES)


if __name__ == "__main__":
    procesar_comisiones()