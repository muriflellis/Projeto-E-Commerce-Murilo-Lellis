# Pipeline Inteligente de Performance de Varejo (E-Commerce)

## 📌 Sobre o Projeto
Este projeto simula o cenário real de uma operação de e-commerce de médio porte que precisa centralizar, limpar e enriquecer seus dados de vendas e clientes para tomada de decisões estratégicas. O objetivo é demonstrar a construção de um pipeline de dados analítico ponta a ponta (ETL), focado em eficiência técnica e inteligência de negócios.

## 💼 O Problema de Negócio
A empresa enfrenta dificuldades para analisar seus dados operacionais devido a registros despadronizados (formatos de datas inconsistentes, valores nulos e duplicados). Além disso, a equipe perde tempo cruzando dados geográficos manualmente e não consegue extrair insights automáticos a partir das avaliações textuais e reclamações deixadas pelos clientes.

## 🚀 Solução Desenvolvida
Desenvolvimento de uma arquitetura automatizada dividida em 4 etapas:
1. **Extração e Limpeza (Python & Pandas):** Tratamento de dados brutos (remover duplicados, tratar nulos e corrigir tipagem).
2. **Enriquecimento de Dados (API):** Consumo automatizado de API de geolocalização para estruturação de dados regionais.
3. **Análise de Sentimentos (IA):** Integração com modelos de linguagem (LLM) para categorização inteligente de feedbacks de clientes.
4. **Armazenamento e Modelagem (SQL):** Estruturação dos dados limpos em um modelo dimensional (Fato/Dimensão) em banco de dados relacional.
5. **Visualização (Power BI):** Construção de dashboards corporativos focados em KPIs financeiros e de satisfação do cliente.

## 🛠️ Tecnologias Utilizadas
* **Python** (Pandas, Requests, SQLAlchemy)
* **SQL** (MySQL Workbench)
* **Power BI Desktop**
* **Git & GitHub**
* **IA Conectiva (API OpenAI/Anthropic)**


*Nota: Repositório em desenvolvimento ativo. Status atual: Fase 1 (Engenharia e Limpeza de Dados).*


##Seguimento do Projeto
1° Etapa - Criação do repositório e inserção dele na pasta
Criei o repositório https://github.com/muriflellis/Projeto-E-Commerce-Murilo-Lellis especifico para esse projeto e após isso, realizei a criação da pasta "Projeto E-Commerce" direto no meus Documents onde realizei e inserção do meu repositório com o Git Bash, "Git Clone" e "Code ." para abrir a pasta direto no meu VsCode.
Ele gerou meus arquivos README e GitIgnore direto. 

2° Etapa - Criação de tabela e começo da Analise.
Solicitei ao OpenIa, um script de criação para criar uma tabela ficticia com os problemas e situações reais para simular e facilitar o andamento do projeto. Caso contrario, seria muito mais complicado mostrar todas as habilidades propostas em um unico projeto de analise. 

Ele gerou o arquivo "gerar_dados.py" que criou o Excel "dados_ecommerce" que foi colado dento da pasta "data" para melhor localização. 
Após isso, criei a pasta "notebook" com o objetivo de preservar o notebook de analises, ja que fazer apartir de um .py me obrigaria a gerar o código varias e varias vezes.

3° Etapa - Tratamento de Dados Nulos
Fiz um tratamento com o "fillna" retirando os valores nulos das colunas "produto_categoria" e "cliente_cidade" para mostrarem, respectivamente, "não informado" e "desconhecido". Após isso, eliminei as linhas vazia da 
coluna "preco" com o "dropna".

Obtive a certeza, através do "isna().sum()" de quem haveria mais nenhum valor nulo na planilha. 

4° Etapa - Analise Analítica e Insights de Negócio.
Comecei definindo quais perguntas responderíamos para poder iniciar a análise. Separamos três perguntas estratégicas de negócio para direcionar o projeto: 
1 - Volume vs Faturamento - Qual categoria vende mais em quantidade e qual traz a maior receita?
2 - Ticket Médio - Qual o valor médio gasto por produto em cada categoria? 
3 - Análise Geográfica da Receita - Quais cidades geram maior faturamento? 

Para conseguir respondê-las com maior facilidade, já inseri diretamente em outra variável para representá-las e facilitar a consulta. 

Respondi as duas primeiras perguntas através de um único código. A tabela "df_vendas" foi separada em categorias de produtos com o "groupby", aplicamos agregações na coluna "preco" para extrairmos o valor total de pedidos, o quanto cada produto arrecadou e o ticket médio de cada produto. Para concluir, organizamos a planilha em ordem decrescente baseada no valor total de cada produto. 

A partir das informações extraídas, conseguimos notar que a categoria "Beleza e Saúde" lidera o faturamento total com R$ 7.890,66 devido ao seu ticket médio alto de R$ 151,74, contrariando as estatísticas de quem possui o maior volume de pedidos. 

Para responder a terceira pergunta, apliquei as mesmas condições das outras perguntas apenas com o diferencial de agrupar os dados pela "cliente_cidade" e fazer as agregações de soma do faturamento total por cidade e o número de pedidos em cada uma delas. Os números nos revelaram que a cidade de "São Paulo" é o principal polo comercial da operação, acumulando R$ 12.795,33 em receita com 79 pedidos. Seguidos de "Rio de Janeiro" e "Desconhecidos", que foi a alteração que fizemos para padronizar a tabela e conseguir gerar esses insights.