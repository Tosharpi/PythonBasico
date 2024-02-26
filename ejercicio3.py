#algoritmo para calcular el factorial de un numero
#como hago para poner que si el usuario ingresa un numero con decimales el codigo le diga que
#debe de ingresar solo numeros enteros

numero = int(input('ingrese el numero a calcular: '))

fact=1
for i in range(1, numero+1):
    fact = fact * i
print('el resultado de factorizar ', numero,'es: ', fact)