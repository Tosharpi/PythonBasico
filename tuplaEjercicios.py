#datos personales
print('ingrese su informacion personal: ')
nombUsu = input('Nombre: ')
Id = int(input('Numero de identificacion: '))
edad = int(input('Su edad: '))
tuplaInfoPersonal = (nombUsu, Id, edad,)



#datos de direccion de residencia
print('ingrese sus datos de residencia: ')
barrio = input('ingrese su barrio: ')
calle = input('ingrese su calle: ')
ciudad = input('ingrese su ciudad: ')
pais = input('ingrese su pais: ')
tuplaDireccion = (pais, ciudad, barrio, calle)



#datos de educacion

nivelEdu = 'nada'
extra = 'no'

eduBasic = input('¿cuenta con educacion basica hasta bachiller?')
if eduBasic == "si":
    nivelEdu = 'Bachillerato'
elif eduBasic != "si":
    prima = input('¿primaria?')
    if prima == "si":
        nivelEdu = 'primaria'

uniResp = input('¿educacion universitaria?')
if uniResp == 'si':
    uni = 'sí'
extraResp = input('¿algun curso o educacion extra?')
if extraResp == 'si':
    extra = 'si'
tuplaEducacion = (nivelEdu, uni, extra)



#datos de experiencia laboral

exp = input('¿cuenta con experiencia laboral?')
if exp == 'si':
    tiempoLab = input('¿cuanto tiempo de experiencia?')
    certificacion = input('¿cuenta con algun documento o certificcion que corrobore ese tiempo?')
elif exp == 'no' :
    tiempoLab = 'sin experiencia laboral'
if certificacion == 'si':
    certi='sí'
elif certificacion != 'si':
    certi = 'no'
tuplaExp = (tiempoLab, certi)

print()

print(tuplaInfoPersonal[0], 'con numero de identificacion ', tuplaInfoPersonal[1], ' y de ', tuplaInfoPersonal[2], 'años')
print()
print('con residencia en ', tuplaDireccion[2], tuplaDireccion[3], 'en la ciudad ', tuplaDireccion[1], '/', tuplaDireccion[0] )
print()
print('cuenta con ', tuplaEducacion[0], ' de educacion. ', 'Universidad: ', tuplaEducacion[1], ' Cursos extra:  ', tuplaEducacion[2] )
print()
print('experiencia laboral: ',  tuplaExp[0], ' Certificacion ', tuplaExp[1])