#int para float e vice versa
preco = 30
print(preco)

preco = float(preco)
print(preco)

preco = 30.50
print(preco)

preco = int(preco)
print(preco)

#coversao por divisao
preco = 10
print(preco)

print(preco / 2) #resultará em um float

print(preco // 2) # // é para dividir por um numero inteiro, então será 5/2 e não 5.0/2

#numerico para string
preco = 10.50
idade = 28

print(str(preco)) #converte o float 10.50 para uma string '10.5'

print(str(idade)) #converte o int 28 para uma string '28'

texto = f"idade {idade} preco {preco}"
print(texto) #idade e preco serão convertidos em string

#string para numerico
preco = '10.50'
idade = '28'

print(float(preco))

print(int(idade))

