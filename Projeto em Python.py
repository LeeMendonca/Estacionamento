# PROGRAMA DE PAGAMENTO DE ESTACIONAMENTO
import time
import os

# Constantes
FORMAS_PAGAMENTO = ['dinheiro', 'cartão', 'cartao']
OPCOES_CARTAO = ['crédito', 'credito', 'débito', 'debito']

# Função: limpa o terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função: calcula o valor a pagar
def calcular_valor(minutos):
    if minutos <= 15:
        return 0.00
    elif minutos <= 60:
        return 9.00
    elif minutos <= 180:
        return 12.00
    elif minutos <= 300:
        return 15.00
    else:
        return 17.00

# Função: simula o pagamento
def processar_pagamento(fp, mensagem):
    print('\nIniciando pagamento...')
    if fp == 'dinheiro':
        print('Aceitamos apenas notas de R$5,00, R$10,00 e R$20,00.')
        print('Aguardando notas...')
    else:
        print('Insira ou aproxime o cartão...')
    time.sleep(2)
    print('Processando...')
    time.sleep(2)
    print(mensagem)

# Função: entrada segura de inteiro
def tempo(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Entrada inválida. Digite apenas números inteiros.')

# Função principal de atendimento
def atendimento():
    minutos = tempo('\nDigite o tempo de permanência (em minutos): ')
    while minutos < 0:
        print('Tempo não pode ser negativo.')
        minutos = tempo('Digite o tempo de permanência (em minutos): ')

    valor = calcular_valor(minutos)

    if valor == 0:
        print('\nEstacionamento gratuito! Você permaneceu até 15 minutos.')
    else:
        print(f'\nValor a pagar: R${valor:.2f}')

        # Escolha da forma de pagamento
        fp = input('\nInforme a forma de pagamento (dinheiro ou cartão): ').strip().lower()
        while fp not in FORMAS_PAGAMENTO:
            fp = input('Forma inválida. Tente novamente: ').strip().lower()

        if fp in ['cartão', 'cartao']:
            cartao = input('Crédito ou débito? ').strip().lower()
            while cartao not in OPCOES_CARTAO:
                cartao = input('Opção inválida. Tente novamente: ').strip().lower()

            if cartao in ['crédito', 'credito']:
                mensagem = 'Pagamento finalizado no crédito.'
            else:
                mensagem = 'Pagamento finalizado no débito.'
        else:
            mensagem = 'Pagamento finalizado em dinheiro.'

        processar_pagamento(fp, mensagem)

    print('\nOperação concluída.')
    print("Obrigado! Ferreira's Park Shopping agradece a sua visita!")

# Função que organiza o ciclo de atendimento
def main():
    print('=' * 50)
    print("Bem-vindo(a) ao estacionamento do Ferreira's Park Shopping")
    print('=' * 50)

    while True:
        atendimento()
        continuar = input('\nDeseja realizar outro atendimento? (s/n): ').strip().lower()
        if continuar != 's':
            print('\nEncerrando o sistema. Até a próxima!')
            break
        limpar_tela()

main()