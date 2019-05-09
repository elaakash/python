
print ("Bienvenido a la calculadora de Aakash")
# ciclo.
while True:
    #variables
    print ("")
    print("[1] Si quiere sumar")
    print("[2] Si quiere restar")
    print("[3] Si quiere dividir")
    print("[4] Si quiere multiplicar")
    print("[5] Si quiere salir")
    di= input("ingrese una operacion: ")
    if di == "1":
        print("Has saleccionado sumar")
        x= int(input("ingrese el primer numero\n"))
        y= int(input("ingrese el segundo numero\n"))
        suma = x + y
        print ("su resultado es", suma)
    elif di=="2":
        print("Has selccionado restar")
        x= int(input("ingrese el primer numero\n"))
        y= int(input("ingrese el segundo numero\n"))
        resta = x - y
        print ("su resutado es", resta)
    elif di=="3":
        x= int(input("ingrese el primer numero\n"))
        y= int(input("ingrese el segundo numero\n"))
        if y == 0:
            print("error indeterminado")
            pass
        else:
            div = x / y
            print ("su resultado es", div)
    elif di =="4":
        print("Has selccionado multiplicar")
        x= int(input("ingrese el primer numero\n"))
        y= int(input("ingrese el segundo numero\n"))
        mult = x * y
        print ("su resutado es", mult)
    elif di =="5":
        print("Gracias por usar la calculadora Aakash")
        exit()

