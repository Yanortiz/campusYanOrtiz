import random 
def juego_adivinanza(): 
    numero_secreto = random.randint(1, 100) 
    intentos = 0 
    print("¡Bienvenido al juego de adivinanzas!") 
    print("Estoy pensando en un número entre 1 y 100") 
    while True:
        intento = int(input("Tu suposición: ")) 
        intentos += 1 
        if intento < numero_secreto:
            print("Muy bajo. Intenta de nuevo.") 
        elif intento > numero_secreto: 
            print("Muy alto. Intenta de nuevo.")
        else: 
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.") 
        break 

if __name__ == "__main__": juego_adivinanza()
