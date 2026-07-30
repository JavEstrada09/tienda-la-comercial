# -*- coding: utf-8 -*-
"""
Programa de cierre de caja de La Comercial.
Calcula ventas por método de pago, IVA, comisión POS y depósito neto.
"""

IVA = 0.12
COMISION_POS = 0.05

VENTAS_DIA = [
    ("EF", 150.00),
    ("TJ", 89.50),
    ("EF", 45.25),
    ("TJ", 210.00),
    ("EF", 78.00),
    ("TJ", 156.75),
    ("EF", 92.50),
    ("EF", 34.00),
    ("TJ", 67.25),
    ("EF", 125.00),
]
def calcular_totales(ventas):
    total_efectivo = 0
    total_tarjeta = 0

    for metodo_pago, monto in ventas:
        if metodo_pago == "EF":
            total_efectivo += monto
        else:
            total_tarjeta += monto

    return total_efectivo, total_tarjeta


def calcular_iva(monto):
    return round(monto - (monto / (1 + IVA)), 2)


def calcular_comision(total_tarjeta):
    return round(total_tarjeta * COMISION_POS, 2)


def imprimir_reporte(total_efectivo, total_tarjeta, iva_efectivo,
                      iva_tarjeta, comision):
    total_dia = total_efectivo + total_tarjeta
    deposito_neto = total_dia - comision

    print("=" * 42)
    print("      CIERRE DE CAJA - LA COMERCIAL")
    print("=" * 42)
    print(f"Ventas en efectivo:      Q {total_efectivo:.2f}")
    print(f"IVA incluido (efectivo): Q {iva_efectivo:.2f}")
    print(f"Ventas con tarjeta:      Q {total_tarjeta:.2f}")
    print(f"IVA incluido (tarjeta):  Q {iva_tarjeta:.2f}")
    print(f"Comisión del POS:        Q {comision:.2f}")
    print("-" * 42)
    print(f"Total del día:           Q {total_dia:.2f}")
    print(f"Depósito neto:           Q {deposito_neto:.2f}")


def procesar_cierre_caja():
    total_efectivo, total_tarjeta = calcular_totales(VENTAS_DIA)

    iva_efectivo = calcular_iva(total_efectivo)
    iva_tarjeta = calcular_iva(total_tarjeta)

    comision = calcular_comision(total_tarjeta)

    imprimir_reporte(
        total_efectivo,
        total_tarjeta,
        iva_efectivo,
        iva_tarjeta,
        comision
    )


if __name__ == "__main__":
    procesar_cierre_caja()