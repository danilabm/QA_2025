# Entrada do nome do aluno
nome_aluno = input("Digite o seu nome: ")

# Solicitação das 4 notas, com textos diferentes para cada input
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Cálculo da média aritmética
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibindo a mensagem final com a média
print(f"\nOlá, {nome_aluno}! Sua média é: {media:.1f} pontos")
