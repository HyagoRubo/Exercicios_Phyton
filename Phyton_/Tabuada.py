for numero_tabuada in range(1, 11):
    print(f"Tabuada do {numero_tabuada}:")

    for multiplicador in range(1, 11):
        resultado = numero_tabuada * multiplicador
        print(f"{numero_tabuada} x {multiplicador} = {resultado}")
    
    print()  # Adiciona uma linha em branco para separar as tabuadas
