def es_palindromo(texto):
    # Convertir el texto a minúsculas y eliminar espacios en blanco 
    texto = texto.lower().replace(" ", "") 
    # Verificar si la versión invertida del texto es igual al original 
    return texto == texto[::-1]
 
if __name__ == "__main__": 
    palabra_frase = input("Ingresa una palabra o frase: ") 
    if es_palindromo(palabra_frase): 
        print(f"{palabra_frase} es un palíndromo.") 
    else: 
        print(f"{palabra_frase} no es un palíndromo.")
