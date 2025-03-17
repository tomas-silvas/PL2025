# TP5: Máquina de Vendas Automática

### Data: 14/03/2024
### Autor: Tomás Silva A104362

### Foto:
![Photo](../Photo.png)

---

### Resumo

Este programa simula uma máquina de vendas automática. Ele permite listar os produtos disponíveis, inserir moedas, selecionar produtos e sair, devolvendo o troco. Para isto, é utilizado o ply.lex para criar os tokens, de forma a facilitar o tratamento do input, e são armazenados os items da máquina de vendas num ficheiro json.

---

### Estrutura do Código

- São declaradas as palavras reservadas para o ply.lex
- É feito o parsing do ficheiro json, armazenando os dados num dicionário
- Processa os comandos do usuário, incluindo listar produtos, inserir moedas, selecionar produtos e sair.
- Calcula e devolve o troco ao sair. 

---

### Exemplo de Entrada
>> LISTAR
>> MOEDA 1e, 20c, 5c, 5c .
>> SELECIONAR A23
>> SAIR

### Exemplo de Saída
maq: 14/03/2024, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome | quantidade | preço
---------------------------------
A23 água 0.5L 8 0.7
B12 refrigerante 0.33L 10 1.2
C34 sumo 0.5L 5 1.5
D56 chocolate 20 1.0
E78 biscoitos 15 0.8
F90 batatas fritas 12 1.3
G11 barra de cereal 25 0.9
H22 chiclete 30 0.5
J44 sanduíche 7 2.5
K55 café 20 1.0
L66 chá gelado 10 1.2
N88 água com gás 0.5L 6 0.8
>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> SAIR
maq: Pode retirar o troco: 50c, 10c.
maq: Até à próxima