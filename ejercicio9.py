#algoritmo para generar una tabla de multiplicar

inicio = input('¿quiere la tabal de multiplicar de un numero?')

if inicio == 'si' or inicio == 'sí' :

    numTab = int(input('ingrese el numero: '))

    print('la tabla de multiplicar es: ')

    numTab1 = 1 * numTab
    print('1 * ', numTab,'= ', numTab1)

    numTab2 = 2 * numTab
    print('2 * ', numTab,'= ', numTab2)

    numTab3 = 3 * numTab
    print('3 * ', numTab,'= ', numTab3)

    numTab4 = 4 * numTab
    print('4 * ', numTab,'= ', numTab4)

    numTab5 = 5 * numTab
    print('5 * ', numTab,'= ', numTab5)

    numTab6 = 6 * numTab
    print('6 * ', numTab,'= ', numTab6)

    numTab7 = 7 * numTab
    print('7 * ', numTab,'= ', numTab7)

    numTab8 = 8 * numTab
    print('8 * ', numTab,'= ', numTab8)

    numTab9 = 9 * numTab
    print('9 * ', numTab,'= ', numTab9)

    numTab10 = 10 * numTab
    print('10 * ', numTab,'= ', numTab10)

    #list1 = ['1 x ', numTab, '= ',1 * numTab]
    #print(list1)

elif inicio == 'no' :
    print('no te podemos ayudar, sorry :(')
else :
    print('hable bien ')