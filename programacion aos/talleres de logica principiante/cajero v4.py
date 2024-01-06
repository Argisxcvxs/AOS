usuario = [[]]
usuario[0].append("123456")
usuario[0].append("1245")
usuario[0].append("Pepito Perez")
usuario[0].append(20000)

usuario.append([])
usuario[1].append("12345")
usuario[1].append("2356")
usuario[1].append("Andres Florez")
usuario[1].append(20000)

usuario.append([])
usuario[2].append("45678")
usuario[2].append("8956")
usuario[2].append("Jaimito Cartero")
usuario[2].append(20000)

usuario.append([])
usuario[3].append("11203")
usuario[3].append("1234")
usuario[3].append("Mariana Pajon")
usuario[3].append(20000)

usuario.append([])
usuario[4].append("21565")
usuario[4].append("7895")
usuario[4].append("Cristobal Colon")
usuario[4].append(20000)
#usuario = [ ["45235", "1245", "Pepito Perez", 20000], ["78455", "3648", "Jaimito Cartero", 5000]            ]
action = 0
#saldo = usuario [2] [3]
#sesion = 0
#contraseña = 0
passing = "NO"
saldo_disponible = 0
nombre = 0
sesion= 0
contraseña = 0
posi = 0
#contraseña = input("ingrese su contraseña:")
sesioninicial = True
ingreso = True
while ingreso:
    print("===================================\n\
BIENVENIDO A SU CAJERO AUTOMATICO\n\
===================================")
    iniciar = input("EN ESTE SU BANCO ESTAMOS TRABAJANDO CONSTANTEMENTE PARA BRINDARLE UN MEJOR SERVICIO.\n\
                    DESEA INGRESAR AL MENU DE OPCIONES? Y OR N:  ")
    iniciar = iniciar.lower()
    if(iniciar == "y"):
        while sesioninicial:
            
        #sesion = input("INGRESE SU NUMERO DE CUENTA: ")
                    
            if( passing == "NO"):
                sesion = input("INGRESE SU NUMERO DE CUENTA: ")
                existecuenta = False

                for i in range(len(usuario)):
                                
                    if usuario[i][0] == sesion:
                        existecuenta = True                     
                        while True:
                            contraseña = input("INGRESE SU CONTRASEÑA:")
                            #for i in range(len(usuario)):
                            if usuario [i] [1] == contraseña:
                                    print("==============================================")
                                    print("BIENVENIDO SR(A)", " ", usuario [i][2])
                                    print("==============================================")
                                    passing = "YES"
                                    sesion = usuario [i] [0]
                                    nombre = usuario [i] [2]
                                    saldo_disponible = usuario [i] [3]
                                    posi = i
                                    break
                            else:
                                print("=============================================================")
                                print("  CLAVE INCORRECTA POR FAVOR VERIFIQUELA E INTENTE DE NUEVO")
                                print("=============================================================")
            if( existecuenta == False):
                print("==============================================")
                print("ERROR CUENTA BANCARIA NO EXISTE",  )
                print("==============================================")
            else:#(passing== "YES"):
                action = input("QUE ACCION DESEA REALIZAR? \n\
                    1.-RETIRAR \n\
                    2.-CONSIGNAR \n\
                    3.-TRANSFERIR FONDOS\n\
                    4.-CONSULTAR SALDO \n\
                    5.-CERRAR SESION \n\
                    6.-SALIR\n\
                    DIGITE AQUI SU ELECCION: ")
            
                if (action =="1"):
                    retirar = int(input("INGRESE LA CANTIDAD A RETIRAR: "))
                    if (retirar <= saldo_disponible):
                        saldo_disponible = saldo_disponible - retirar
                        print("============================================")
                        print("         ACCION REALIZADA CON ÉXITO         ")
                        print("============================================")
                        actionret = int(input("DESEA VER SU NUEVO SALDO?\n\
                                1.-SI \n\
                                2.-NO\n\
                                DIGITE AQUI SU ELECCION: "))
                        
                        if (actionret == 1):
                            
                            print("==============================================")
                            print("SU NUEVO SALDO ES", "$",saldo_disponible,)
                            print("==============================================")
                        else:
                            print("==============================================")
                            print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS")
                            print("==============================================")

                    elif(retirar > saldo_disponible):
                        print("==============================================")
                        print("SALDO INSUFICIENTE")
                        print("==============================================")
                        error=int((input("DESEA VERIFICAR SU SALDO?\n\
                                            1.-SI\n\
                                            2.-NO\n\
                                            DIGITE AQUI SU ELECCION: ")))
                        if(error == 1):
                            print("==============================================")
                            print("SU SALDO DISPONIBLE ES", "$",saldo_disponible)
                            print("==============================================")
                        else:
                            print("==============================================")
                            print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS =)")
                            print("==============================================")
                    elif(retirar == 0):
                        print("==============================================")
                        print("    ACCION INCORRECTA CERO NO ES UN VALOR" )
                        print("==============================================")
                        error=int((input("DESEA VERIFICAR SU SALDO?\n\
                                            1.-SI\n\
                                            2.-NO\n\
                                            DIGITE AQUI SU ELECCION: ")))
                        if(error == 1):
                            print("==============================================")
                            print("SU SALDO DISPONIBLE ES", "$",saldo_disponible)
                            print("==============================================")
                        else:
                            print("==============================================")
                            print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS =)")
                            print("==============================================")
                    else:
                        print("==============================================")
                        print("          ERROR ACCION NO VALIDA              ")
                        print("==============================================")              
                elif(action == "2"):
                    
                    consignar = int(input("INGRESE EL MONTO A CONSIGNAR: "))
                    
                    
                   # if (consignar == int):
                        #print("123")

                    if(consignar > 0):
                        saldo_disponible = saldo_disponible + consignar
                        print("==============================================")
                        print("        ACCION REALIZADA CON EXITO            ")
                        print("==============================================")
                        accionconsig = int(input("DESEA VER SU NUEVO SALDO?\n\
                            1.-SI \n\
                            2.-NO\n\
                            DIGITE AQUI SU ELECCION: "))
                        if (accionconsig == 1):
                            print("==============================================")
                            print("SU NUEVO SALDO ES", "$",saldo_disponible,)
                            print("==============================================")
                        else:
                            print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS")
                    else:
                        print("==============================================")
                        print("          ERROR ACCION NO VALIDA              ")
                        print("==============================================")
                elif(action == "3"):
                    usuario2 = 0
                    actionver = True
                    while actionver:
                        montotransf = int(input("INGRESE LA CANTIDAD QUE DESEA TRANSFERIR: "))
                        if montotransf <= saldo_disponible:
                            validar = True
                            validar_u = "no"
                            while validar:
                                if(validar_u == "no"):
                                    print("==============================================")
                                    acciontransferir = input("INGRESE EL NUMERO DE CUENTA AL QUE DESEA TRANSFERIR:")
                                    cuenta_a_trasnferir = False

                                    for i in range(len(usuario)):
                                        
                                        if usuario[i][0] == acciontransferir:
                                            cuenta_a_trasnferir = True
                                            bucle_transf = True                     
                                            while bucle_transf:
                                                usuario2 = usuario [i]
                                                print (usuario2)
                                                if usuario [i] [0] == acciontransferir:
                                                        
                                                        print("==============================================")
                                                        print("ESTA SEGURO QUE DESEA TRANSFERIR", montotransf, "A: ", usuario [i][2])
                                                        print("1.-SI")
                                                        print("2,-NO")
                                                        confirmar = input("DIGITE AQUI SU RESPUESTA: ")
                                                        if(confirmar == "1"):
                                                           #print(usuario2)
                                                            usuario [i] [3] = usuario [i] [3] + montotransf
                                                            usuario [posi] [3] = usuario [posi] [3] - montotransf
                                                            saldo_disponible = saldo_disponible - montotransf
                                                            print("============================") 
                                                            print(" ACCION REALIZADA CON EXITO")
                                                            print("============================")
                                                            print("QUE DESEA HACER?")   
                                                            print("1.-VER MI SALDO")
                                                            print("2.-REALIZAR OTRA TRANSACCION")
                                                            accion= input("3.-VOLVER AL MENU PRINCIPAL: ")
                                                            if( accion == "1"):
                                                                print("==============================================")
                                                                print("SU SALDO DISPONIBLE ES: ", "$", saldo_disponible)
                                                                print("==============================================")
                                                                validar = False
                                                                actionver = False
                                                                bucle_transf = False
                                                                break
                                                            elif(accion == "2"):
                                                                validar = False
                                                                bucle_transf = False
                                                                break
                                                            elif(accion == "3"):
                                                                validar = False
                                                                actionver = False
                                                                bucle_transf = False
                                                                break

                                                            else:
                                                                print ("=================================")
                                                                print ("     ERROR ACCION INCORRECTA")
                                                                print (" SERA ENVIADO AL MENU PRINCIPAL")
                                                                print ("=================================")
                                                                validar = False
                                                                actionver = False
                                                                bucle_transf = False
                                                                break
                                                        #actionver= False
                                                        #validar_u = "yes"
                                                        #break
                                                
                                                    #sesion = usuario [i] [0]
                                                        #nombre = usuario [i] [2]
                                                        #saldo_disponible = usuario [i] [3]
                                                        #posi = i
                                    if(cuenta_a_trasnferir == False):
                                        print("==========================================================================") 
                                        print(" ERROR CUENTA BANCARIA NO EXISTE POR FAVOR VERIFIQUE E INTENTE DE NUEVO") 
                                        print("==========================================================================")  
                                if (acciontransferir == sesion):
                                    #cuenta_a_trasnferir = True
                                    print("==============================================================")
                                    print(" error no puede usar su propia cuenta para transferir fondos. ")
                                    print("==============================================================")
                        else:
                            print("error no posee esa cantidad de dinero en su cuenta")
                            validacion = int(input("desea ver su saldo disponible\n\
                                                1.-SI\n\
                                                2.-NO\n\
                                                ingrese aqui su opcion: "))
                            if validacion == 1:
                                print("==============================================")
                                print("SU SALDO DISPONIBLE ES: ", "$", saldo_disponible)
                                print("==============================================")
                                actionver = False
                elif(action == "4"):
                    print("==============================================")
                    print("SU SALDO DISPONIBLE ES: ", "$", saldo_disponible)
                    print("==============================================")
                elif(action == "5"):
                    usuario[posi] [3] = saldo_disponible
                    print('=======================================')
                    print("GRACIAS POR USAR NUESTROS SERVICIOS")
                    print("VUELVA PRONTO SR(A)", nombre )
                    print('=======================================')
                    passing = "NO"
                elif(action == "6"):
                    usuario[posi] [3] = saldo_disponible
                    print('=======================================')
                    print("GRACIAS POR USAR NUESTROS SERVICIOS")
                    print("VUELVA PRONTO SR(A)", nombre )
                    print('=======================================')
                    passing = "NO"
                    break
                else:
                    print("==========================================================================")
                    print("  ACCION INCORRECTA, POR FAVOR VERIFIQUE SU ELECCION Y VUELVA A INTENTAR")
                    print("==========================================================================")  
        sesioninicial = True
    elif(iniciar == "n"):
        print("TENEMOS NUEVAS FUNCIONES Y BENEFICIOS ESTUPENDOS QUE TE PUEDEN ENCANTAR.")    
    else:
        print("OPCION ERRADA POR FAVOR DIGITE UNO DE LOS DOS VALORES INDICADOS")
    