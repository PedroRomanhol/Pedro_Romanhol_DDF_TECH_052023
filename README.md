# **Pedro Henrique Romanhol Pessoa**

# <https://metabase-treinamentos.dadosfera.ai/collection/485-pedro-romanhol-05-2023>

#

**Item 1 -** Sobre a Base de Dados

Essa base de dados contém todas as transações ocorridas entre 01/12/2010 e 09/12/2011 para uma empresa de varejo online não física com sede registrada no UK, a base e mais detalhes podem ser encontrados em:

<https://archive.ics.uci.edu/dataset/352/online+retail>

Colunas (Variáveis):

- InvoiceNo: número da fatura
- StockCode: Código do Estoque
- Quantity: Quantidade
- InvoiceDate: data da fatura
- UnitPrice: Preço da unidadee
- CustomerID: ID do cliente
- Country: Pais

# **Item 2.1 -** Sobre a Dadosfera – Integrar

- Carregamento:

<https://app.dadosfera.ai/pt-BR/collect/import-files/f01e674b-ef9c-487d-bbf3-55eb4ef5a113>

- Análise descritiva

<https://metabase-treinamentos.dadosfera.ai/dashboard/115-vendas-uk>

# **Item 3 -** Sobre a Dadosfera - Explorar

As imagens se encontram nos prints e no arquivo pdf

# **Item 4 -** Sobre Data Quality

| Coluna (Variável) | Ordem correta | Valores nulos | Tipo de dado correto? |
| --- | --- | --- | --- |
| InvoiceNo | Sim | 0   | Sim |
| StockCode | Sim | 0   | Sim |
| Description | Sim | 1454 | Sim |
| Quantity | Sim | 0   | Sim |
| InvoiceDate | Sim | 0   | Não |
| UnitPrice | Sim | 0   | Sim |
| Country | Sim | 0   | Sim |

- Coluna “Description”: 1454 valores nulos (0.27% do total)
- Coluna “InvoiceDate”: todos os valores estão em formato inesperado

# **Item 5 -** Sobre o uso de GenAI e LLMs – Processar

<https://app.dadosfera.ai/pt-BR/catalog/data-assets/96824688-544e-4e04-b05f-de1e07e88121>

# Item 6 - Sobre Modelagem de Dados

**Justificativa da Escolha**

A abordagem de Kimball e o esquema Estrela são escolhidos porque:

Facilidade de Consulta: O esquema Estrela simplifica as consultas, permitindo a fácil extração de dados agregados.

Desempenho: O design do esquema Estrela é otimizado para consultas de leitura intensiva, que são comuns em análises e relatórios.

Flexibilidade: Permite adicionar novas dimensões ou fatos conforme necessário, sem grandes modificações na estrutura existente.

**Esquema Estrela**

O esquema Estrela consiste em uma tabela de fatos central, que armazena dados transacionais ou métricas, e várias tabelas de dimensões que armazenam os atributos descritivos.

**Tabelas de Dimensões**

**Dimensão Produto:**

- produto_id (chave primária)
- docid
- titulo
- Descricao

**Dimensão Categoria:**

- categoria_id (chave primária)
- categoria
- categoria_label

**Tabela de Fatos:**

- Fato Produto Categoria
- fato_id (chave primária)
- produto_id (chave estrangeira para Dimensão Produto)
- categoria_id (chave estrangeira para Dimensão Categoria)+

# **Item 7 -** Sobre Análise de Dados - Analisar

<https://metabase-treinamentos.dadosfera.ai/dashboard/127-analise-corpus-pedro>

**_Bonus 3:_** Traga ou realize alguma nova análise com dados próximos ao domínio utilizado neste case, mas que utilize ferramentas externas de BI como PowerBI ou Tableau. Crie um Readme explicando como foi criado esse projeto e suba no mesmo repositório do case. [Incorpore](https://www.google.com/url?q=https://docs.dadosfera.ai/docs/carregar-ativos-manualmente&sa=D&source=editors&ust=1716474247010282&usg=AOvVaw2v2hMI7iO8ZjF_abZYBBZF) esse dashboard externo como um Ativo na Dadosfera.

# Item  8 - Sobre Pipelines

https://app-intelligence-treinamentos.dadosfera.ai/pipeline?project_uuid=7e8cdf4d-0163-418b-850f-a8d12fb03b7b&pipeline_uuid=ba74a8b7-7e00-4aa6-946e-74aa8a226e0d

**Simulação da Copa América em Python**

Este é um projeto simples em Python que simula os resultados da Copa América utilizando aprendizado de máquina e análise de dados.

**Descrição**

O objetivo deste projeto é prever os resultados dos jogos da Copa América com base em dados históricos das equipes participantes.

O projeto utiliza as seguintes etapas:

1. Coleta de dados históricos das equipes participantes.
2. Pré-processamento dos dados para alimentar o modelo de aprendizado de máquina.
3. Treinamento do modelo de aprendizado de máquina.
4. Interface para o usuário selecionar as equipes participantes e prever os resultados dos jogos.

**Bibliotecas Utilizadas**

- Pandas: Para manipulação de dados.
- Scikit-learn: Para treinar o modelo de aprendizado de máquina.

# Item  9 - Sobre Data Apps

https://app-intelligence-treinamentos.dadosfera.ai/pipeline?project_uuid=7e8cdf4d-0163-418b-850f-a8d12fb03b7b&pipeline_uuid=ba74a8b7-7e00-4aa6-946e-74aa8a226e0d

Utilizando a simulação da Copa América do item 8, criei um data app que simula a Copa América. Ele mostra os grupos com as seleções que estão participando e, ao clicar no botão de simular, são gerados os resultados da fase de grupos. Uma nova tabela com a pontuação e posição de cada seleção é apresentada e, com as seleções classificadas, temos a fase de mata-mata que é simulada fase a fase até a definição do campeão.

**O data app exibe as seguintes informações:**

1. Grupos da Copa América com as seleções participantes.
2. Resultados da fase de grupos.
3. Tabela com a pontuação e posição de cada seleção.
4. Fase de mata-mata simulada.
5. Campeão da Copa América.
   
**Observações:**

A simulação é baseada em dados históricos e utiliza aprendizado de máquina para prever os resultados dos jogos.
