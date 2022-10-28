print("\n************************")
print("Programa isla del tesoro")
print("************************")

print("|\nbienvenido a la isla, tu mision sera encontrar el tesoro.")
print("\nTienes dos caminos a elejir, playa o selva")
g_o="'GAME OVER'"
y_w="'YOU WIN'"
camino=input("¿Cual camino elijes?: ")
camino=camino.lower()

if camino=="playa":
    print("Elejistes el camino de la playa")
    print("Caistes en un agujero y te ahogastes"+g_o)
elif camino=="selva":
    print("Elejistes el camino de la selva")
    sobrevivir=input("¿Cuentas con lo necesario para sobrevivir a la selva, ('si, no')? :")
    sobrevivir=sobrevivir.lower()
    if sobrevivir== "si" or sobrevivir=="yes":
        print("Llegastes a la entrada de una cueva la cual te llevara al tesoro")
        mapa=input("¿Cuentas con el mapa del tesoro('si, no' )?: ")
        mapa=mapa.lower()
        contador=0
        while mapa=="no" or mapa=="not":
            print("Regresa a la embarcasion y encuentralo")
            contador+=1
            mapa=input("¿Cuentas con el mapa del tesoro('si, no' )?: ")
            if contador==2:
                print("Lo sentimos exedistes el numero de intentos, el programa finalizara.")
                break
        if mapa=="yes" or mapa=="si":
            print("Entras a la cueva y encuentras el cofre del tesoro") 
            print("Lleva el cofre del tesoro hasta la embarcasion "+y_w) 
            print("\nNuestro programa finalizo correctamente")   
    else:
        print("Moriste de sed y hambre "+g_o)

else:
    print("El camino que elejiste")
