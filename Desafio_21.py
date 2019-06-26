'''__________String__________
Fatiamento: [x:y:z]
    x-> Início,
    y-> Final(exclusive),
    z-> pula a qtd de casas indicada
Análise:
    len() -> Comprimento ,
    count('x', 0, 13) -> contar qtd de x com fatiamento ,
    find ('xyz') -> Indica o indexador inicial onde foi encontrado a str OBS(-1 não encontrado),
    'string' in variável -> Operador boleano que indica se tem a str na variável

Transformação:
    replace('x', 'y') ->  Trocar, reposicionar 'x' por 'y'
    upper() -> Método que troca todas as letras para maiúsculas,
    lower() -> Método que troca todas as letras para minúsculas,
    capitalize() -> Método que deixa só a primeira letra em maiúscula,
    title() -> Método que deixa a primeira letra de cada palavra em maiúsculas,
    strip() -> Remove os espaços inúteis do inicio e fim da str,
        rstrip() -> Remove os espaços a direita,
        lstrip() -> remove os espaços a esquerda,
Divisão:
    split() -> Divide uma str em uma lista, onde cada palavra vira uma nova lista,
Junção:
    '-'.join('variável') -> Junta as str por um '-'
'''
#Brincando com Strings
nome = str(input('Digite seu nome completo: ')).strip()
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras (sem espaços): {}'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O primeiro nome é {} e tem {} letras. '.format(separa[0], len(separa[0])))
#ou -> print(nome.find(' '))
