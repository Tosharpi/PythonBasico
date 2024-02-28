#categorias
categorias_Dict= {
    
    "MenuDulce":{
        "Panettone":1500,
        "Rosca de reyes":2000,
        "Concha":2500,
        "Trenza de chocolate":3000,
        "Donas":3500,
        "Croissant":4000,
        "Bollo de canela":4500,
        "Eclair":5000,
        "Ensaimada":5500,
        "Cinnamon roll":6000,
        },

    "MenuSalado":{
        "Baguette":6500,
        "Pan de ajo":7000,
        "Focaccia":7500,
        "Pretzel":8000,
        "Pan de centeno":8500,
        "Bollo de queso":9000,
        "Pan de papa":9500,
        "Bolillo":10000,
        "Pan de maíz":10500,
        "Chapata":11000,
    },
    "MenuPostre":{
        "Tiramisú":11500,
        "Cheesecake de fresa":12000,
        "Coulant de chocolate":12500,
        "Crème brûlée":13000,
        "Helado de vainilla con salsa de chocolate":13500,
        "Tarta de manzana":14000,
        "Mousse de limón":14500,
        "Profiteroles rellenos de crema":15000,
        "Flan de caramelo":15500,
        "Pastel de tres leches":16000
    },
    "Descuentos":{
        "Trenza de chocolate":{"Descuento del 20%":0.80},
        "Donas":{"descuento del 20%":0.80},
        "Baguette":{"descuento del 10%":0.90},
        "Pan de ajo":{"descuento del 10%":0.90},
        "Flan de caramelo":{"descuento del 30%":0.70},
        "Pastel de tres leches":{"descuento del 30%":0.70},
    }
}

print('Bienvenido a panaderia Los Panes')

print('contamos con tres menús: '.center(50,"="))

for i, val in enumerate(categorias_Dict):
    if i != 3:
        print(f"""{i}. {val} """)

codCat=input('Ingrese el codigo de la categoria: ')
print(codCat)
print(categorias_Dict.keys())
if codCat in categorias_Dict.keys():
    print(codCat)