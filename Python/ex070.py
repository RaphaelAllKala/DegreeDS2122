menorvalor = total = qpro1000 = 0
menorproduto = []
while True:
    resp = ' '
    produto = str(input("Qual o produto? ")).upper().strip()
    valor = float(input('Qual o valor?  '))
    total += valor
    if menorvalor == 0:
        menorvalor = valor
    if menorproduto == []:
        menorproduto =  produto
    if valor < menorvalor:
        menorvalor = valor
        menorproduto = produto
    if valor >1000:
        qpro1000 += 1
    while resp not in 'SN':
        resp = str(input('Deseja adcionar mais algum produto?  (S?N)')).upper().strip()[0]
    if resp == 'N':
            break
print(f'Total de compras = R${total}\n'
      f'{qpro1000} produto(s) acima de R$1000,00\n'
      f'O produto mais barato foi o {menorproduto}')
