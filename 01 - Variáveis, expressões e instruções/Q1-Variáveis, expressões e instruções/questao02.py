# Drikinha gosta de bolos de vários sabores. Uma vez por semana ela vai em uma padaria 
# perto de casa e pede x pedaços de bolo de algum sabor, o pedaço de bolo tem o valor 
# fixo de 3.25 reais, independentemente do sabor. Escreva um programa que recebe o sabor do 
# bolo e a quantidade de pedaços que Drikinha irá comprar e retorne a frase do atendente: 
#
# "Foram x pedaços de bolo de s, então fica z reais". 
# Onde x é a quantidade de pedaços, s o sabor do bolo e z o total da compra de 
# Drikinha em reais. Imprima o valor da compra com apenas duas casas após a vírgula.

# A Entrada consiste de: Uma string e um número inteiro positivo, 
# representando o sabor do bolo e quantidade de pedaços respectivamente.

# A Saída deve apresentar: Uma string, como especificado no enunciado.

sabor, qtdeBolo = input().split() #input().split() le mais de um valor na mesma linha
qtdeBolo = int(qtdeBolo) #converte a string em um int

print (f'Foram {qtdeBolo} pedaços de bolo de {sabor}, então fica {qtdeBolo * 3.25:.2f} reais')