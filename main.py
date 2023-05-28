from tr import TR 
from db import DB 
from read_data import RM
from tabulate import tabulate

# Instanciando objetos que representam o banco de dados e a
# classe responsável pela leitura dos arquivos.
database = DB()
read_data = RM("metadado.json", "entrada_log")

# Obtendo o nome da tabela, colunas e os dados.
name_table = read_data.get_name_table()
columns_list = read_data.get_columns_list()
data_list = read_data.get_data_list()

# Criando a tabela e preenchendo a tabela com os dados iniciais
# do arquivo metadado.json.
database.create(name=name_table, columns=columns_list)
database.fill_table(name=name_table, data=data_list)

# Obtendo a lista de log do arquivo entrada_log.
log_list = read_data.get_log_list()

# Obtendo o conjunto de transações que vão realizar REDO e
# conjunto que vai fazer UNDO e a lista com todas as transações.
redo, undo, tr_list = read_data.get_redo_undo_tr(log_list)

# Realizando a separação da lista com todas as transações para
# duas listas separadas por REDO e UNDO.
redo_list, undo_list = read_data.split_tr(tr_list, redo, undo)

# Printando o estado inicial do banco de dados.
print("Estado inicial do banco de dados:")
data = database.select_all(name_table)
print(tabulate(data, headers=columns_list, tablefmt='grid'))

# Realizando os updates de todas as transações.
for tr in tr_list:
    database.update(name_table, tr)

# Printando as transações que realizaram REDO.
print()
for tr in redo:
    print(f"Transação {tr} realizou REDO")
print()

# Printando as transações que realizaram UNDO.
for tr in undo:
    print(f"Transação {tr} realizou UNDO")
print()

# Percorrendo a lista de REDO e aplicando.
for tr in redo_list:
    database.redo(name_table, tr)

# Revertendo a lista de UNDO para começar da última alteração
# para a primeira.
undo_list.reverse()

# Percorrendo a lista de UNDO e aplicando.
for tr in undo_list:
    database.undo(name_table, tr)

# Printando o banco de dados após efetuar todas as ações.
data = database.select_all(name_table)
print("Dados após as operações de REDO e UNDO:")
print(tabulate(data, headers=columns_list, tablefmt='grid'))
