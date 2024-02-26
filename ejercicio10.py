#algoritmo para calcular el promedio de una lista de numeros 2.0

resp = input('¿quiere sacarle el promedio a una lista?')

if resp == 'si' or resp == 'sí' :
    cant = int(input('¿cuantos datos son?'))
    control = 1
    sumatoria = 0
    
while control <= cant :
    print('ingrese el valor del dato #',control) ; cantDat = float(input())
    sumatoria = sumatoria + cantDat
    control = control + 1
    promedio = sumatoria / cant
    print('el promedio de los datos es: ', promedio)

else :
    print('¿pa, que hace aqui?')