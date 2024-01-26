import os

def celsius_a_fahrenheit(celsius): 
    return (celsius * 9/5) + 32 
def fahrenheit_a_celsius(fahrenheit): 
    return (fahrenheit - 32) * 5/9 

if __name__ == "__main__": 
    while True:
        try: 
            opcion = input("¿Quieres convertir de Celsius a Fahrenheit (C) o de Fahrenheit a Celsius (F)? ").upper() 
        
            if opcion == "C": 
                temperatura_celsius = float(input("Ingresa la temperatura en Celsius: ")) 
                resultado = celsius_a_fahrenheit(temperatura_celsius) 
                print(f"{temperatura_celsius} grados Celsius son {resultado} grados Fahrenheit.") 
            elif opcion == "F": 
                temperatura_fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: ")) 
                resultado = fahrenheit_a_celsius(temperatura_fahrenheit) 
                print(f"{temperatura_fahrenheit} grados Fahrenheit son {resultado} grados Celsius.") 
            else: 
                print("Por favor, ingresa una opción válida (C o F).")
                
        except ValueError:
            print("Por favor, ingresa una temperatura válida.")
