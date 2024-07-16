print("BEM-VINDOS A LOJA DO LUAN FERREIRA LIMA")
# Entrada do valor do pedido e a quantidade de parcelas.
valorDoPedido = float(input("Entre com o valor do produto R$: "))
quantidadeParcela = int(input("Entre com a quantidade de parcelas: "))

# Estrutura de condições para definir o juros que o produto vai receber.
if quantidadeParcela < 4:  # certo
    juros = 0

elif 4 <= quantidadeParcela <= 6:
    juros = (valorDoPedido * 4) / 100

elif 6 <= quantidadeParcela <= 9:
    juros = (valorDoPedido * 8) / 100

elif 9 <= quantidadeParcela <= 13:
    juros = (valorDoPedido * 16) / 100

else:
    juros = (valorDoPedido * 32) / 100

# Calculo para definir o valor de cada parcela e o valor do produto com o juros incluso.
valorDaParcela = (valorDoPedido + juros) / quantidadeParcela
valorTotalParcelado = valorDaParcela * quantidadeParcela

print(f"O valor das parcelas é de: R${valorDaParcela:.2f} ")
print(f"O valor Total parcelado é de: R${valorTotalParcelado:.2f}")
