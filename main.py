from datetime import datetime

# Pergunta o nome
nome = input("Qual é o seu nome? ")

# Pergunta a data de nascimento
data_nascimento_str = input("Qual é a sua data de nascimento? (dd/mm/aaaa) ")

# Converte a string da data de nascimento em um objeto datetime
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Data Atual
data_atual = datetime.now()

# Calcula a idade
idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

# Exibe o cumprimento e a idade
print(f"Olá, {nome}! Você tem {idade} anos.")