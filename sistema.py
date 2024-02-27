productos = tuple((
    "Coca-Cola", 
    "Pepsi", 
    "Sprite", 
    "Fanta", 
    "7UP", 
    "Mountain Dew", 
    "Dr Pepper", 
    "Schweppes", 
    "Mirinda", 
    "Lift"))
precios = tuple((
    4500, 
    3750, 
    3000, 
    3600, 
    5250, 
    6000, 
    5400, 
    3900, 
    4200, 
    4800))

for i, val in enumerate(productos):
    print(f"""   {i} {val} $ {precios[i]}""")

opcion = int(input())
print(f"""usuario usted selecciono el producto {productos[opcion]} 
      con un valor de ${precios[opcion]}""")

dinero = float(input('ingrese la cantidad de dinero disponible: '))
vueltos = dinero - precios[opcion] 

if dinero >= precios[opcion]:
    #vueltos = dinero - precios[opcion] 
    print(f"""usuario usted compro el prodcuto {productos[opcion]} con un valor de ${precios[opcion]}
           sus vueltos son ${vueltos}""")
else:
    print(f"""usuario el producto que desea comprar {productos[opcion]} con un valor de ${precios[opcion]}, le falta un total de ${-vueltos}""")
    #