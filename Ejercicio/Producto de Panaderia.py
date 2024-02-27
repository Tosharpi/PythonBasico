#hacer un menu que tenga una categoria y dependiendo esa categoria 
#muesytre los productos
#por ejemplo, postres : genobesa, roscones, gelatina, nose
#cuantos desea? y promociones
#diga los productos seleccionados y haga el pago

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

print('Bienvenido a panaderia Los Panes')
print('contamos con tres menús: ')
print(
    """       0. Menú Dulce 
       1. Menú Postres 
       2. Menú Salado""")

catMenú = int(input('¿Que menú desea ver? '))

if catMenú == 0:
    for numProductDulce, nomProductoDulce in enumerate(MenuDulce):
        print(f""" {numProductDulce}. {MenuDulce[numProductDulce]} ${MenuDulcePrecio[numProductDulce]}""")

        decision = input('¿Que producto desea llevar?')
        print(f"""Seleccionó el producto  {numProductDulce[decision]} 
        cuyo valor es ${MenuDulcePrecio[decision]}""")

elif catMenú == 2 :
    for numProductSalado, nomProductoSalado in enumerate(MenuSalado):
        print(f""" {numProductSalado}. {MenuDulce[numProductSalado]} ${MenuSaladoPrecio[numProductSalado]}""")

elif catMenú == 1 :
    for numProductPostre, nomProductoPostre in enumerate(MenuPostre):
        print(f""" {numProductPostre}. {MenuPostre[numProductPostre]} ${MenuPostrePrecio[numProductPostre]}""")
