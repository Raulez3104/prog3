import random
print('===================================')
print('Bienvenido al Juego adivinar numero')
print('===================================')

numero_secreto=random.randrange(1,101)

print('Selecciona el nivel de dificultad')
print('(1)Fácil  (2)Medio  (3)Dificil')
nivel=int(input('Ingrese el nivel de dificultad:'))
if(nivel==1):
  total_intentos=20
elif(nivel==2):
  total_intentos=10
else:
  total_intentos=5

for iteracion in range(1,total_intentos+1):
  print('Intento: {} de {}'.format(iteracion,total_intentos))
  entrada=int(input('Digite un numero entre el 1 al 100'))
  print('Digitaste...',entrada)
  if(entrada<1 or entrada>100):
    print('Ingresar un numero entre 1 y 100')
    continue
  acertaste= entrada==numero_secreto #iguales
  mayor=entrada>numero_secreto #mayor
  menor=entrada<numero_secreto #menor
  if(acertaste):
    print('Felicitaciones... Adivinaste el numero')
    print('El numero que se tenia que adivinar es: ',numero_secreto)
  elif(mayor):
    print('Lo siento... el numero que ingresaste es mayor al numero secreto')
  elif(menor):
    print('Lo siento... el numero que ingresaste es menor al numero secreto')
  iteracion=iteracion+1
print('Fin del Juego')
