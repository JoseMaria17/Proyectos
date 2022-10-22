print("+++++++++++++++++++++++++++++++++++++++++++++")
print("programa de verificasion para numeros primos.")
print("+++++++++++++++++++++++++++++++++++++++++++++")

num=int(input("Introduce el numero a comprobar, por favor: "))
list=[x for x in range(2,num) if num%x==0]
if num=1:
    print("El numero ",num, 'No es primo'")
elif num=2: 
    print("El numero ",num, 'Si es primo'")
elif len(list)!=0:
    print("El numero ",num, 'No es primo'") 
else:
    print("El numero ",num, 'Si es primo'")
          
print("Termino la ejecusion del programa exitosamente.")          
          
          
        
        
