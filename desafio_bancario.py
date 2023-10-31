menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = ""
saque_diaro = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if (opcao == 'd'):
        print('Opção de Depósito')
        valor = float(input('Qual o valor positivo para o depósito? '))
        if (valor > 0):
            saldo += valor
            extrato += f"Depósito de R${valor:.2f}\n"
        else:
            print('Valor inválido para depósito!')
    elif (opcao == 's'):
        print('Opção de Saque')
        valor = float(input('Qual o valor positivo para o saque? '))
        if (valor > saldo):
            print('Saldo insuficiente para saque!')
        elif (valor > limite):
            print('Limite diário de R$500,00 excedido!')
        elif (saque_diaro >= LIMITE_SAQUES):
            print('Limite diário de saque excedido!')
        elif (valor > 0):
            saldo -= valor
            saque_diaro += 1
            extrato += f"Saque de R${valor:.2f}\n"
        else:
            print('Valor inválido para saque!')
    elif (opcao == 'e'):
        print('Opção de Extrato')
        if not extrato:
            print("Nenhuma operação realizada!")
        else:
            print(extrato)
        print(f"Saldo: R${saldo:.2f}")
    elif (opcao == 'q'):
        break
    else:
        print('Opção inválida!')