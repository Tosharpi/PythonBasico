#algoritmo para determinar si un numero es par o inpar

resp = input('¿deseas determinar si un numero es par o impar?')
cont = 0
if (resp == 'si') or (resp == 'sí') :
    num = int(input('escriba el numero: '))

    resi = num % 2
if resi == 0 :
    cont = cont + 1
    print('el numero ', num, 'es par')
if resi != 0 :
    cont = cont + 1
    print('el numero ', num, 'es impar')


if resp == 'no' :
    cont = cont + 1
    print('bueno, no podemos ayudarte :)')
if cont == 0 :
    print('hable bien')