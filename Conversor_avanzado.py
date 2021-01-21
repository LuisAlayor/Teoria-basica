print("================================")
print("Convertidor de numeros a letras")
print("================================\n")


print("Menú de opciones: \n")
print("Presiona 1 para convertir de numero a palabras.")
print("Presiona 2 para convertir de palabras a numero. \n")

opcion = int(input("Cual es tu opcion elegida?: "))


if opcion == 1:
    print("\n Conversor de numero a palabras. \n")

    opcion_uno = int(input("Introduce el numero deseado: "))

    if opcion_uno ==1:
        print("El numero es uno")
    elif opcion_uno ==2:
        print("El numero es dos")
    elif opcion_uno ==3:
        print("El numero es tres")
    elif opcion_uno ==4:
        print("El numero es cuatro")
    elif opcion_uno ==5:
        print("El numero es cinco")
    elif opcion_uno ==6:
        print("El numero es seis")
    elif opcion_uno ==7:
        print("El numero es siete")
    elif opcion_uno ==8:
        print("El numero es ocho")
    elif opcion_uno ==9:
        print("El numero es nueve")
    elif opcion_uno ==10:
        print("El numero es diez")
    else:
        print("Se siente, solo para numeros de 1 a 10. ")
    


elif opcion == 2:
    print("\n Conversor de palabras a numero. \n")

    opcion_dos = input("Texto a transformar¿?: ")
    opcion_dos = opcion_dos.lower()

    if opcion_dos == "uno":
        print("El numero es '1'")
    elif opcion_dos == "dos":
        print("El numero es '2'")
    elif opcion_dos == "tres":
        print("El numero es 3")
    elif opcion_dos == "cuatro":
        print("El numero es 4")
    elif opcion_dos == "cinco":
        print("El numero es 5")
    elif opcion_dos == "seis":
        print("El numero es 6")
    elif opcion_dos == "siete":
        print("El numero es 7")
    elif opcion_dos == "ocho":
        print("El numero es 8")
    elif opcion_dos == "nueve":
        print("El numero es 9")
    elif opcion_dos == "dies":
        print("El numero es 10")
    else:
        print("Se siente, solo para numeros de 1 a 10. ")

else:
    print("Eres mas tonto que una acelga, aprende a seguir instrucciones.")

print("\n Fin.")



