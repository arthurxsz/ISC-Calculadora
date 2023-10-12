str_digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digitos = {k: v for v, k in enumerate(str_digitos)}


def converte(num, base_num, base_destino=10):
    """
    Converte um número de uma base para outra

    Parâmetros:
        num (str): Número que deverá ser convertido.
        base_num (int): Base de num.
        base_destino (int): Base do resultado.

    Retorna:
        converte(num, base_num, base_destino): Um número na base_destino, tendo como entrada num na base_num.
    """
    resultado = 0
    if not type(num) == str:
        num = str(num)
        
    for i, d in enumerate(num):
        resultado += digitos[d]* base_num**(len(num)-1-i)

    if base_destino == 10:
        return str(resultado)
    else:
        lista = []
        while resultado > 0:
            lista.append(resultado%base_destino)
            resultado = resultado//base_destino
        
        resultado = ''
        for d in lista:
            resultado += list(digitos.keys())[list(digitos.values()).index(d)]

        return resultado[::-1]


def converte_fracionario(num, base_num, precisao, base_destino):
    """
    Converte um número fracionário de uma base para outra.

    Parâmetros:
        num (str): Número fracionário que deverá ser convertido.
        base_num (int): Base de num.
        precisao (int): Precisao do resultado.
        base_destino (int): Base do resultado.

    Retorna:
        converte_fracionario(num, base_num, precisao, base_destino): Um número fracionário na base_destino, tendo como entrada num na base_num.
    """
    num = num.split(',') if ',' in num else num.split('.')
    resultado = converte(num[0], base_num, base_destino)
    parte_fracionaria = ''

    while precisao > 0:
        expressao = converte(num[1], base_num, 10) + f" * ('{base_destino}',10)"
        decimal = resultado_expressao(expressao, base_num)
        parte_fracionaria += converte(decimal[:-(len(num[1]))], base_num, base_destino) if converte(decimal[:-(len(num[1]))], base_num, base_destino) != '' else '0'

        num[1] = decimal[-len(num[1]):]
        precisao -= 1
    
    return resultado + ',' + parte_fracionaria

def resultado_expressao(expressao:str, base_destino:int):
    """
    Calcula o resultado de uma expressão em diferentes bases.
    Os números em diferentes bases na expressão devem seguir o formato:
    "(num,base)"

    Exemplo da expressão da multiplicação de dois números em bases diferentes:
    "('num1',base1) * ('num2',base2)"

    Parâmetros:
        expressao (str): Expressão que deverá ser calculada.
        base_destino (int): Base do resultado da expressão.

    Retorna:
        resultado_expressao(expressao, base_destino): Um número na base_destino, tendo como entrada uma expressão.
    """

    expressao = expressao.split()

    for i, elemento in enumerate(expressao):
        if "(" in elemento:
            expressao[i] = str(converte(eval(elemento)[0], eval(elemento)[1]))

    resultado = str(eval(' '.join(expressao)))

    return converte(resultado, 10, base_destino)


def complemento(num, base):
    """
    Retorna o complemento de um número em sinal e magnitude caso num seja um número em sinal e magnitude
    Ou retorna um número em sinal e magnitude caso num esteja em complemento da base.

    Parâmetros:
        num (str): Número em complemento ou sinal e magnitude.
        base (int): Base de num.
    """
    maxdigit = list(digitos.keys())[list(digitos.values()).index(base-1)]
    expressao = f"('{maxdigit*(len(str(num))+1)}',{base}) - ('{num}',{base}) + 1"
    resultado = resultado_expressao(expressao, base)
    
    return resultado if resultado[1] != '0' else resultado[1:]


def converte_em_complemento(num, base_num, base_destino):
    """
    Converte um número em complemento para outro em outra base.

    Parâmetros:
        num (str): Número em complemento ou sinal e magnitude.
        base_num (int): Base de num.
        base_destino (int): Base do resultado da conversão.
    """
    num = complemento(num, base_num)
    num = converte(num, base_num, base_destino)
    num = complemento(num, base_destino)

    return num
