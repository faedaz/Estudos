'''Descrição: Crie um script que:
Pergunte ao usuário o ano atual.
Pergunte ao usuário o ano em que ele nasceu.
Calcule e exiba a idade do usuário (ou a idade que ele fará no ano corrente).'''

year = int(input("Type the current year: "))
birth_year = int(input("Type your birth year: "))
age = year - birth_year
print(f"Age: {age}")