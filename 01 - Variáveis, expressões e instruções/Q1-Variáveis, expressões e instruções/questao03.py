#Susu terminou sua tarefa de matemática e para revisar mais um pouco o conteúdo ela 
# resolveu aplicar vários números em uma expressão numérica que ela mesma criou: 
# para cada número x, primeiro multiplica-se x por 2, desse resultado subtrai-se 
# 5 e por último acrescenta-se 2^x. Escreva um programa que recebe um inteiro x, 
# o aplica na expressão de Susu e retorna o resultado.

# A Entrada consiste de: x , um número inteiro positivo.

# A Saída deve apresentar: Um número inteiro, o resultado da expressão numérica.

x = input()
x = int(x)

x = (x * 2) - 5 + (2 ** x)
print (x)