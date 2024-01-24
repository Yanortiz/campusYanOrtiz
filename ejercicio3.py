eleccion_comida = input("¿Qué tipo de comida prefieres? (italiana, mexicana, china): ") 
if eleccion_comida.lower() =="italiana": 
    print("Te recomendaría probar 'La piza' para disfrutar de auténtica comida italiana.") 
if eleccion_comida.lower() == "mexicana": 
    print("¡'El Taquito' es una excelente opción para disfrutar de auténtica comida mexicana!") 
if eleccion_comida.lower() == "china": 
    print("Para sabores chinos auténticos, te sugiero 'Gran Muralla'.") 
else: print("Lo siento, no conozco restaurantes de ese tipo de comida.")
