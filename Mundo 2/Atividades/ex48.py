s = 0
for c in range (0, 500):
  if c%2 == 1 and c%3 == 0:
    print (c)
    s = s + c
print(f'O total da soma entre os impares e divisíeveis por 3 = {s}')