'''
Programa de Pagamento de Estacionamento - Parte 3.3

Tentativa 4 - Ainda não deu certo.

Obs1: tive que pesquisar um pouco sobre listas, para dimunir o tamanho do código, mas dava para fazer sem. 
Encontrei esse site: https://blog.betrybe.com/python/python-list/#3

Obs2: utilizei a biblioteca time, só por diversão, para que o resultado na interface parecesse mais realista.
'''

import time

# Tempo gasto no estacionamento
tempo = int(input('Insira o tempo em minutos: '))

if tempo <= 15:
  print('\nVocê não precisa pagar o estacionamento :)')
elif tempo <= 60:
  print('\nVocê deve pagar R$9,00')
elif tempo <= 180:
  print('\nVocê deve pagar R$12,00')
elif tempo <= 300:
  print('\nVocê deve pagar R$15,00')
else:
  print('\nVocê deve pagar R$17,00')

# Formas que o cliente pode digitar
dinheiro = ['dinheiro', 'Dinheiro']
cartao = ['cartao', 'cartão', 'Cartao', 'Cartão']
credito = ['credito', 'crédito', 'Credito', 'Crédito']
debito = ['debito', 'débito', 'Debito', 'Débito']

# Caso o cliente digite algo fora das listas
novamente = 'Desculpe, não entendi. Tente novamente: '

# Forma de pagamento
if tempo > 15:
  forma_pagamento = input('\nInsira a forma de pagamento: ')

  while forma_pagamento not in dinheiro and forma_pagamento not in cartao:
    forma_pagamento = input(novamente)

# Pagamento em dinheiro
  if forma_pagamento in dinheiro:
    print('\nAtenção: Aceitamos apenas notas de R$5,00, R$10,00 e R$20,00.')
    time.sleep(3)
    print('\nInsira as notas.')
    time.sleep(4)
    print('Processando...')
    time.sleep(4)
    print('Pagamento finalizado.')

# Pagamento no cartão
  elif forma_pagamento in cartao:
    cartao = input('\nCrédito ou débito? ')

    while cartao not in credito and cartao not in debito:
      cartao = input(novamente)

    if cartao in credito:
      print('\nInsira o cartão.')
      time.sleep(3)
      print('Processando...')
      time.sleep(4)
      print('Pagamento finalizado no crédito.')

    elif cartao in debito:
      print('\nInsira o cartão.')
      time.sleep(3)
      print('Processando...')
      time.sleep(4)
      print('Pagamento finalizado no débito.')

print('\nObrigado, volte sempre!')
