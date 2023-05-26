from tr import TR 
from db import DB 
from read_data import RM


database = DB()
read_data = RM("metadado.json", "entrada_log")

name_table = read_data.get_name_table()
columns_list = read_data.get_columns_list()
data_list = read_data.get_data_list()

database.create(name=name_table, columns=columns_list)
database.fill_table(name=name_table, data=data_list)

log_list = read_data.get_log_list()
redo, undu, tr_list = read_data.get_redo_undu_tr(log_list)
redo_list, undu_list = read_data.split_tr(tr_list, redo, undu)

# Realizando os updates de todas as transações
for tr in tr_list:
    database.update(name_table, tr)

print(redo)
print(undu)
print(tr_list)
print(redo_list)
print(undu_list)

"UPDATE public.initial SET id=?, a=?, b=? WHERE <condition>;"