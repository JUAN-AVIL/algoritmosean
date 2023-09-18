#Los ciclos para la programacion son secuenciales que permiten la realizacion o ejecucion de
#funciones para poder abreviar o automatizar codigo, esta el cilo for que sifnifica
#ciclo while que significa mientras que

#print ("Tipo de programa que incluya un ciclo")

#print ("-------------- Inicio del ciclo ---------------- -----")

#for i in range (10):
 #   print (i**2)

#print ("finalize el ciclo")

#el programa que vamos a realizar tiene como fianlidad realizar un ciclo donde le pida al usuario 
#ingresar hasta tres numeros, es este caso la edad, y cuando genere la variable correcta
#ejecute en pantalla la siguiente accion, por ejemplo: digita tu numero de cedula, 3 digite si desea
#saber el numero de silla donde fue asignado

print ("bienvenido a la plataforma por favor llene los siguientes datos para saber el numero de silla asignado en el concierto ")

Nombre= str (input ("ingrese su nombre :  "))

Direcion= str (input ("ingrese su direcion : "))

for edad in range(15, 35):

    num = int(input("Ingrese su edad: "))

    if num > 17:

        input("Cédula ciudadanía: ")

    else:
        input("Tarjeta de identidad: ")

identificasion = str (input ("ingrese su numero de identificasion : "))

sillas_disponibles = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10",
                     "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10",
                     "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10",
                     "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"]









