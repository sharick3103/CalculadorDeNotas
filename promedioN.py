import time

while True:
    print("Introduce tus notas:")
    
    numero1 = float(input("Ingresa tu primera nota "))
    numero2 = float(input("Ingresa tu segunda nota: "))
    numero3 = float(input("Ingresa tu tercera nota: "))
     
    notas = numero1 , numero2 , numero3
    print("Tus notas son {}".format(notas))
    print('''
        1. Sí
        2. No
        3. Salir
        ''')
        
    respuesta = int(input("Opción (1,2,3): "))
    
    match respuesta:
    

        case 1:
            promedio = round((numero1 + numero2 + numero3) / 3 ,2)
            notas = numero1 , numero2 , numero3
            time.sleep(1)
            print("El promedio de tus notas es: {}".format(promedio))
            break
                
        case 2:
            print("Vuelve a ingresar tus notas")
            continuecd
            
        case _:
            break

    



