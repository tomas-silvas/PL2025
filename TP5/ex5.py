import json
import ply.lex as lex
from datetime import datetime
import sys

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    'CODIGO',
    'VIRGULA',
    'EURO',
    'CENT',
    'PONTO'
)

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'
t_PONTO = r'\.'
t_VIRGULA = r'\,'

def t_CODIGO(t):
    r'[A-Z][0-9]+'
    return t

def t_EURO(t):
    r'[0-9]+e'
    t.value = int(t.value[:-1])
    return t

def t_CENT(t):
    r'[0-9]+c'
    t.value = int(t.value[:-1])
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

file_path = '/home/tomazo/Desktop/PL2025/TP5/stock.json'

def main():
    stock_dic = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for product in data["stock"]:
        stock_dic[product["cod"]] = {
            "nome": product["nome"],
            "quant": product["quant"],
            "preco": product["preco"]
        }
    
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    print(f"maq: {current_date}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    saldo = 0.00
    
    while True:
        pedido = input(">> ")
        lexer.input(pedido)
        tokens = list(lexer)
        
        if not tokens:
            print("maq: Erro: comando não reconhecido")
            continue
        
        if tokens[0].type == 'LISTAR':
            print("maq:\ncod | nome | quantidade | preço\n---------------------------------")
            for key in stock_dic:
                print(f"{key} {stock_dic[key]['nome']} {stock_dic[key]['quant']} {stock_dic[key]['preco']}")
        elif tokens[0].type == 'MOEDA':
            for tok in tokens[1:]:
                if tok.type == 'EURO':
                    saldo += tok.value
                elif tok.type == 'CENT':
                    saldo += tok.value / 100
                elif tok.type == 'PONTO':
                    print("maq: Erro: ponto fora de contexto")
                    break
                elif tok.type == 'VIRGULA':
                    continue
                else:
                    print("maq: Erro: comando não reconhecido")
                    break
            else:
                print(f"maq: Saldo = {int(saldo)}e{int((saldo - int(saldo)) * 100)}c")
        elif tokens[0].type == 'SELECIONAR':
            if len(tokens) > 1 and tokens[1].type == 'CODIGO':
                cod = tokens[1].value
                if cod in stock_dic:
                    produto = stock_dic[cod]
                    if saldo >= produto['preco']:
                        saldo -= produto['preco']
                        produto['quant'] -= 1
                        print(f'maq: Pode retirar o produto dispensado "{produto["nome"]}"')
                        print(f"maq: Saldo = {int(saldo)}e{int((saldo - int(saldo)) * 100)}c")
                    else:
                        print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                        print(f"maq: Saldo = {int(saldo)}e{int((saldo - int(saldo)) * 100)}c; Pedido = {int(produto['preco'])}e{int((produto['preco'] - int(produto['preco'])) * 100)}c")
                else:
                    print("maq: Produto não existe")
            else:
                print("maq: Erro: comando não reconhecido")
        elif tokens[0].type == 'SAIR':
            troco = saldo
            moedas = []
            for valor, nome in [(0.50, "50c"), (0.20, "20c"), (0.10, "10c"), (0.05, "5c"), (0.02, "2c"), (0.01, "1c")]:
                while troco >= valor:
                    troco -= valor
                    moedas.append(nome)
            print(f"maq: Pode retirar o troco: {', '.join(moedas)}.")
            print("maq: Até à próxima")
            sys.exit()
        else:
            print("maq: Erro: comando não reconhecido")

if __name__ == '__main__':
    main()