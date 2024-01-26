def es_bisiesto (anio):
    if (anio % 4 == 0 and anio % 100 != 0)or (anio % 400 == 0):
        return True
    else:
        return False
    
if __name__ == "__main__":
    try:
        anio_ingresado = int(input("ingresa el año"))
        if es_bisiesto(anio_ingresado):
            print (f"(anio_ingresado)es un año bisiesto.")
    except ValueError:
        print("por favor ingresa un año valido")            
