filaF=["O","O","x","O","O","O","O","O","O","x","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]
filaE=["O","O","x","O","O","O","O","O","O","x","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]
filaD=["O","O","x","O","O","O","O","O","O","x","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]

filaC=["O","O","O","O","O","O","O","O","O","x","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]
filaB=["O","O","O","O","O","O","O","O","O","x","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]
filaA=["O","O","O","O","O","O","O","O","O","x","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]

valorAsientos=("Asiento común, $60.000 peso","Espacio adicional para piernas, $80.000 pesos","No reclina, $50.000 pesos")


def ComprarPasajes():
    while True:
        print(f"fila F",filaF)
        print(f"fila E",filaE)
        print(f"fila D",filaD)
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"fila C",filaC)
        print(f"fila B",filaB)
        print(f"fila A",filaA)

        fila=input("ingrese la fila a solicitar (debe ingresar solo la letra)").lower()
        try:
            if fila=="f":
                asiento=int(input("ingrese el asiento desde (1 a 33)"))
                try: 
                    if asiento==3 or asiento==10:
                        print("asiento ocupado")      
                    else: 
                        if asiento>=1 or asiento<33:
                            print("asiento disponible")
                            PosicionAsiento =["x"]
                            asiento=asiento-1
                            filaF.insert(asiento, PosicionAsiento)
                except ValueError:
                    print("ingrese solo los asientos") 
            elif fila=="e":
                asiento=int(input("ingrese el asiento desde (1 a 33)"))
                if asiento==3 or asiento==10:
                    print("asiento ocupado")      
                else: 
                    if asiento>=1 or asiento<33:
                        print("asiento disponible")
                        PosicionAsiento =["x"]
                        asiento=asiento-1
                        filaE.insert(asiento, PosicionAsiento)
            elif fila=="d":
                asiento=int(input("ingrese el asiento desde (1 a 33)"))
                if asiento==3 or asiento==10:
                    print("asiento ocupado")      
                else: 
                    if asiento>=1 or asiento<33:
                        print("asiento disponible")
                        PosicionAsiento =["x"]
                        asiento=asiento-1
                        filaD.insert(asiento, PosicionAsiento)
            elif fila=="c":
                asiento=int(input("ingrese el asiento desde (1 a 33)"))
                if asiento==10:
                    print("asiento ocupado")      
                else: 
                    if asiento<33:
                        print("asiento disponible")
                        PosicionAsiento =["x"]
                        asiento=asiento-1
                        filaC.insert(asiento, PosicionAsiento)
            elif fila=="b":
                asiento=int(input("ingrese el asiento desde (1 a 33)"))
                if asiento==10:
                    print("asiento ocupado")      
                else: 
                    if asiento>=1 or asiento<33:
                        print("asiento disponible")
                        PosicionAsiento = ["x"]
                        asiento=asiento-1
                        filaB.insert(asiento, PosicionAsiento)
            elif fila=="a":
                asiento=int(input("ingrese el asiento desde (1 a 33)"))
                if asiento==10:
                    print("asiento ocupado")      
                else: 
                    if asiento>=1 or asiento<33:
                        print("asiento disponible")
                        PosicionAsiento =["x"]
                        asiento=asiento-1
                        filaA.insert(asiento, PosicionAsiento)
            print("precio de asientos")
            print(valorAsientos)
            break
        except TypeError:
            print("ingrese las filas disponibles")
        









print("----------------------")
print("bienvenido a la linea aerea FLASH\n------------------------\na continuacion escoga una de las opciones disponibles\n-----------------------------")
opciones=int(input("(1)Comprar pasajes\n(2)Mostrar ubicaciones disponibles\n(3)Ver listado de pasajeros\n(4)Buscar pasajero\n(5)Reasignar asiento\n(6)Mostrar ganancias totales"))
if opciones==1:
    ComprarPasajes()