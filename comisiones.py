# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

LIMITE_COMISION_ALTA = 30000
LIMITE_BONO = 50000
COMISION_BAJA = 0.05
COMISION_ALTA = 0.08
BONO = 500

# lista de vendedores
VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]

def calcular_comisiones():
    total_pagar = 0

    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)

    # recorre la lista
    for vendedor in VENDEDORES:

        # si vendio mas de 30000
        if vendedor[1] > LIMITE_COMISION_ALTA:

            # calcula la comision del 8%
            comision = vendedor[1] * COMISION_ALTA
            comision = round(comision, 2)

            # el bono es de 300
            if vendedor[1] > LIMITE_BONO:
                bono = BONO
            else:
                bono = 0

            total = round(comision + bono, 2)
            total_pagar = total_pagar + total

            print(vendedor[0] + ": Q " + str(total))

        else:

            # calcula la comision del 5%
            comision = vendedor[1] * COMISION_BAJA
            comision = round(comision, 2)

            bono = 0

            total = round(comision + bono, 2)
            total_pagar = total_pagar + total

            print(vendedor[0] + ": Q " + str(total))

    # ta = tp * 1.12
    # print("con iva", ta)

    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))

calcular_comisiones()