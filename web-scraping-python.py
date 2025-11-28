#Simulação simples do preço vindo do site
produto = "Café Extra Forte 500g"
preco_atual = 17.90

#Entrada do usuário
preco_desejado = float(input("Digite o preço que você acha justo: "))

#Decisão
if preco_atual <= preco_desejado:
    print("Pode comprar, o preço está bom!")
else:
    print("Ainda está caro, melhor esperar.")

#Saída final
print("\nResumo:")
print("Produto:", produto)
print("Preço atual:", preco_atual)
print("Preço desejado:", preco_desejado)
