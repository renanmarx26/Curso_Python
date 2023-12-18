menu = input(f"""
            Digite a opção desejada:
==============================================
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
""")

menu = 1
menu = 2
menu = 3
menu = 0

menu = True

saldo_conta = 0
extrato_conta = ""
saque = 0
NUMEROS_SAQUE = 3
LIMITE_SAQUE = 500
valor_deposito = ""

while True:

    if menu == 1:
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        if valor_deposito > 0:
            saldo_conta += valor_deposito
            extrato_conta += float(print(f'Foi depositado: R${valor_deposito}.'))



    elif menu == 2:
        saque = float(input("Digite quanto deseja sacar: "))
     
        SEM_SALDO_SAQUE = saque > saldo_conta
        SEM_LIMITE_SAQUE = saque > LIMITE_SAQUE
        SEM_SAQUE_DIARIO = NUMEROS_SAQUE >= LIMITE_SAQUE

        if SEM_SALDO_SAQUE:
            print("Você não possui saldo suficiente para sacar o dinheiro solicitado.")
        elif SEM_LIMITE_SAQUE:
            print("Você excedeu o limite do saque.")
        elif SEM_SAQUE_DIARIO:
            print("Você excedeu o limite de saques diários. Tente novamente amanhã.")
        elif saque > 0:
            saldo -= valor_deposito
            extrato+= float(print(f'Foi feito um saque de: R$ {saque}'))
            NUMEROS_SAQUE += 1

        else:
            print("Erro.Tente novamente.")


    elif menu == 3:
        print(f"""
            ******Bem vindo ao seu EXTRATO******)
        """)
        float(print(f'Seu saldo é: R$ {saldo}'))


    elif menu == 0:
        break



    else:
        print("Erro. Selecione uma opção válida.")
