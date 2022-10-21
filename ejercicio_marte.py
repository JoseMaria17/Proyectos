





nombre="jose"

# int=1   flotantes=3.4  booleanos= True-False   str="hola mundo"  complex=5j 

# entrada(input):Es el que nos va a solicitar datos desde teclado

#salida(print):nos permite imprimir letreros en pantalla y indicar que un proceso a finalizado

""" hola franchesca
como estas
coma vas con python"""

"""print("\nConversor de numeros a letra y viceversa \n")
print("opcion #1: conversor de numeros a letras")
print("opcion #2: conversor de letras a numeros\n")

opcion=int(input("\n¿Cual opcion deseas implementar?: "))

if opcion==1:
    print("Elegistes el conversor de numeros a letras.")
    opcion_uno=int(input("\nIntroduce el numero que quieres traducir a letra: "))
    if opcion_uno==1:
        print("El numero es 'Uno'")
    elif opcion_uno==2:
        print("El numero es 'Dos'") 
    elif opcion_uno==3:
        print("El numero es 'Tres'")
    else:
        print("Lo sentimos la opcion no esta disponible")           
elif opcion==2:
    print("Elegistes el conversor de letras a numeros.")
    opcion_dos=input("\nIntroduce la letra que quieres traducir a numero:")
    opcion_dos=opcion_dos.lower()
    if opcion_dos=="uno":
        print("El numero es '1'")
    elif opcion_dos=="dos":
        print("El numero es '2'") 
    elif opcion_dos=="tres":
        print("El numero es '3'")
    else:
        print("Lo sentimos la opcion no esta disponible") 

else:
    print("La opcion no esta disponible")  
    print("termino la ejecusion de nuestro programa.")   """



for i in range(4):
    print("hola chicos")

    

mi_email=input("Introduce tu email:")
for i in mi_email:
    print(i)    








""" edad=5

while  edad<=5:
    print("hola mundo") """  

 
""" bucles:son los que nos van a permitir repetir  un conjunto de instrucciones siempre y cuando una 
instruccion se cumpla, es decir mientras la condicion se cumpla este va a seguir ejecutando las 
instruicciones que contenga 
 """

 





    
    



































# peso es igual a masa * aceleracion de la gravedad




    



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

#calculo_peso()       


     
