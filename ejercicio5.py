#algoritmo para pasar de grados celcius a farenheit

preg = str(input('¿quieres pasar celcius a farenheit?'))
control = 0

if (preg == 'si') or (preg == 'sí') :
    control = control + 1
    tempCel = float(input('¿cuantos grados celcius a calcular?'))
    convFarenheit = (tempCel * 1.8) + 32
    #print(convFarenheit)
    print('la temperatura en Farenheit serian: ', convFarenheit)

elif control == 0 :

    preg2 = input('¿quieres pasar de farenheit a celcius?')

    if (preg2 == 'si') or (preg2 == 'sí') :
        control = control + 1

        tempFar = float(input('¿cuantos grados farenheit a calcular?'))
        convCelcius = (tempFar - 32) / 1.8
        print('la temperatura en Celcius serian: ', convCelcius)


if control == 0 :
    print('no te podemos ayudar, lo siento')