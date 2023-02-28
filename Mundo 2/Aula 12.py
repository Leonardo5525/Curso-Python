nome = input('Digite um nome = ')

if nome == 'leo':
    print('Gostei do seu nome')
elif nome == 'joao' or nome == 'jose' or nome == 'maria':
    print('Nome comum no Brasil')
elif nome == 'vitoria':
    print('Nome feminino bonito')

print('Tenha um bom dia'.format(nome))