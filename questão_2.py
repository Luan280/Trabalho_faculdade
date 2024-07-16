print("-----BEM-VINDO A LOJA DE MARMITAS DO LUAN FERREIRA LIMA----")
print("""-------------------------- CARDÁPIO -----------------------
-----------------------------------------------------------
---| TAMANHO | BIFE ACEBOLADO(BA) | FILÉ DE FRANGO(FF) |---
---|    P    |      R$ 16.00      |      R$ 15.00      |---
---|    M    |      R$ 18.00      |      R$ 17.00      |---
---|    G    |      R$ 22.00      |      R$ 21.00      |---""")

# A variável "acumulador" serve para receber a soma dos valores dos produtos.
# E foi declarada fora para pode ser usada dentro e fora do laço de repetição.
acumulador = 0
while True:
    # Verifica se a entrada é "BA" ou "FF". se não, da uma mensagem de erro.
    sabor = str(input("Entre com o sabor desejado (BA/FF): ")).upper()[0:2]
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente")
        print()
    else:
        # Verifica se a entrada é "P, M ou G". se não, da uma mensagem de erro.
        tamanho = str(input("Entre com um tamanho (P/M/G): ")).upper()[0]
        if tamanho != "P" and tamanho != "M" and tamanho != "G":
            print("Tamanho inválido. Tente novamente.")
            print()
        else:
            # Nessa estrutura verifica se é BA ou FF e da o valor de acordo com o tamanho.
            if sabor == "BA" and tamanho == "P":
                acumulador += 16
                valor = 16
                sabor = "BIFE ACEBOLADO"
            elif sabor == "BA" and tamanho == "M":
                acumulador += 18
                valor = 18
                sabor = "BIFE ACEBOLADO"
            elif sabor == "BA" and tamanho == "G":
                acumulador += 22
                valor = 22
                sabor = "BIFE ACEBOLADO"
            else:
                if sabor == "FF" and tamanho == "P":
                    acumulador += 15
                    valor = 15
                    sabor = "FILÉ DE FRANGO"
                elif sabor == "FF" and tamanho == "M":
                    acumulador += 17
                    valor = 17
                    sabor = "FILÉ DE FRANGO"
                elif sabor == "FF" and tamanho == "G":
                    acumulador += 21
                    valor = 21
                    sabor = "FILÉ DE FRANGO"
            print(f"Você pediu um {sabor} no tamanho {tamanho}: R$ {valor:.2f}")
            print("-=" * 29)
            # A variável "continuar" serve como parâmetro para interromper a estrutura de repetição.
            continuar = str(input("Deseja mais alguma coisa? (S/N): ")).upper()[0]
            print("-=" * 29)
            if continuar == "N":
                print(f"O valor total a ser pago: R${acumulador:.2f}")
                break
            else:
                continue
