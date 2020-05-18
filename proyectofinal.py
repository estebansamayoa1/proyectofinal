import json, requests, emoji, validators, csv 


def main():
    x=0
    while x==0:
        contacts=requests.get("http://demo7130536.mockable.io/final-contacts-100")
        open('contactos.txt', 'wb').write(contacts.content)
        with open('contactos.txt', 'r') as JSON:
            cjason=json.load(JSON)
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
        8.Exportar
        9.Salir\n """))
        print("------------------")
        #Agregar Contacto
        if opcion==1:
            nombre=input("Escriba el nombre del contacto que desea agregar\n")
            letra0=nombre[0]
            letra=letra0.capitalize()
            if letra in cjason:
                telefono=int(input("Ingrese un número de telefono\n"))
                correo=input("Ingrese un correo electronico\n")
                if validators.email(correo)==True:
                    compañia=input("Ingrese donde labora el contacto\n")
                    extra=input("Extra:\n")
                    cjason[letra]={f'{nombre}':{'telefono':f'{telefono}', 'email':f'{correo}', 'company':f'{compañia}', 'extra':f'{extra}'}}
                    print ("\n\n")
                    print(nombre)
                    print (f"telefono: {cjason[letra][nombre]['telefono']}")
                    print (f"email: {cjason[letra][nombre]['email']}")
                    print (f"company: {cjason[letra][nombre]['company']}")
                    print (f"extra: {cjason[letra][nombre]['extra']}")
                    
                else:
                    print ("Correo invalido\n")
                
             
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
                print (f"->Telefono: {cjason[letra][persona]['telefono']}")
                print (f"->E-mail: {cjason[letra][persona]['email']}")
                print (f"->Company: {cjason[letra][persona]['company']}")
                print (f"->Extra: {cjason[letra][persona]['extra']}")
                print ("\n\n")
        
            
        
        #Editar Contactos
        elif opcion==3:
            n=0
            editar=input("Escribe una letra para filtar y buscar el contacto de la persona que deseas llamar\n")
            for persona in cjason[editar]:
                n+=1
                print (f"{n}.{persona}")


   
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
            llamar=input("Escribe una letra para filtar y buscar el contacto de la persona que deseas enviarle mensaje\n")
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
            n=0
            correo=input("Escribe una letra para filtar y buscar el contacto de la persona que deseas enviarle mensaje\n")
            for persona in cjason[correo]:
                n+=1
                print("--------------------------------")
                print(f"{n}. {persona}")
                print("--------------------------------")
            pers=input("Escriba el nombre completo de la persona que desea enviar un mensaje\n")
            if pers in cjason[correo]:
                asunto=input("Asunto:")
                mensaje=input("Escriba el mensaje:\n")
                print ("\n\n")
                print("-----------------------------------------------")
                print (emoji.emojize(f"Mensaje a: {pers} al correo {cjason[correo][pers]['email']}")) 
                print("-----------------------------------------------")
                print (asunto)
                print("-----------------------------------------------")
                print (mensaje)
                print("-----------------------------------------------")
                print (emoji.emojize(f"Mensaje enviado:heavy_check_mark:\n"))

        elif opcion==8:
            w = csv.writer(open("contactos.csv", "w"))
            for key, cont in cjason.items():
                w.writerow([key, cont])
    
        elif opcion==9:
            contactos1 = json.dumps(cjason)
            f = open("contactos.json","w")
            f.write(contactos1)
            f.close()
            print("Saliendo...")
            x=1
        


main()