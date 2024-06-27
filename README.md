# ANÁLISE DE INDICADORES DA NORTHWIND
<div align="center">
 
 <td><img src="imagens/icon/ico-nortwind.jpeg" width="850" style="display: block; margin: 0 auto;" alt="Dinha"> </td>
  </div>



## Introdução
  
Esse projeto tem como objetivo a construção de um relatório feito no power BI com a disponibilização de 14 tabelas da empresa fictícia “Northwind”. Essa empresa enfrenta problemas de gerenciamento e análise de dados que devido a grande demanda e crescimento da loja, os métodos antigos deixaram de ser úteis, então esse projeto tem a função de integrar diferentes áreas em apenas um relatório, assim há uma diminuição de conflitos entre elas e um aumento da performance da loja. E para isso, primeiro foi passado pela etapa de pré-processamento de dados, em que eles foram explorados em um arquivo jupyter notebook, para verificar a integridade e resolver qualquer problema que possa causar no momento das análises, e a outra etapa foi a construção do painel no power BI, contendo 7 páginas que buscam integrar diferentes áreas e gerar insights para os tomadores de decisão. 
* [Link do painel interativo](https://bit.ly/northwindanalytics)

##  Requisitos Essenciais e Critérios de Avaliação

| Requisito Essencial                  | Descrição                                                                                                           | Critério de Avaliação                                                                 | Método de Avaliação                                    |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------|
| Pré-processamento de Dados           | Importar, explorar e limpar dados utilizando Python no Google Colab.                                                | Dados sem valores nulos, formatos consistentes, datasets relevantes selecionados e preparados. | Revisão de código, análise de logs de limpeza de dados, verificação manual das amostras de dados. |
| Construção do Painel no Power BI     | Carregar e organizar dados no Power BI, criando visualizações interativas divididas em seis páginas temáticas mais uma capa. | Painel funcional, visualizações claras e interativas, navegação eficiente entre páginas. | Testes de usabilidade, feedback de stakeholders, verificação da funcionalidade dos botões interativos. |
| Design de Layouts no Figma           | Produzir layouts das páginas do relatório no Figma, utilizando cores da marca e um logotipo fictício, integrando design ao Power BI. | Consistência visual com a marca, layout profissional e integrado ao painel do Power BI. | Revisão do design por equipe de design, comparação com padrões de marca, validação de stakeholders. |
| Geração de Insights                  | Analisar dados e gerar insights acionáveis para apoiar decisões estratégicas, focando em aumentar o ticket médio e reduzir o churn. | Insights relevantes e aplicáveis, suportados por dados, que podem orientar ações estratégicas. | Avaliação de stakeholders, comparação dos insights com objetivos estratégicos, análise de viabilidade das ações sugeridas. |
| Qualidade dos Dados                  | Garantir que todos os datasets utilizados estão em alta qualidade e adequadamente pré-processados antes de serem carregados no Power BI. | Dados sem inconsistências, alta integridade e adequação para análise. | Revisão de qualidade de dados, verificação de integridade, relatórios de limpeza de dados. |
| Interatividade do Painel             | Implementar funcionalidades interativas no painel, como botões para limpar filtros, visualizar tabelas de dados e navegação entre páginas. | Interatividade fluida, fácil de usar, e que melhora a experiência do usuário. | Testes de usabilidade com usuários finais, feedback de usuários, análise de performance das funcionalidades interativas. |
| Documentação do Projeto              | Criar documentação detalhada de todas as etapas do projeto, incluindo pré-processamento, construção do painel e design de layouts. | Documentação clara, detalhada e fácil de seguir, cobrindo todas as etapas do projeto. | Revisão por pares, feedback de novos membros da equipe que utilizam a documentação para entendimento do projeto. |


## Etapas do Desenvolvimento: 

- **Pré-processamento de Dados**:
  - Ferramenta: Python no Google Colab
  - Importação: Importação dos arquivos de dados para o ambiente do Google Colab
  - Exploração: Verificação e tratamento de valores nulos e formatos inadequados
  - Exclusão de Datasets: `customer_customer_demo`, `customer_demographics`, `employee_territories`, `region`, `territories`, `us_states`
  - Formatação de Datasets: `categories`, `order_details`, `shippers` (em bom formato)
  - Tratamento de Valores Nulos: `customers`, `employees`, `orders`, `supplies`
  - Conversão de Formatos: Conversão de valores de data para datetime (`employees`, `orders`), alteração de valor numérico para categórico (`products`)

- **Construção do Painel no Power BI**:
  - Planejamento: Identificação e organização dos dados a serem utilizados
  - Carregamento: Upload dos dados pré-processados no Power BI
  - Criação de Páginas: Desenvolvimento de seis páginas temáticas (customers, employees, orders, products, supplies, shippers) e uma capa
  - Funcionalidades Interativas: Botões para limpar filtros, visualizar tabelas de dados, links para redes sociais, navegação entre páginas

- **Design de Layouts no Figma**:
  - Ferramenta: Figma
  - Layouts: Produção de layouts das páginas do relatório
  - Consistência Visual: Uso de cores da marca e logotipo fictício em tons de verde
  - Integração: Integração do design ao painel do Power BI

- **Geração de Insights**:
  - Análise: Análise dos dados para gerar insights acionáveis
  - Foco Estratégico: Aumentar o ticket médio e reduzir o churn
  - Páginas Temáticas:
    - **Customers**: Identificação de concentração de clientes, potencial de expansão em outras regiões
    - **Employees**: Concentração de empregados, necessidades de expansão de força de trabalho
    - **Orders**: Quantidade de pedidos por região, análise de custos de frete e principais destinatários
    - **Products**: Circulação de produtos, controle de estoque, principais categorias de produtos
    - **Supplies**: Concentração de fornecedores, comunicação e integração com representantes de vendas e gerentes de marketing
    - **Shippers**: Distribuição das transportadoras, formas de contato e integração

- **Documentação do Projeto**:
  - Detalhamento: Documentação detalhada de todas as etapas do projeto
  - Clareza: Explicação clara e fácil de seguir sobre o pré-processamento, construção do painel e design de layouts
  - Revisão: Revisão por pares e feedback de novos membros da equipe


## Conclusão
Neste projeto, abordamos um conjunto abrangente de etapas que nos permitiram transformar dados brutos em insights acionáveis para a Northwind Traders. Destacou a importância de um pré-processamento de dados robusto, garantindo a qualidade e integridade dos dados para análises subsequentes e o uso do Power BI permitiu criar visualizações interativas e acessíveis, facilitando a compreensão dos dados e a geração de insights e por fim, a integração de design no Figma reforçou a identidade visual da marca, proporcionando uma experiência coesa e profissional. 
Através deste projeto, adquirimos um conhecimento aprofundado sobre as melhores práticas de manipulação e visualização de dados, além de estratégias de análise que podem apoiar decisões empresariais informadas. Esses insights são cruciais para aumentar o ticket médio e reduzir o churn, alinhando-se aos objetivos estratégicos da Northwind Traders.

