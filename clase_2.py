# temportizador = 5

# while temportizador > 0:
#     print(temportizador)
#     temportizador -= 1
# print("¡Despegue!")

# respuesta = ""
# while respuesta.lower != "si":
#     respuesta = input("Escribe 'si' para terminar el programa: ")
#     print("Has salido del bucle")

# edad = -1
# while edad < 0:
#     edad = int(input("Introduce tu edad: "))

# print(f"Tu edad es:")

# correcto = False
# while not correcto:

#     nombre = input("Nombre: ")
#     email = input("Email: ")
#     edad = input("Edad: ")

#     print("-----RESUMEN-----")
#     print("Nombre:", nombre)
#     print("Email:", email)
#     print("Edad:", edad)


# confirmacion = input("¿Está todo correcto? (si/no): ")
# if confirmacion.lower() != "si":
#     correcto = True
#     print("Por favor, ingresa los datos nuevamente.")

# otro while not correcto:
# confirmacion = "no"

# while confirmacion.lower() != "si":
#     nombre = input("Nombre: ")
#     email = input("Email: ")
#     edad = input("Edad: ")

#     print("-----RESUMEN-----")
#     print("Nombre:", nombre)
#     print("Email:", email)
#     print("Edad:", edad)

#     confirmacion = input("¿Está todo correcto? (si/no): ")
#     while confirmacion.lower() != "si" and confirmacion.lower() != "no":
#         confirmacion = input("Por favor, responde con 'si' o 'no': ")
# print("¡Gracias por ingresar tus datos!")

intentos = 0
while intentos < 3:
    password = input("Introduce la contraseña: ")
    if password == "secreto":
        print("¡Contraseña correcta! Acceso concedido.")
        # break
        intentos = 3  # Esto también termina el bucle

    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos} de 3.")
