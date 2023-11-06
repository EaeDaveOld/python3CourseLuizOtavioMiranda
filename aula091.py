# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return 'Fim do laço'


gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)
