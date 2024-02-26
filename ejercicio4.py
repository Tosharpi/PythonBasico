#algoritmo para verificar si un numero es primo

resp = str(input('ey, quieres saber si tú numero es primo? '))

resp2 = (resp == 'si') or (resp == 'sí')
control = 0

if resp2 == True :

    numP = int(input('ingrese un numero'))
    control = 1
    cont = int(0)

    while control <= numP :

        if numP % control == 0 :

            cont = cont + 1
            control = control + 1

        if cont == 2 :

            print('el numero ', numP,'es primo')
        else :
            print('el numero ', numP,'no es primo, es par')