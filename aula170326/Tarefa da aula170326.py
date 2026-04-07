# Tarefa da aula 17/03/2026
# Descrição: Este programa lê dois números inteiros digitados pelo usuário e calcula a subtração, multiplicação, divisão, exponenciação e radiciação.
# Autor: Gabriel G. Ghignatti
# Data: 17/03/2026
# Versão: 0.0.2
# Notas de Correção: Foi adicionado um parênteses no fim do print.

# Alocação de Memória
numero_1 = 0.0

numero_2 = 0.0

sub= 0.0

mult = 0.0

div = 0.0

exp = 0.0

rad = 0.0

# Entrada de Dados
numero_1 = int(input("Qual o primeiro dígito? "))

numero_2 = int(input("Qual o segundo dígito? "))

# Processamento de dados
sub= numero_1 - numero_2

mult = numero_1 * numero_2

div = numero_1 / numero_2

exp = numero_1 ** numero_2

rad = numero_1 ** (1/numero_2)

# Saída de dados
print(f"O resultado da sua subtração foi {sub}, da multiplicação foi {mult}, da divisão foi {div}, da exponenciação foi {exp} e da radiciação foi {rad}.") # O comando do print estava incompleto gerando um erro na hora de printar a resposta.