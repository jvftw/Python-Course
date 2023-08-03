"""
estruturas condicionais
permitem o desvio de fluxo de controle, quando determinadas
expressões logicas são atendidas

if
else
elif

"""

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando Saque")

if saldo < saque:
    print("Saldo insuficiente")

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

opcao = int(input("Informe uma opção:\n [1] Sacar \n [2] Extrato\n"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato")

else:
    print("Opção Invalida")

"""
if alinhado

"""
contaNormal = True
contaUni = False

saldo = 4000
saque = 4500
cheque = 450

if contaNormal:
    if saldo >= saque:
        print("Saque realzado com sucesso")
    elif saque <= (saldo + cheque):
        print("Saque realizado com uso do cheque")
    else:
        print("Saldo insuficiente")

elif contaUni:
    if saldo > saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")

else:
    print("Tipo de conta desconhecido")

"""

if ternario
3 partes
primeira parte = retorno caso a expressao retorne true
segunda parte = expressao logica
terceira = retorno caso a expressão não seja antendida

"""

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f'{status} ao realizar o saque')

"""
repetição

for -> usado para percorrer um objeto repetivel
for/else
range -> usado para produzir uma sequencia de numeros inteiros a partir de um inicio
para um fim (geralmente i e j)
range tem 3 args: stop (obrigatorio) start step (opcionais)

"""

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()
    print("Finalizado")

for numero in range(0, 11): #o 11 é exclusivo, então lista termina em 10
    print(numero, end=" ")

for numero in range(0,51,5): # 5 é o step, então é contado de cinco em cinco
    print(numero, end=" ")

"""

while -> usado para repetir um bloco de codigo varias vezes, usado quando não sabemos
quantas vezes o codigo tem que ser repetido
break -> quebra o loop
continue -> usado para pular execução

"""

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o Extrato")
else:
    print("Obrigado por usar nosso sistema")

while True:
    numero = int(input("Informe um numero: "))
    
    if numero == 10:
        break

    print(numero)