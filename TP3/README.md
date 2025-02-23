# TP3: Conversor de MarkDown para HTML

### Data: 23/02/2024
### Autor: Tomás Silva A104362

### Foto:
![Photo](../Photo.png)

---

### Resumo

Este programa faz o parsing de um ficheiro Markdown e converte-o em HTML. Ele lida com cabeçalhos, negrito, itálico, links, imagens e listas.

---

### Estrutura do Código

#### Função `hearders`

Esta função converte cabeçalhos Markdown (`#`, `##`, `###`) em cabeçalhos HTML (`<h1>`, `<h2>`, `<h3>`).

#### Função `bold`

Esta função converte texto em negrito Markdown (**texto**) em negrito HTML (<b>texto</b>).

#### Função `italic`

Esta função converte texto em itálico Markdown (*texto*) em itálico HTML (<i>texto</i>).

#### Função `links`

Esta função converte links Markdown (texto) em links HTML (<a href="url">texto</a>).

#### Função `images`

Esta função converte imagens Markdown (!alt) em imagens HTML (<img src="url" alt="alt">).

#### Função `images`

Esta função converte listas ordenadas Markdown em listas HTML (<ul><li>item</li></ul> e <ol><li>item</li></ol>).