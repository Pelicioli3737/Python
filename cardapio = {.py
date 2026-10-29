cardapio = {
    "x-salada": 18.0,
    "batata": 12.0,
    "suco": 8.0,
    "pudim": 10.0,
}
print("Bem-vindo ao nosso restaurante!")
print("Nosso cardápio:")
for item, preco in cardapio.items():
    print(f"{item}: R${preco:.2f}")
print("Digite o nome do item que deseja pedir:")
pedido = str(input())
if pedido in cardapio:
    print(f"Você pediu {pedido}. O preço é R${cardapio[pedido]:.2f}.")
else:
    print("Item não encontrado no cardápio.")
