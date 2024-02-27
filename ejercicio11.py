#algoritmo para calcular el area de un circulo
resp = input('¿desea saber el area del circulo?')
if resp == 'si' :
    
    print('ingrese el radio del circulo: '); radio = float(input())

    area = 3.1416 * (radio * radio)
    print('el area del circulo es: ', area)
elif resp != 'si' :
    print ('¿que?')
    #