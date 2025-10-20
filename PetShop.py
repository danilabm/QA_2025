# Entrada de dados: idade do pet em anos humanos
idade_humana = int(input("Digite a idade humana do seu pet (em anos): "))

# Entrada do nome do pet (opcional para personalizar a saída)
nome_pet = input("Digite o nome do seu pet: ")

# Entrada do porte do cachorro
porte = input("Digite o porte do cachorro (grande, medio ou pequeno): ").lower()

# Entrada da quantidade de banhos nos últimos 12 meses
quantidade_banhos = int(input("Digite quantos banhos o pet tomou nos últimos 12 meses: "))

# Cálculo da idade do pet em anos de cachorro
idade_cachorro = idade_humana * 7

# Definindo valores padrão de banho e custo
preco_banho = 0
custo_banho = 0

# Usando if, elif e else para definir os preços e custos com base no porte
if porte == "grande":
    preco_banho = 75
    custo_banho = 20
elif porte == "medio":
    preco_banho = 60
    custo_banho = 15
elif porte == "pequeno":
    preco_banho = 50
    custo_banho = 5
else:
    print("Porte inválido. Use apenas: grande, medio ou pequeno.")
    exit()  # Encerra o programa se o porte for inválido

# Cálculo do lucro: (preço - custo) * número de banhos
lucro_total = (preco_banho - custo_banho) * quantidade_banhos

# Exibindo os resultados
print(f"\nOlá, {nome_pet} tem {idade_cachorro} anos (idade de cachorro) e nos últimos 12 meses o lucro com este animal foi de R${lucro_total:.2f}")