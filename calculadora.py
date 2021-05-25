print('------------------')
print('CALCULADORA')
print('------------------')

#declara função
def calcular():
    operacao = input('''
Por favor, digite a operação matemática que você gostaria de completar:
+ para adição
- para subtração
/ para divisão
* para multiplicação 
''')
 
    numero1 = int(input('Digite o seu primeiro numero: '))
    numero2 = int(input('Digite o seu segundo numero: '))
 
#adição
    if operacao == '+':
        print('{} + {} =' .format(numero1, numero2))
        print(numero1 + numero2)
 
#subtração
    elif operacao == '-':
        print('{} - {} =' .format(numero1, numero2))
        print(numero1 - numero2)
 
#divisão
    elif operacao == '/':
        print('{} / {} =' .format(numero1, numero2))
        print(numero1 / numero2)
 
#multiplicação
    elif operacao == '*':
        print('{} * {} =' .format(numero1, numero2))
        print(numero1 * numero2)
 
    else:
        print('Você não digitou um operador válido, execute o programa novamente')
 
    again()
 
#Defina a função again() para perguntar ao usuário se ele deseja usar a calculadora novamente
 
def again():
  #Obtenha a opinião do usuário
    calc_again = input('''Você quer calcular de novo? Pressione S para sim e N para não
''')
#se o usuário pressionar S, run a função calcular
    if calc_again.upper() == 'S':
        calcular()
#se o usuário pressionar N, dê adeus ao usuário e encerre o programa
    elif calc_again.upper() == 'N':
        print('Te vejo depois')
#se o usuário pressionar outra tecla, reinicie a função
    else:
        again()
 
calcular()