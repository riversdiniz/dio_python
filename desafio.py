MENU = """ 

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

SALDO = 0
LIMITE = 500
EXTRATO = ""
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3

while True:

    OPCAO = input(MENU)

    if OPCAO == "D":
        VALOR = float(input("Informe o valor do deposito: "))

        if VALOR > 0:
            SALDO += VALOR
            EXTRATO += f"Deposito: R$ {VALOR:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif OPCAO == "S":
        VALOR = float(input("Informe o valor do saque: "))

        EXCEDEU_SALDO = VALOR > SALDO

        EXCEDEU_LIMITE = VALOR > LIMITE
        
        EXCEDEU_SAQUES = NUMERO_SAQUES >= LIMITE_SAQUES

        if EXCEDEU_SALDO:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif EXCEDEU_LIMITE:
            print("Operação falhou! O valor do saque excedeu o limite.")

        elif EXCEDEU_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif VALOR > 0:
            SALDO -= VALOR
            EXTRATO += f"Saque: R$ {VALOR:.2f}\n"
            NUMERO_SAQUES += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif OPCAO == "E":
        print("\n================= EXTRATO =================")
        print("Não foram realizadas movimentações." if not EXTRATO else EXTRATO)
        print(f"\nSaldo: R$ {SALDO:.2f}")
        print("=============================================")

    elif OPCAO == "Q":
        print("\n================= VOLTE SEMPRE! =================")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")