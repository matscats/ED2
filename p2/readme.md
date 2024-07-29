# Avaliação da segunda unidade de Algoritmos e Estrutura de Dados II

## Resumo
Esta tarefa tem como objetivo fazer um mapeamento acerca da rede de coautoria da UFRN. Para isso, utilizou-se o Scopus para selecionar todos os trabalhos publicados da UFRN os quais se enquadrassem dentro de algum Objetivo de Desenvolvimento Sustentável da ONU (ODS).

Para este trabalho, foram selecionadas quatro ODS's distintas, sendo estas:
- ODS 3 -- Saúde e Bem-Estar;
- ODS 7 -- Energia Acessível e Limpa;
- ODS 15 -- Vida Terrestre;
- ODS 17 -- Parcerias e Meios de Implementação.

Para cada uma das ODS's, construiu-se um grafo, onde cada vértice representa um autor da instituição. Considera-se coautoria quando dois ou mais autores publicam artigos juntos. Ou seja, um vértice entre dois nós do grafo ocorre quando pesquisadores publicam um trabalho em conjunto.

Ademais, para a construção do grafo, considerou-se interconexões simples, sem a utilização de pesos. Ou seja, caso dois ou mais autories publiquem mais de um trabalho juntos, ainda assim estes terão apenas um vértice os conectando, uma vez que o objetivo é apenas mapear conexões entre os autores.

Por fim, para análise de resultados, foi montado, para cada ODS, um gráfico bipartido sobre a assortatividade em relação ao grau dos nós da rede, conforme pode ser visualizado na pasta [requisito_02](./requisito_02/). Outrossim, também construiu-se uma tabela para cada uma das ODS's, destacando fatores fundamentais de análise, sendo este: Número de vértices, número de arestas, coeficiente de assortatividade de grau, número de componentes conectados, tamanho do componente gigante e coeficiente médio de aglomeração, conforme pode ser visto na pasta [requisito_03](./requisito_03/).

No geral, os pesquisadores da UFRN mostram uma boa conectividade global em áreas com um número maior de pesquisadores e colaborações, indicando uma rede bem estabelecida de coautoria. Há uma tendência significativa de formação de clusters colaborativos, sugerindo que os pesquisadores trabalham frequentemente dentro de grupos bem definidos. A assortatividade de grau varia entre as redes, com algumas áreas mostrando uma forte tendência para colaborações entre pesquisadores com graus semelhantes, enquanto outras são mais variadas. A fragmentação é mais pronunciada em redes menores, mas ainda existe uma conectividade substancial dentro dos maiores componentes dessas redes.

## Reprodutibilidade dos resultados

Para verificar os resultados, deve-se instalar as dependência necessárias do trabalho. Para isso, deve-se usar o gerenciador de pacotes pip e executar o comando abaixo a partir da pasta root:
`
 $ pip install -r requirements.txt
`

Ademais, para reproduzir cada gráfico do requisito_02, deve-se entrar na [pasta do requisito_02](./requisito_02/) e executar o arquivo main. Para decidir qual resultado da ODS visualizar, deve-se apenas alterar o caminho da variável csv_file para ajustar de acordo com a planilha a ser visualizada. Para executar o arquivo main, basta executar
`
 $ python main.py
`

Além disso, para reproduzir cada tabela do requisito_03, deve-se entrar na [pasta do requisito_03](./requisito_03/) e executar o arquivo main. Para decidir qual resultado da ODS visualizar, deve-se apenas alterar o caminho da variável csv_file para ajustar de acordo com a planilha a ser visualizada. Para executar o arquivo main, basta executar
`
 $ python main.py
`

## Autor
Trabalho realizado individualmente pelo aluno Mateus Cavalcanti Alves Teixeira Silva.