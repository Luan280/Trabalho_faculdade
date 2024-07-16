def escolha_modelos():
    print("""ENTRE COM OS MODELOS DESEJADOS:
MCS - Camiseta Manga Curta Simples
MLS - Camiseta Manga longa Simples
MCE - Camiseta Manga Curta Com Estampa
MLE - Camiseta Manga Longa Com Estampa""")
    while True:
        # Entrada do modelos. Se o modelos for errado ele chama a função de novo.
        modelos = str(input(">>")).upper()

        if modelos == "MCS":
            return 1.80
        elif modelos == "MLS":
            return 2.10
        elif modelos == "MCE":
            return 2.90
        elif modelos == "MLE":
            return 3.20
        else:
            print("Escolha inválida. entre com o modelo novamente.")


def num_camisetas():
    while True:
        try:
            camisetas = int(input("Entre com o número de camisetas: "))
            print()
            # Estrutura de condições para saber o desconto a partir da quantidade das camisetas.
            if camisetas < 20:
                desconto = 0
            elif camisetas < 200:
                desconto = 5
            elif camisetas < 2000:
                desconto = 7
            elif camisetas <= 20000:
                desconto = 12
            else:
                print("Não aceitamos tantas camisetas de uma vez.")
                print("Por favor, entre com o número de camisetas novamente.")
                print()
                continue
            # Calculo para saber o desconto das camisetas
            camisetas = camisetas - (camisetas * desconto) / 100
            return camisetas
        except ValueError:
            print("Por favor, insira um valor numérico válido.")


def frete():
    print("""Escolha o tipo de frete:
1 - Frete por transportadora - R$ 100.00
2 - Frete por Sedex - R$ 200.00
0 - Retirar pedido na fábrica - R$ 0.00""")

    # Entrada do frete. Se o valor não for "0, 1, 2" ele chama a função de novo.
    valor = int(input(">>"))
    if valor != 1 and valor != 2 and valor != 0:
        print('Digite somente "0, 1, 2".')
        frete()
    if valor == 0:
        return 0
    elif valor == 1:
        return 100
    elif valor == 2:
        return 200


# Programa príncipal
print("BEM-VINDO A FÁBRICA DE CAMISETAS DO LUAN FERREIRA LIMA")
# Chamada de todas as funções.
valor_modelos = escolha_modelos()
valor_camisetas = num_camisetas()
valor_frete = frete()
valor_total = (valor_modelos * valor_camisetas) + valor_frete

print(f"Total: R$ {valor_total:.2f} (Modelo: {valor_modelos:.2f} * Quantidade(com desconto): {valor_camisetas:.2f} + frete: {valor_frete:.2f}")
