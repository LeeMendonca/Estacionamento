'''
Programa de Pagamento de Estacionamento - Parte 3.2

Tentativa 3
- Erro: usei if dentro do while para quando fosse digitado a forma correta.
- Consequência: se digitado 'dinheiro' como forma de pagamento, por exemplo, pulava da linha 22 para a 54. 
- Correção: para os casos em que a condição estiver correta, basta indentar fora do while, ou seja, sair do loop.
'''

tempo = int(input('Insira o tempo em minutos: '))

if tempo <= 15:
  print('Você não precisa pagar o estacionamento :)')
elif tempo <= 60:
  print('Você deve pagar R$9,00')
elif tempo <= 180:
  print('Você deve pagar R$12,00')
elif tempo <= 300:
  print('Você deve pagar R$15,00')
else:
  print('Você deve pagar R$17,00')

if tempo > 15:
  forma_pagamento = input('Insira a forma de pagamento: ')

  while forma_pagamento != "dinheiro" and forma_pagamento != "Dinheiro" and forma_pagamento != "cartão" and forma_pagamento != "Cartão" and forma_pagamento != "cartao" and forma_pagamento != "Cartao":
      forma_pagamento = input('Desculpe, não entendi. Informe a forma de pagamento (dinheiro ou cartão): ')
        
      if forma_pagamento == "dinheiro" or forma_pagamento == "Dinheiro":
        print('Atenção: Aceitamos apenas notas de R$5,00, R$10,00 e R$20,00.')
        print('Insira as notas.')
        print('Processando...')
        print('Pagamento finalizado')
        print('Obrigado, volte sempre!')   
      
      elif forma_pagamento == "cartão" or forma_pagamento == "Cartão" or forma_pagamento == "cartao" or forma_pagamento == "Cartao":
        cartao = input('Crédito ou débito? ')
  
        while cartao != "crédito" and cartao != "Crédito" and cartao != "credito" and cartao != "Credito" and cartao != "débito" and cartao != "Débito" and cartao != "debito" and cartao != "Debito":
          cartao = input('Desculpe, não entendi. Informe se será crédito ou débito: ')
          if cartao == "crédito" or cartao == "Crédito" or cartao == "credito" or cartao == "Credito":
            print('Insira o cartão.')
            print('Processando...')
            print('Pagamento finalizado no crédito.')
            print('Obrigado, volte sempre!')
  
          elif cartao == "débito" or cartao == "Débito" or cartao == "debito" or cartao == "Debito":
            print('Insira o cartão.')
            print('Processando...')
            print('Pagamento finalizado no débito.')
            print('Obrigado, volte sempre!')

else:  # if tempo < 15.
  print('Obrigado, volte sempre!')

print('\nFim do programa!')
