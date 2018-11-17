
def calcula_dobro(numero):
    return numero * 2

print(calcula_dobro(15))

print('')

def calcula_soma_numeros(**numeros):
    print(numeros)
    return sum(numeros.values())

print(calcula_soma_numeros(num1=5,num2=10,num3=20))