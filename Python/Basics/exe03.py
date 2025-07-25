'''Descrição: Crie um script que:
Defina duas variáveis, a e b, com valores inteiros de sua escolha (por exemplo, a = 10 e b = 20).
Mostre os valores originais de a e b.
Troque os valores entre as duas variáveis, de modo que a passe a ter o valor de b, e b passe a ter o valor de a.
Mostre os valores de a e b após a troca.'''

a = int(input("Type a number: "))
b = int(input("Type another number: "))
print(f"A = {a} --- B = {b}")
c = a
a = b
b = c
print(f"Swapped values:  A = {a} and B = {b}") 