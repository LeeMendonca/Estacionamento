'''
Programa de Pagamento de Estacionamento - Parte 2

Continuando com o nosso caixa de estacionamento, agora temos que indicar o valor que a pessoa precisa pagar:
Até 015 minutos → R$ 00,00 (cortesia)
Até 060 minutos → R$ 09,00
Até 180 minutos → R$ 12,00
Até 300 minutos → R$ 15,00
Acima de 300 minutos → R$ 17,00
'''

print('Insira o cartão de estacionamento!')
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
