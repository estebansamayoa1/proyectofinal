import json, requests, emoji, validators 


def main():
    x=0
    while x==0:
        contacts=requests.get("http://demo7130536.mockable.io/final-contacts-100")
        open('contactos.json', 'wb').write(contacts.content)
        with open('contactos.json', 'r') as JSON:
            cjason=json.load(JSON)
        with open('contactos.json', 'w') as fp:
            json.dump(cjason, fp)
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
        6.Enviar Correo
        7.Eliminar Contacto
        8.Salir\n """))
        print("------------------")
        #Agregar Contacto
        if opcion==1:
            nombre=input("Escriba el nombre del contacto que desea agregar\n")
            letra0=nombre[0]
            letra=letra0.capitalize()
            if letra in cjason:
                cjason[letra][nombre]={'telefono':'', 'email':'', 'company':'', 'extra':''}
                telefono=int(input("Ingrese un número de telefono\n"))
                cjason[letra][nombre]['telefono']=telefono
                for contacto in cjason[letra]:
                    print (contacto)

            
        #Ver contactos
        elif opcion==2:
            n=0
            nm=0
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
                nm+=1
                print ("--------------------------------")
                print (f"{nm}.{persona}")
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
        elif opcion==3:
            n=0
            editar=input("Escribe una letra para filtar y buscar el contacto de la persona que deseas llamar\n")
            for persona in cjason[editar]:
                n+=1
                print (f"{n}.{persona}")
            per=input("Ingrese el nombre completo de la persona que desea editar\n")
            for info in cjason[editar][per]: 
                print (info)

   
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
            llamar=input("Escribe una letra para filtar y buscar el contacto de la persona que deseas llamar\n")
            for persona in cjason[llamar]:
                n+=1
                print("--------------------------------")
                print(f"{n}. {persona}")
                print("--------------------------------")
            pers=input("Escriba el nombre completo de la persona que desea enviar un mensaje\n")
            if pers in cjason[llamar]:
                mensaje=input("Escriba el mensaje:\n")
                print ("\n\n")
                print("-----------------------------------------------")
                print (emoji.emojize(f"Mensaje a: {pers}")) 
                print("-----------------------------------------------")
                print (mensaje)
                print("-----------------------------------------------")
                print (emoji.emojize(f"Mensaje enviado:heavy_check_mark:\n"))
            
        
        #Enviar Correo
        elif opcion==6:
            print("Correo")

        elif opcion==8:
            print("Saliendo...")
            x=1
        


main()