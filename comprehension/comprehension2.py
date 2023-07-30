dobroDosPares = [i * 2 for i in range(10) if i % 2 == 0]
#multiplica todos os numeros de 0 a 9 por 2 e printa, caso o numero entre 0 e 9 seja par, sera printado a multiplicação por 2
print(dobroDosPares)

#outra versão
dobroDosPares = []
for i in range(10):
    if i % 2 == 0:
        dobroDosPares.append(i * 2)
print(dobroDosPares)