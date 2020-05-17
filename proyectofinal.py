import json
import requests
import emoji
import validators 
import numpy as np 


def main():
    x=0
    while x==0:
        contacts=requests.get("http://demo7130536.mockable.io/final-contacts-100")
        cjason=contacts.json()
        #Menú Principal 
        print ("\n\n")
        print("CONTACT BOOK")
        print("------------------")
        print("MENÚ PRINCIPAL")
        opcion=int(input("""
        1.Agregar Contactos
        2.Ver Contactos
        3.Editar Contactos
        4.Llamar contacto
        5.Enviar Mensaje
        6.Salir\n """))
        print("------------------")

        #Agregar Contacto
        if opcion==1:
            for letra in cjason:
                for persona in cjason[letra]: 
                    print (persona)
                    for item in cjason[persona]:
                        print("Key : {} , Value : {}".format(item, persona[item]))
                
        #Ver contactos
        elif opcion==2:
            n=0
            for letra in cjason: 
                print (letra+":")
                print("--------------------------------")
                for persona in cjason[letra]:
                    n+=1
                    print(f"{n}. {persona}")
                print("--------------------------------")
                print ("\n") 
            letra0=input ("Ingrese una letra para filtrar los contactos que desea ver\n")
            letra=letra0.capitalize()
            for persona in cjason[letra]: 
                n+=1
                print ("--------------------------------")
                print (f"{n}.{persona}")
                print ("--------------------------------")
                print (cjason[letra][persona]['telefono'])
                print (cjason[letra][persona]['email'])
                print ("\n")
            esp=input("Ingrese el nombre del contacto para ver el resto de los datos\n")
            if esp in cjason[letra]:
                print (f"{esp}")
                print (cjason[letra][esp]['email'])
            else: 
                print ("Contacto Invalido")
            
                
                   
        #Editar Contactos
    
        #Llamar Contacto
        elif opcion==4: 
            n=0
            llamar=input("Escribe una letra para filtar y buscar el contacto de la persona que deseas llamar\n")
            for persona in cjason[llamar]:
                n+=1
                print("--------------------------------")
                print(f"{n}. {persona}")
                print("--------------------------------")
            pers=input("Escriba el nombre completo de la persona que desea llamar\n")
            if pers in cjason[llamar]:
                print (emoji.emojize(f":telephone_receiver:Llamando a {pers} al {cjason[llamar][pers]['telefono']}")) 
            
            
            
    
        #Enviar Mensaje
        elif opcion==5:
            n=0
            numbers = [0]
            num = 0
            letra5=input("Escriba la primer letra del contacto al que desea enviarle un mensaje\n")
            
                     
        #Salir 
        elif opcion==6:
            print("Saliendo...")
            x=1 
main()