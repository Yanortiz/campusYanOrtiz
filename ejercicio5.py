palabra_ingresada = input("Ingresa una palabra: ") 
palabra_invertida = palabra_ingresada[::-1] 
if palabra_ingresada == palabra_invertida: 
    print("La palabra es un palíndromo.") 
else: 
    print("La palabra no es un palíndromo.")
