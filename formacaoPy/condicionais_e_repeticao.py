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

"""

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        