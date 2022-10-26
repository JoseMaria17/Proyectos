# peso es igual a masa * aceleracion de la gravedad

print("\n****************************************************")
print("Programa para calcular nuestro peso en otros planetas")
print("*****************************************************")

def calculo_peso():
    mi_peso_tierra=75
    opcion=input("En que planeta deseas que se calcule tu peso, Marte o Neptuno:")
    opcion=opcion.lower()
    

    if opcion=="marte":
        acele_marte=3.711
        peso=mi_peso_tierra*acele_marte
        print ("Nuestro peso en Marte es de", peso, "kilogramos")
    elif opcion=="neptuno":
        acele_neptuno=11.15  
        peso=mi_peso_tierra*acele_neptuno
        print ("Nuestro peso en Neptuno es de", peso, "kilogramos")

calculo_peso()       


     
