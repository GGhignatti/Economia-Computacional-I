""" 
Programa: Quadrado

Descrição: Este programa calcula a área de um quadradado baseado nos valores dados pelos usuários.
Autor: Gabriel G. Ghignatti
Data: 10/10/2026
Versão: 0.1.0
"""

# Alocação de Memória
lado = 0.0
area = 0.0

# Entrada de Dados
lado = float(input("\nDigite o lado do quadrado que você quer calcular a área: "))

# Processamento de Dados
area = lado**2

# Saída de Dados
print(f"A área do quadrado de lado {lado} é igual {area}")
