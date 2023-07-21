import requests
datos_api = requests.get('https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-api.json')
datos= datos_api.json()

def menu():
    while True:
        try:
            print("Por favor, seleccione una opción:")
            print("1. Mostrar ubicaciones disponibles")
            print("2. Mostrar información meteorológica para una ubicación")
            print("3. Realizar análisis estadístico para una ubicación")
            print("4. Buscar información meteorológica para una ubicación en una fecha específica")
            print("5. Salir")
            opcion = int(input("Ingrese el número de la opción que desea: "))
            if opcion not in range(1,6):
                raise Exception
            break
        except:
            print("Por favor ingrese unicamente numeros enteros entre 1 y 5")
    return opcion 


def mostrar_ubicaciones():
    print("\n---- UBICACIONES DISPONIBLES ----")
    for x in datos:
        for k,v in x.items():
            if k == 'location_name':
                print("\t",v)


def mostrar_informacion_ubicacion():
    mostrar_ubicaciones
    for ubicacion_actual in datos:
        if ubicacion_actual['location_name'].lower() == ubicacion.lower():
            print(datos[ubicacion]["location_measurements"])
            break
      

'''if opcion == "1":
        mostrar_ubicaciones(datos_meteorologicos)
    elif opcion == "2":
        ubicacion = input("Ingrese el nombre de la ubicación: ")
        mostrar_informacion_ubicacion(datos_meteorologicos, ubicacion)
    elif opcion == "3":
        ubicacion = input("Ingrese el nombre de la ubicación: ")
        analisis_estadistico(datos_meteorologicos, ubicacion)
    elif opcion == "4":
        ubicacion = input("Ingrese el nombre de la ubicación: ")
        fecha = input("Ingrese la fecha en formato 'AAAA-MM-DD': ")
        busqueda_por_fecha(datos_meteorologicos, ubicacion, fecha)
    elif opcion == "5":
        print("Gracias por utilizar el sistema de visualización de datos meteorológicos.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
'''


def main():
    while True:
        opcion = menu()
        

        if opcion == 1:
           mostrar_ubicaciones()
        elif opcion == 2:
            ubicacion = input("Ingrese el nombre de la ubicación: ")
            mostrar_informacion_ubicacion()#(datos, ubicacion)
        elif opcion == 3:
            ubicacion = input("Ingrese el nombre de la ubicación: ")
            #analisis_estadistico(datos_meteorologicos, ubicacion)
        elif opcion == 4:
            ubicacion = input("Ingrese el nombre de la ubicación: ")
            fecha = input("Ingrese la fecha en formato 'AAAA-MM-DD': ")
           # busqueda_por_fecha(datos_meteorologicos, ubicacion, fecha)
        elif opcion == 5:
            print("Gracias por utilizar el sistema de visualización de datos meteorológicos.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    
main()
    




