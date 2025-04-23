# A Entrada consiste de:
# Uma string S contendo todo o texto da postagem.

# A Saída deve apresentar:
# Na primeira linha, o pior tempo de leitura estimado em minutos sob a 
# seguinte formatação: "Pior dos casos: PC", onde PC é um número real 
# (de ponto decimal) que representa o pior tempo estimado com três casas 
# decimais de precisão.
# Na segunda linha, o melhor tempo de leitura estimado em minutos sob a seguinte 
# formatação: "Melhor dos casos: MC ", onde MC é um número real que representa o 
# melhor tempo estimado com três casas decimais de precisão.

S = input()
qtdeChars = len(S)

PC = (qtdeChars / 1200)
MC = (qtdeChars / 1550)

print(f'Pior dos casos: {PC:.3f}')
print(f'Melhor dos casos: {MC:.3f}')