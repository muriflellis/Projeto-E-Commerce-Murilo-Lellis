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

3° Etapa - Auditoria, tratamento e validação dos dados

Com a tabela criada, comecei a trabalhar com Python e Pandas para entender melhor os dados e identificar possíveis problemas.

Primeiro, fiz uma verificação geral da tabela para entender a quantidade de registros, os tipos de dados, os valores ausentes e possíveis duplicidades.

Durante essa análise, encontrei:

12 valores ausentes em produto_categoria;

10 valores ausentes em preco;

28 valores ausentes em cliente_cidade.

Depois de identificar esses problemas, comecei o tratamento dos dados:

Converti a coluna data_compra de texto para o formato de data (datetime).

Substituí os valores ausentes de produto_categoria e cliente_cidade por "Não Informado".

Mantive os 10 preços ausentes sem preenchimento, pois entendi que utilizar uma média ou mediana poderia alterar os resultados das análises financeiras.

Por último, realizei algumas verificações para garantir que os dados estavam consistentes, conferindo pedidos duplicados, linhas repetidas, preços, fretes e avaliações fora do intervalo permitido.

O resultado foi:

250 registros preservados;

Nenhum pedido ou registro duplicado;

Nenhum preço ou frete com valor igual ou inferior a zero;

Nenhuma avaliação fora do intervalo de 1 a 5;

Apenas os 10 preços que já estavam ausentes continuaram sem informação.

Com isso, finalizei a preparação da base e deixei os dados prontos para começar a análise das vendas.
