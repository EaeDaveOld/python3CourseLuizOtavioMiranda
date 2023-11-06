import sys

# Generator expression, Iterables and Iterators
iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__()  # tem __iter__ e __next__
iterator = iter(iterable)  # tem __iter__ e __next__

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))  # - Bytes of memory (85176 Bytes)
print(sys.getsizeof(generator))  # - Bytes of memory (200 Bytes)

for n in generator:
    print(n)
