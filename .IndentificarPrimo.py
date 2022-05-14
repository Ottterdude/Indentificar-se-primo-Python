num = int(input('Digite um número '))
dim = num - 1
resultado = True
while dim > 1:
    if num % dim == 0:
        resultado = False
        break
    else:
        dim -= 1
if resultado:
    print('O número que você digitou é primo!!!')
else:
    print('O número que você digitou não é primo')
