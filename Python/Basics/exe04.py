'''Objetivo: Praticar o uso de operadores aritméticos com números de ponto flutuante (float) e formatar a saída de dados.
Descrição: Crie um script que:
Pergunte o preço original de um produto.
Pergunte o percentual de desconto (por exemplo, 15 para 15%).
Calcule o valor do desconto.
Calcule o novo preço do produto com o desconto aplicado.
Exiba o preço original, o valor do desconto e o preço final.'''

original_price = float(input("What is the product's price? $"))
discount_percentage = float(input("What is the discount percentage? %"))
discount_value = original_price * (discount_percentage / 100)
final_price = original_price - discount_value

print(f"\n--- Receipt ---")
print(f"Original Price: ${original_price:.2f}")
print(f"Discount ({discount_percentage:.2f}%): -${discount_value:.2f}")
print(f"Final Price: ${final_price:.2f}")