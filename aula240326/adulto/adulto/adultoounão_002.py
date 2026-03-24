"""
Programa adulto ou não 
Descrição: Este programa pergunta a idade de uma pessoa, se idade for maior ou igual que 18 anos o programa imprime o texto "Oi! Você é um adulto". Caso contrário retornará "Oi! Você é menor de idade."
Alteração: Nessa versão foi utilizado a variável "texto" para imprimir a resposta.
Autor: Gabriel G. Ghignatti
Data: 24/03/2026
Versão: 0.0.2
"""

# Alocação de Memória
idade = 0
texto = ""
# Entrada de Dados
idade = int(input("\nQual a sua idade? "))

# Processamento de Dados
if idade>=18:
    texto="\nOi! Você é um adulto."
else:
    texto="\nOi! Você é menor de idade."

# Saída de Dados
print(texto)