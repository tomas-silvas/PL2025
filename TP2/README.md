# TP2: Análise de um dataset de obras musicais

### Data: 20/02/2024
### Autor: Tomás Silva A104362

### Foto:
![Photo](../Photo.png)

---

### Resumo

Este programa faz o parsing de um ficheiro csv com informações sobre obras músicais, e organiza-as em três estruturas: 
1. **Lista ordenada alfabeticamente dos compositores musicais**: Um array ordenado.
2. **Distribuição das obras por período**: Um dicionário ordenado (periodo -> num_obras).
3. **Dicionário de títulos das obras por período**: Um dicionário em que a cada período está associada uma lista alfabética dos títulos das obras desse período (periodo -> lista_ordenada_titulos).


---

### Estrutura do Código

#### Função `parse_csv`

Esta função lê um arquivo CSV e extrai informações específicas de cada linha. A expressão regular é usada para substituir todas as quebras de linha (\n) dentro de aspas duplas por espaços:
- ".*?": Este padrão corresponde a qualquer sequência de caracteres entre aspas duplas. 
- lambda x: x.group(0).replace('\n', ' '): Para cada correspondência encontrada, a função substitui todas as quebras de linha (\n) dentro das aspas duplas por espaços.
- Esta flag faz com que o caractere . na expressão regular corresponda a qualquer caractere, incluindo quebras de linha. Isso permite que a expressão regular capture texto que se estende por várias linhas.

#### Função `create_catalogs`

Esta função cria os três catálogos referidos acima a partir das entradas extraídas do CSV.