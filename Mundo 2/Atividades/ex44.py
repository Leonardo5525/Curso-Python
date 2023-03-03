preco = float(input('Qual o valor do produto? '))
paga = input('Forma de pagamento? ')

dinheiro = preco - (preco*0.1)
cheque = preco - (preco*0.1)
cartao = preco - (preco*0.05)
cartao2 = preco
cartao3 = preco + (preco*0.2)

if paga == 'dinheiro':
    print(f'O total pago em dinheiro ou cheque é {dinheiro:.2f}')
elif paga == 'cheque':
    print(f'O total pago em dinheiro ou cheque é {dinheiro:.2f}')
elif paga == 'cartao':
    print(f'No cartão à vista, 5% de desconto, sendo no total {cartao:.2f}')
elif paga == 'cartao2':
    print(f'No cartão em 2 vezs, valor normal, sendo no total {cartao2:.2f}')
elif paga == 'cartao3':
    print(f'No cartão em 3 vezes, 20% de juros, sendo no total {cartao3:.2f}')
else:
    print('Compra cancelada')