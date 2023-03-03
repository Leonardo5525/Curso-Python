frase = input('Escreva uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#Nesse caso o inverso será uma variável a qual o valor será atribuído posteriormente após o "for letra in range, de modo que seja uma a frase inversa, utilizando dessa variável para comparar com outra."
inverso = ''
# Por isso que da o valor da variável "inverso" de vazio, pois sempre deve se atribuir o valor a uma variável para utiliza-la, sendo o vazio o equivalente a zero como no caso de problemas matemáticos. Sendo necessário começar do "-1" para que não começasse do "vazio" na inversão, o que faria o resultado dar errado, pois se utilizou do 'strip' e do 'join' acima
for letra in range (len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)

if junto == inverso:
    print ('A frase é um palindromo')
else:
    print('Frase não é um palindromo')
    
