# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# Tamanho da área em metros quadrados
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Taxa de cobertura da tinta (litros por metro quadrado)
taxa_cobertura = 1 / 3

# Capacidade de uma lata de tinta (litros)
capacidade_lata = 18

# Preço de uma lata de tinta
preco_lata = 80.0

# Calcula a quantidade de litros de tinta necessária
litros_necessarios = area * taxa_cobertura

# Calcula a quantidade de latas de tinta necessárias
latas_necessarias = litros_necessarios / capacidade_lata

# Arredonda para cima para garantir que você compre pelo menos uma lata completa
latas_necessarias = int(latas_necessarias)
if litros_necessarios % capacidade_lata > 0:
    latas_necessarias += 1

# Calcula o preço total
preco_total = latas_necessarias * preco_lata

# Exibe os resultados
print(f"Você precisará de {latas_necessarias} latas de tinta.")
print(f"O preço total será de R${preco_total:.2f}")