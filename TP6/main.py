from anasin import rec_Parser

def calculo(node):
    if node["type"] == "NUM":
        return node["value"]
    elif node["type"] == "PLUS":
        return calculo(node["left"]) + calculo(node["right"])
    elif node["type"] == "MINUS":
        return calculo(node["left"]) - calculo(node["right"])
    elif node["type"] == "MULT":
        return calculo(node["left"]) * calculo(node["right"])
    elif node["type"] == "DIV":
        right_value = calculo(node["right"])
        if right_value == 0:
            print("Erro: Divisão por zero")
            exit(1)
        return calculo(node["left"]) / right_value
    else:
        raise ValueError(f"Nó desconhecido: {node['type']}")

def main():
    #entrada = "67-(2+3*4)"
    entrada = input("Digite a expressão a ser calculada: ")
    
    ast = rec_Parser(entrada)
    print(f"AST gerada: {ast}")
    
    # Avaliar a AST
    resultado = calculo(ast)
    print(f"Resultado final: {resultado}")

if __name__ == "__main__":
    main()