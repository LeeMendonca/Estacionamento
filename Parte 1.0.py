'''
Programa de Pagamento de Estacionamento - Parte 1

Você foi contratada para criar uma máquina de pagamento de estacionamento para um shopping. Para se organizar, você decide primeiro fazer a parte do programa que define se a pessoa ainda está na tolerância de tempo (e não precisa pagar nada). 

Crie um programa que apresenta uma mensagem pedindo para inserir o cartão e então recebe o tempo desde que a pessoa entrou no estacionamento com seu carro. Se o tempo for menor que 15 minutos, avise a pessoa que ela não precisa pagar.

'''

print('Insira o cartão de estacionamento!')

tempo = int(input('Insira o tempo em minutos: '))

if tempo < 15:
  print('Você não precisa pagar o estacionamento :)')
else:
  print('Você deve pagar o estacionamento.')

print('\nFim do atendimento eletrônico.')
