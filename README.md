<div align="center" id="top"> 
  <img src="./img/log-file.png" alt="Db2_atividade_log" />

  &#xa0;

</div>

<h1 align="center">Trabalho Prático - LOG</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/ViiniciusK9/db2_atividade_log?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/ViiniciusK9/db2_atividade_log?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/ViiniciusK9/db2_atividade_log?color=56BEB8">

</p>

<p align="center">
  <a href="#dart-sobre">Sobre</a> &#xa0; | &#xa0; 
  <a href="#rocket-tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requisitos">Requisitos</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-iniciar">Iniciar</a> &#xa0; | &#xa0;
  <a href="https://github.com/ViiniciusK9" target="_blank">Autor</a>
</p>

<br>

## :dart: Sobre ##

O objetivo principal do projeto é desenvolver e implementar um mecanismo de log Redo/Undo sem checkpoint em um Sistema de Gerenciamento de Banco de Dados (SGBD). O mecanismo de log Redo/Undo permite rastrear e recuperar alterações realizadas no banco de dados, oferecendo a capacidade de refazer (Redo) ou desfazer (Undo) operações anteriores de forma precisa e consistente.

O código inicia lendo o arquivo ```metadado.json```, que contém informações sobre a estrutura da tabela e os dados iniciais. Com base nesses dados, a tabela é criada e os registros são inseridos. Essa etapa é crucial para iniciar o processo de log a partir de um estado inicial consistente.

Exemplo de arquivo ```metadado.json``` :
```json
{
  "INITIAL": {
    "id": [1, 2],
    "A": [20,20],
    "B": [55,30]
  }
}
```

Em seguida, o código realiza a leitura do arquivo ```entrada_log```, que contém informações relevantes para o processamento das transações. Esse arquivo inclui dados sobre o início das transações, as modificações efetuadas por cada transação e informações sobre quais transações foram finalizadas.

Exemplo de arquivo ```entrada_log``` :
```
<start T1>
<T1,1,A,20,2000>
<start T2>
<T2,1,B,55,1000>
<commit T2>
<start T3>
<T3,2,B,30,1000>
<commit T1>
<start T4>
<T4,1,A,2000,3000>
<start T5>
<commit T4>
<T5,2,A,20,1000>
<T3,2,B,1000,8000>
```

Primeiramente, o código processa todas as alterações registradas no arquivo ```entrada_log```. Em seguida, ele analisa as transações para determinar quais delas requerem a aplicação do REDO e quais precisam ser desfeitas pelo UNDO. O REDO é executado para refazer as alterações registradas e atualizar o banco de dados de acordo. Posteriormente, o código realiza o UNDO para desfazer as alterações necessárias, garantindo a consistência e a correção das operações executadas.

Exemplo de saida após executar o código com os exemplos acima:
```
Estado inicial do banco de dados:
+------+-----+-----+
|   id |   A |   B |
+======+=====+=====+
|    1 |  20 |  55 |
+------+-----+-----+
|    2 |  20 |  30 |
+------+-----+-----+

Transação T2 realizou REDO
Transação T1 realizou REDO
Transação T4 realizou REDO

Transação T5 realizou UNDO
Transação T3 realizou UNDO

Dados após as operações de REDO e UNDO:
+------+------+------+
|   id |    A |    B |
+======+======+======+
|    1 | 3000 | 1000 |
+------+------+------+
|    2 |   20 |   30 |
+------+------+------+
```


## :rocket: Tecnologias ##

As seguintes ferramentas foram utilizadas neste projeto:

- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)

## :white_check_mark: Requisitos ##

Antes de iniciar :checkered_flag:, você precisa ter o [Git](https://git-scm.com) e [Python3.8](https://www.python.org/) ou [Python3.9](https://www.python.org/) instalado.

## :checkered_flag: Iniciar ##

```bash
# Clone este projeto
$ git clone https://github.com/ViiniciusK9/db2_atividade_log

# Acesse
$ cd db2_atividade_log

# Crie um ambiente virtual
$ python3 -m venv db2-env

# No Windows, execute:

$ db2-env\Scripts\activate.bat

# No Unix ou no MacOS, executa:

$ source db2-env/bin/activate

# Instale as dependências
$ python -m pip install -r requirements.txt

# Crie um arquivo chamado .env na raiz do projeto
# Adicione as seguintes variáveis
DATABASE    = nomedobanco
HOST        = localhost -> (default)
USER        = usuario
PASSWORD    = senha
PORT        = 5432 -> (default)

# Execute o projeto
$ python main.py
```

<br>
Feito por <a href="https://github.com/ViiniciusK9" target="_blank">Vinicius Koncicoski</a>

&#xa0;

<a href="#top">Voltar ao topo</a>
