# O for no python intera sobre a lista de alguma coisa

for i in range(10):
    print(i)

else:
    print('Fim do loop')
    print('')


lista1 = ['Maca', 'Banana', 'Limao']
lista2 = ['Tomate', 'Cebola', 'Cenoura']

for i, j in zip(lista1, lista2):
    print(i, j)
else:
    print('')

for i, j in enumerate(lista1):
    print(i, j)
else:
    print('')
