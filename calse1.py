productos = tuple(('Coca Cola', 'Pepsi Cola'))
productos = list(productos)
productos.append('Colombiana')
productos.insert(1, 'Ponymalta')
productos = tuple((productos))
print(productos)
print(productos.count('Colombiana'), 'colombiana/s')
#