casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário? '))
anos = float(input('Em quantos anos pretende quitar a casa? '))

mes = anos * 12
parcela = casa/ mes
diferenca = salario * 0.3
print(f'{parcela:.2f}')
print(diferenca)

if parcela <= diferenca:
    print('Empréstimo concedido')
else:
    print('Empréstimo NEGADO')