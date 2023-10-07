from funcoes import *
from os import system, name

def menu():
    print('1. Conversor de uma base para outra')
    print('2. Calcular expressão de diferentes bases')
    print('3. Complemento da base para sinal e magnitude')
    print('4. Sinal e magnitude para complemento da base')
    print('5. Conversor de um número em complemento para outro em base diferente')
    print('6. Conversor de uma base para outra de número fracionário')
    print('0. Para encerrar o programa')

    opcao = input('\nDigite sua opção: ')

    while opcao not in "0 1 2 3 4 5 6":
        opcao = input("Digite uma opção válida: ")

    return opcao


def clear():
    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')


if __name__ == "__main__":
    while int(opcao:=menu()):
        clear()
        if opcao == '1':
            num = input('Digite o número: ')
            base_num = int(input('Digite a base do número: '))
            base_destino = int(input('Digite a base de destino: '))
            resultado = converte(num, base_num, base_destino)

            print(f"O número {num} base {base_num} na base {base_destino} é igual a {resultado}.")
        elif opcao == '2':
            print("Números na forma ('num',base) sem espaço dentro dos parênteses")
            print("Exemplo de expressão: ('A1',16) * ('13',10) / ('1001',2)\n")
            expressao = input("Digite a expresão: ")
            base = int(input("Base do resultado: "))
            resultado = resultado_expressao(expressao, base)

            print(f'{expressao} = ({resultado},{base})')
        elif opcao == '3':
            num = input('Digite o número em complemento da base: ')
            base = int(input('Digite a base do número: '))
            resultado = complemento(num, base)

            print(f"O número {num} em complemento da base é igual a {resultado} em sinal e magnitude.")
        elif opcao == '4':
            num = input('Digite o número negativo em sinal e magnitude sem o (-): ')
            base = int(input('Digite a base do número: '))
            resultado = complemento(num, base)

            print(f"O número {num} em sinal e magnitude é igual a {resultado} em complemento da base.")
        elif opcao == '5':
            num = input('Digite o número em complemento da base: ')
            base_num = int(input('Digite a base do número: '))
            base_destino = int(input('Digite a base do resultado final: '))
            resultado = converte_em_complemento(num, base_num, base_destino)

            print(f"O número {num} base {base_num} na base {base_destino} é igual a {resultado} em complemento da base.")
        elif opcao == '6':
            num = input('Digite o número fracionário: ')
            base_num = int(input('Digite a base do número: '))
            precisao = int(input('Digite a quantidade de casas decimais do resultado: '))
            base_destino = int(input('Digite a base de destino: '))
            resultado = converte_fracionario(num, base_num, precisao, base_destino)

            print(f"O número {num} base {base_num} na base {base_destino} é igual a {resultado}.")

        input("Pressione enter para voltar ao menu...")
        clear()