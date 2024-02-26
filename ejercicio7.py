# #algoritmo para calcular el area de un triangulo

resp = input('desea calcular el area de un triangulo?')
cont=0
if (resp == 'si') or (resp == 'sí') :
    cont = 1
    altura = int(input('ingrese la altura del triangulo: '))
    base = int(input('ingrese la base del triangulo: '))
    area = (base * altura) / 2
    print('el area del triangulo es: ', area)
if (resp == 'no') or (resp == 'No') :
    cont =1
    print('no te puedo ayudar, lo siento')
elif cont == 0 :
    print('hable bien')