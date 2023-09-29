# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

quilos = float(input('Digite a quantidade de peixes que pegou (Kg): '))

if quilos > 50:
    excedente = quilos - 50
    multa = 4 * excedente
    print(f'Você pescou {quilos}Kg, pegou {excedente}Kg a mais que 50kg, a multa é de R${multa}')
else:
    print(f'Você pescou {quilos}Kg, e como não é maior que 50Kg, não houve multa.')