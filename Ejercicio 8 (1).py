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

print("Bienvenido a la plataforma. Por favor, llene los siguientes datos para saber el número de silla asignado en el concierto.")

nombre = input("Ingrese su nombre: ")
direccion = input("Ingrese su dirección: ")

while True:
    genero = input("Ingrese su género (M , F): ")
    if genero in ["M",  "F"]:
        break
    else:
        print("Género no válido. Por favor, ingrese M, F.")

while True:
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        documento = input("Ingrese su número de Cédula de Ciudadanía: ")
        break
    elif 15 <= edad < 18:
        documento = input("Ingrese su número de Tarjeta de Identidad: ")
        break
    else:
        print("Edad no válida. Debe tener al menos 15 años.")

identificacion = input("Ingrese su número de identificación: ")

sillas_disponibles_hombres = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
sillas_disponibles_mujeres = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]

silla_asignada = None

if genero == "M":
    while True:
        if not sillas_disponibles_hombres:
            print("Lo sentimos, no quedan sillas disponibles para hombres.")
            break
        silla = sillas_disponibles_hombres.pop(0)
        print(f"Su silla asignada es: {silla}")
        break

elif genero == "F":
    while True:
        if not sillas_disponibles_mujeres:
            print("Lo sentimos, no quedan sillas disponibles para mujeres.")
            break
        silla = sillas_disponibles_mujeres.pop(0)
        print(f"Su silla asignada es: {silla}")
        break

else:
    print("Género no válido. No se pudo asignar una silla.")

print("Gracias por usar la plataforma.")










