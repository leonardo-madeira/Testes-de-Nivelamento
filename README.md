# Vaga de estágio - Testes de Nivelamento

Este repositório documenta a execução dos testes de nivelamento realizados para a oportunidade em uma vaga de estágio.

## 1. Teste de Web Scraping

**Objetivo:** Criar um script em Python que automatize o processo para acessar e baixar anexos do site da ANS.

**Tarefas realizadas:**
- Acesso ao site: [Atualização do Rol de Procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
- Download dos Anexos I e II em formato PDF
- Compactação dos anexos em um único arquivo ZIP

## 2. Teste de Transformação de Dados

**Objetivo:** Extrair dados de uma tabela em um PDF e salvar em um arquivo .csv, compactar o arquivo e substituir de nome das colunas OD e AMB pelas descrições completas, conforme a legenda no
rodapé da tabela do PDF.

**Tarefas realizadas:**
- Extração de dados da tabela "Rol de Procedimentos e Eventos em Saúde" do Anexo I
- Conversão dos dados para CSV
- Compactação do CSV em um arquivo `Teste_{seu_nome}.zip`
- Substituição de abreviações de colunas OD e AMB pelas descrições completas

## 3. Teste de Banco de Dados

**Objetivo:** Criar scripts SQL para estruturar, importar e analisar dados.

**Tarefas realizadas:**
- Download de arquivos do repositório público da ANS:
  - [Demonstrações Contábeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
  - [Dados Cadastrais de Operadoras](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)
- Criação de tabelas para armazenar os dados
- Importação dos arquivos CSV com o encoding correto
- Desenvolvimento de uma query analíticas para responder:
  - Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
  - Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

## 4. Teste de API

**Objetivo:** Criar uma interface web em Vue.js conectada a um servidor em Python.

**Tarefas realizadas:**
- Utilização dos dados cadastrais das operadoras Ativas do teste 3
- Desenvolvimento de um servidor com rota para busca textual na lista de cadastros de operadoras
- Criação de uma coleção no Postman para demonstrar os resultados

---

**Status:** Todos os testes concluídos com sucesso.

**Tecnologias utilizadas:** Python, SQL, Vue.js, Postman.

Para mais detalhes, consulte os arquivos de código neste repositório.

