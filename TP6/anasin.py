from analex import lexer  # Importa o analisador léxico

prox_simb = ('Erro', '', 0, 0)  # Token atual

def parserError(simb):
    print(f"Erro sintático, token inesperado: {simb}")
    exit(1)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)

# Regra: Factor → NUM | ( Exp )
def rec_Factor():
    global prox_simb
    if prox_simb.type == 'NUM':
        print("Derivando por Factor → NUM")
        value = int(prox_simb.value)  # Converte o valor do token para inteiro
        rec_term('NUM')
        print(f"Reconheci Factor → NUM com valor {value}")
        return {"type": "NUM", "value": value}
    elif prox_simb.type == 'LPAREN':
        print("Derivando por Factor → ( Exp )")
        rec_term('LPAREN')
        node = rec_Exp()  # Resolve a expressão dentro dos parênteses
        rec_term('RPAREN')
        print(f"Reconheci Factor → ( Exp )")
        return node
    else:
        parserError(prox_simb)

# Regra: Term2 → * Factor Term2 | / Factor Term2 | ε
def rec_Term2(left):
    global prox_simb
    if prox_simb is not None and prox_simb.type == 'MULT':
        print("Derivando por Term2 → * Factor Term2")
        rec_term('MULT')
        right = rec_Factor()
        node = {"type": "MULT", "left": left, "right": right}
        return rec_Term2(node)
    elif prox_simb is not None and prox_simb.type == 'DIV':
        print("Derivando por Term2 → / Factor Term2")
        rec_term('DIV')
        right = rec_Factor()
        node = {"type": "DIV", "left": left, "right": right}
        return rec_Term2(node)
    else:
        print("Derivando por Term2 → ε")
        return left

# Regra: Term → Factor Term2
def rec_Term():
    print("Derivando por Term → Factor Term2")
    factor_node = rec_Factor()
    node = rec_Term2(factor_node)
    print("Reconheci Term → Factor Term2")
    return node

# Regra: Exp2 → + Term Exp2 | - Term Exp2 | ε
def rec_Exp2(left):
    global prox_simb
    if prox_simb is not None and prox_simb.type == 'PLUS':
        print("Derivando por Exp2 → + Term Exp2")
        rec_term('PLUS')
        right = rec_Term()
        node = {"type": "PLUS", "left": left, "right": right}
        return rec_Exp2(node)
    elif prox_simb is not None and prox_simb.type == 'MINUS':
        print("Derivando por Exp2 → - Term Exp2")
        rec_term('MINUS')
        right = rec_Term()
        node = {"type": "MINUS", "left": left, "right": right}
        return rec_Exp2(node)
    else:
        print("Derivando por Exp2 → ε")
        return left

# Regra: Exp → Term Exp2
def rec_Exp():
    print("Derivando por Exp → Term Exp2")
    term_node = rec_Term()
    node = rec_Exp2(term_node)
    print("Reconheci Exp → Term Exp2")
    return node

# Função principal do parser
def rec_Parser(data):
    global prox_simb
    lexer.input(data)  # Alimenta o lexer com a entrada
    prox_simb = lexer.token()  # Obtém o primeiro token
    ast = rec_Exp()  # Constrói a AST
    if prox_simb is not None:
        print(f"Erro: entrada não consumida completamente. Token restante: {prox_simb}")
        exit(1)
    print("Análise sintática concluída com sucesso!")
    return ast
