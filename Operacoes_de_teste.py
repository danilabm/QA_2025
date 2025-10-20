# Entrada do valor numérico
valor = float(input("Digite um valor numérico: "))

# Operações matemáticas
dobro = valor * 2
triplo = valor * 3
quadrado = valor ** 2
raiz_quadrada = valor ** 0.5
raiz_cubica = valor ** (1/3)

# Exibindo os 5 resultados
print(f"\nResultados para o valor {valor}:")
print(f"1. Dobro: {dobro}")
print(f"2. Triplo: {triplo}")
print(f"3. Ao quadrado: {quadrado}")
print(f"4. Raiz quadrada: {raiz_quadrada:.2f}")
print(f"5. Raiz cúbica: {raiz_cubica:.2f}")
