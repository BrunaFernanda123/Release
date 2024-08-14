estoque = {
    "tomate":[1000, 2.30],
    "alface":[500, 0.45],
    "batata":[2001, 1.20],
    "feijão":[100, 1.50],
}
total = 0
print("vendas:/n")
while True:
      produto = input('nome do produto (fim para sair)')
      if produto == "fim":
          break
      if produto in estoque:
          quantidade = int(input("Quantidade"))
          if quantidade <= estoque[produto][0]:
              preço = estoque[produto][1]
              custo = preço * quantidade
              print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f} ")
              estoque[produto][0] -= quantidade
              total += custo
          else:
         print("quantidade solicitada não disponível")
      else:
         print("nome de produto inválido")
         print(f" Custo total: {total:21.2f}/n")
          print("estoque:/n")
      for chave, dados in estoque.items():
          print("descrição: ", chave)
          print("quantidade: ", dados[0])
          print(f"preço: {dados[1]:6.2f}/n")

