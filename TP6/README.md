# TP6: Recursivo Descendente para expressões aritméticas

### Data: 23/03/2025
### Autor: Tomás Silva A104362

### Foto:
![Photo](../Photo.png)

---

### Resumo

Este programa avalia expressões matemáticas utilizando um analisador léxico e um analisador sintático recursivo descendente. Ele constrói uma Árvore Sintática Abstrata (AST) para representar a expressão e, em seguida, calcula o resultado percorrendo a AST.

---

### Estrutura do Código

- **Analisador Léxico (`analex.py`)**:
  - Define os tokens da linguagem, como números (`NUM`), operadores (`PLUS`, `MINUS`, `MULT`, `DIV`) e parênteses (`LPAREN`, `RPAREN`).
  - Divide a entrada em tokens para serem processados pelo analisador sintático.

- **Analisador Sintático (`anasin.py`)**:
  - Implementa um analisador recursivo descendente para construir a AST com base na gramática definida.
  - A gramática suporta operações de adição, subtração, multiplicação, divisão e agrupamento com parênteses.

- **Função de Avaliação (`main.py`)**:
  - Recebe a AST gerada pelo analisador sintático e calcula o resultado da expressão percorrendo a árvore.

---

### Exemplo de Entrada

```plaintext
67-(2+3*4)
```

### Exemplo de Saída 

```plaintext
Derivando por Exp → Term Exp2
Derivando por Term → Factor Term2
Derivando por Factor → NUM
Reconheci Factor → NUM com valor 67
Derivando por Term2 → ε
Reconheci Term → Factor Term2
Derivando por Exp2 → - Term Exp2
Derivando por Term → Factor Term2
Derivando por Factor → ( Exp )
Derivando por Exp → Term Exp2
Derivando por Term → Factor Term2
Derivando por Factor → NUM
Reconheci Factor → NUM com valor 2
Derivando por Term2 → ε
Reconheci Term → Factor Term2
Derivando por Exp2 → + Term Exp2
Derivando por Term → Factor Term2
Derivando por Factor → NUM
Reconheci Factor → NUM com valor 3
Derivando por Term2 → * Factor Term2
Derivando por Factor → NUM
Reconheci Factor → NUM com valor 4
Derivando por Term2 → ε
Reconheci Term → Factor Term2
Derivando por Exp2 → ε
Reconheci Exp → Term Exp2
Reconheci Factor → ( Exp )
Reconheci Term → Factor Term2
Reconheci Exp2 → - Term Exp2
Reconheci Exp → Term Exp2
Análise sintática concluída com sucesso!
AST gerada: {'type': 'MINUS', 'left': {'type': 'NUM', 'value': 67}, 'right': {'type': 'PLUS', 'left': {'type': 'NUM', 'value': 2}, 'right': {'type': 'MULT', 'left': {'type': 'NUM', 'value': 3}, 'right': {'type': 'NUM', 'value': 4}}}}
Resultado final: 53
```
