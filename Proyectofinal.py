
import os
os.system("cls")


print("Bienvenido a tu calculador de estado nutricional\n")



op=int(input("Opcion de Menu \n1.Calcular IMC\n2.Peso Ideal\n3.Constitucion Cosporal\n"))

if(op==1):
    print("Digite su peso actual en kilos\n")
    peso=float(input())
    print("Digite su altura en m\n")
    altura=float(input())
    
    imc=peso/altura**2
    print("Su IMC es de","{:.2f}".format(imc)," kg.")
    print("Fin de la aplicacion")
    
     

elif(op==2):
    op=int(input("Indique su genero \n1.Mujer\n2.Hombre\n"))
    if(op==1):
        print("Digite su altura en cm\n")
        altura=float(input())
        peso=altura-152/2.5*2.3+45.5
        print("Su peso ideal es de: "+str(peso))
        print("Fin de la aplicacion")
    elif(op==2):
        print("Digite su altura en\n")
        altura=float(input())
        peso=altura-152/2.5*2.3+48
        print("Su peso ideal es de" +str(peso))
        print("Fin de la aplicacion")
    else:print("Opcion invalida")

elif(op==3):
     print("Digite su altura\n")
     altura=float(input())
     print("Digite tamano de la muneca")
     muneca=float(input())
     cc=altura/muneca
     print("Su Constitucion Corporal es de","{:.2f}".format(cc)," cm.")
     print("Fin de la aplicacion")
else:print("Opcion invalida")

    
        
