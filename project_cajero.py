
mis_clientes = {
    'Susana Ramirez': 1500000, 
    'Daniela Castro': 350000, 
    'Juan Hernandez': 830000
    }

contraseñas = {
    'Susana Ramirez': 'susana_1',
    'Daniela Castro': 'daniela_1',
    'Juan Hernandez': 'juan_1'
   }


nombres = list(mis_clientes.keys())  # Se obtiene la lista de nombres a partir del diccionario

while True:
    try:
        #Preguntar por el cliente
        seleccion = int(input('\n¿Usted quién es?\n1: Susana Ramirez\n2: Daniela Castro\n3: Juan Hernandez\n0: SALIR\n='))
        print()

        if seleccion == 0:
            print('Saliendo... \nSalida exitosa\n')
            break
        
        #Darle la bienvenida al cliente y preguntar por la trasacción a realizar
        elif 1 <= seleccion <= len(nombres):
            nombre_cliente = nombres[seleccion - 1]
            print(f'¡Hola, {nombre_cliente}, bienvenid@!\n')
            
            # Transacciones
            while True:
                try:
                    proceso = int(input('¿Qué desea hacer?\n1: Consultar saldo\n2: Retirar\n3: Agregar\n0: Salir\n='))
                    
                    #El cliente quiere consultar el saldo de cuenta:
                    if proceso == 1 :
                        print(f'\nSu saldo es: ${mis_clientes[nombre_cliente]:,.0f}\n¡Gracias por usar nuestros servicios!\n')
                        break
                   
                    #El cliente quiere retirar dinero de su cuenta. Se le pregunta el monto:
                    elif proceso == 2 :
                        monto_retiro = (int(input('\nIngrese el monto que desea retirar:')))
                        
                        #El monto a retirar es menor o igual al saldo de la cuenta. Puede retirar.
                        if monto_retiro <= mis_clientes[nombre_cliente]:                        
                            mis_clientes[nombre_cliente] -= monto_retiro  # Se actualiza el saldo
                            print(f'\nRetiro exitoso. \nUsted ha retirado ${monto_retiro:,.0f}. \nEl nuevo saldo de su cuenta es ${mis_clientes[nombre_cliente]:,.0f}\n')
                        else:
                            print('\nFondos insuficientes. No puede retirar más de su saldo actual.\n')

                
                    #El cliente quiere ingresar dinero a su cuenta:  
                    elif proceso == 3 :
                        monto_adicion = (int(input('\nIngrese el monto que desea ingresar:')))
                        nuevo_total_cuenta = (mis_clientes[nombre_cliente]) + monto_adicion
                        print(f'\nAdición exitosa. \nUsted ha ingresado {monto_adicion}. \nEl nuevo saldo de cuenta es ${nuevo_total_cuenta}\n')
                    
                    #El cliente quiere salir
                    elif proceso == 0 :
                        print ('Saliendo... \nSalida exitosa\n')
                        break
                
                    else:
                        print('Opción no válida. Inténtelo de nuevo\n')
                    
                except ValueError:
                    print('Por favor, ingrese un número válido.\n')
            
        
        else:
            print('Opción no válida. Inténtelo de nuevo.\n')

    except ValueError:
        print('Por favor, ingrese un número válido.\n') 
        



