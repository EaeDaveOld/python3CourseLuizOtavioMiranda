# while - break & continue

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Aqui eu vou voltar para o início do laço')
        continue

    print(contador)

    if contador == 40:
        break  # Termina o laço

print('Acabou')
