if __name__ == "__main__":
    print("¡Hola, Python desde VS Code! 🎉")

    x,y,z="hola",2,'c'

    print("Estas son las variables que tengo "+x,y,z)
    c=3

    hora=12

    if hora<12:
        print("Buenos días")
    elif hora>=12 and hora<19:
        print("Buenas tardes")  
    else:
        print("Buenas noches")
    
    edad=70

    if edad<=17:
        print("Eres menor de edad")
    elif edad>17 and edad<=30:
        print("Eres joven")
    elif edad>30 and edad<=60:
        print("Eres adulto")
    else:
        print("Eres un adulto mayor")

    for i in range(10):
        print("El número es :",i+1,"\n",i+1)

   