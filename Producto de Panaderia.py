#hacer un menu que tenga una categoria y dependiendo esa categoria 
#muesytre los productos
#por ejemplo, postres : genobesa, roscones, gelatina, nose
#cuantos desea? y promociones
#diga los productos seleccionados y haga el pago
#[]-
# Tupla de panes dulces

MenuDulce = (
    "Panettone",
    "Rosca de reyes",
    "Concha",
    "Trenza de chocolate",
    "Donas",
    "Croissant",
    "Bollo de canela",
    "Eclair",
    "Ensaimada",
    "Cinnamon roll"
)
MenuDulcePrecio = (1500, 2000, 2500, 3000, 3500,
    4000, 4500, 5000, 5500, 6000)

# Tupla de panes salados

MenuSalado = (
    "Baguette",
    "Pan de ajo",
    "Focaccia",
    "Pretzel",
    "Pan de centeno",
    "Bollo de queso",
    "Pan de papa",
    "Bolillo",
    "Pan de maíz",
    "Chapata"
)
MenuSaladoPrecio = (6500, 7000, 7500, 8000, 8500,
    9000, 9500, 10000, 10500, 11000)
#tupla de los postres

MenuPostre = (
    "Tiramisú",
    "Cheesecake de fresa",
    "Coulant de chocolate",
    "Crème brûlée",
    "Helado de vainilla con salsa de chocolate",
    "Tarta de manzana",
    "Mousse de limón",
    "Profiteroles rellenos de crema",
    "Flan de caramelo",
    "Pastel de tres leches"
)
MenuPostrePrecio = (11500, 12000, 12500, 13000, 13500,
    14000, 14500, 15000, 15500, 16000)

MenuDescuentos = (
    "Tiramisú: 2 o más unidades por un descuento del 5","%","en el precio final",
    "Crème brûlée Tiramisú: 2 o más unidades por un descuento del 10","%","en el precio final",
    "Focaccia Tiramisú: 2 o más unidades por un descuento del 15","%","en el precio final",
    "Pretzel Tiramisú: 2 o más unidades por un descuento del 20","%","en el precio final",
    "Eclair Tiramisú: 2 o más unidades por un descuento del 25","%","en el precio final",
)

MenuDescuentosPorcentaje = (
    0.05,
    0.10,
    0.15,
    0.20,
    0.25,
)

#descuentos
#pregDescuentos = input('¿Desea saber que descuentos tenemos hoy?')
#if pregDescuentos == 'si':
#    for numDesc, nomDesc in enumerate(MenuDescuentos):
#        print(f""" {numDesc}. {nomDesc} %{MenuDescuentosPorcentaje[numDesc]} de descuento""")
#    decisionDesc = input('¿deseas llevar algun producto con descuento?')
#    if decisionDesc == 'si':
#
#        codDesc = input('digite el codigo del descuento: ')
#
#        print(f"""El descuento seleccionado es: {MenuDescuentos[codDesc]} 
#        cuyo valor es ${MenuDescuentosPorcentaje[codDesc]}""")
#
#
#         deuda = 


print('Bienvenido a panaderia Los Panes')
print('contamos con tres menús: ')
print(
    """       0. Menú Dulce 
       1. Menú Postres 
       2. Menú Salado""")

catMenú = int(input('¿Que menú desea ver? '))

#el menu de productos dulces
if catMenú == 0:
    for numProductDulce, nomProductDulce in enumerate(MenuDulce):
        print(f""" {numProductDulce}. {nomProductDulce} ${MenuDulcePrecio[numProductDulce]}""")

    decision = int(input('¿Que producto desea llevar? digite su codigo: '))

    print('')

    print(f"""Seleccionó el producto  {MenuDulce[decision]} 
    cuyo valor es ${MenuDulcePrecio[decision]}""")

    cantidad = int(input('¿cuantas unidades desea llevar?'))
    deuda = cantidad * MenuDulcePecio[decirsion]
    print('La cantidad a pagar es: ', deuda)

    pago = int(input('introduzca la cantidad de dinero correspondiente a la deuda: '))
    control = 0

    while control == 0 :
    
        if pago < deuda :
            vueltos = pago - deuda
            print('La cantidad de dinero es insuficiente, faltan: ', vueltos)
            print('ingrese el dinero de nuevo: ')

        if pago > deuda :
            control = control + 1
            vueltos = pago - deuda
            print('Pago realizado, su cambio es: ', vueltos, 'pesos')

#el menu de productos salados
if catMenú == 2 :
    for numProductSalado, nomProductoSalado in enumerate(MenuSalado):
        print(f""" {numProductSalado}. {nomProductoSalado} ${MenuSaladoPrecio[numProductSalado]}""")

    decision = int(input('¿Que producto desea llevar? digite su codigo: '))
    
    print(f""" seleccionó el producto  {MenuSalado[decision]} 
    cuyo valor es ${MenuSaladoPrecio[decision]} """)

    cantidad = int(input('¿cuantas unidades desea llevar?'))
    deuda = cantidad * MenuSaladoPrecio[decision]
    print('La cantidad a pagar es: ', deuda)

    pago = int(input('introduzca la cantidad de dinero correspondiente a la deuda: '))
    control = 0

    while control == 0 :
    
        if pago < deuda :
            vueltos = pago - deuda
            print('La cantidad de dinero es insuficiente, faltan: ', vueltos)
            print('ingrese el dinero de nuevo: ')

        if pago > deuda :
            control = control + 1
            vueltos = pago - deuda
            print('Pago realizado, su cambio es: ', vueltos, 'pesos')

#el menu de productos tipo postres
if catMenú == 1 :
    for numProductPostre, nomProductoPostre in enumerate(MenuPostre):
        print(f""" {numProductPostre}. {nomProductoPostre} ${MenuPostrePrecio[numProductPostre]}""")

    decision = int(input('¿Que producto desea llevar? digite su codigo: '))

    print(f""" seleccionó el producto  {MenuPostre[decision]} cuyo valor es ${MenuPostrePrecio[decision]}""")
    #pago

    cantidad = int(input('¿cuantas unidades desea llevar?'))
    deuda = cantidad * MenuPostrePrecio[decision]
    print('La cantidad a pagar es: ', deuda)

    pago = int(input('introduzca la cantidad de dinero correspondiente a la deuda: '))
    control = 0

    while control == 0 :
    
        if pago < deuda :
            vueltos = pago - deuda
            print('La cantidad de dinero es insuficiente, faltan: ', vueltos)
            print('ingrese el dinero de nuevo: ')

        if pago > deuda :
            control = control + 1
            vueltos = pago - deuda
            print('Pago realizado, su cambio es: ', vueltos, 'pesos')