num1 = input('ingrese el primer numero: ')
num1 = int(num1)
num2 = input('ingrese el primer numero: ')
num2 = int(num2)
num3 = input('ingrese el primer numero: ')
num3 = int(num3)

numMayor1 = (num1) > (num2)
#print (numMayor1)
if numMayor1 : 
    numMayor1 = num1
else :
    numMayor1 = num2

numMayor2 = (numMayor1) > (num3)
if numMayor2 :
    print ('el numero mayor de los tres es: ', numMayor1)
else :
    numMayor2 = num3
    print('el numero mayor es: ', numMayor2)
