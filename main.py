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
redo, undo, tr_list = read_data.get_redo_undo_tr(log_list)
redo_list, undo_list = read_data.split_tr(tr_list, redo, undo)

# Realizando os updates de todas as transações
for tr in tr_list:
    database.update(name_table, tr)


print("As seguintes transações irão fazer REDO: ", end="")
for tr in redo:
    print(tr, end=", ")
print()

print("As seguintes transações irão fazer UNDO: ", end="")
for tr in undo:
    print(tr, end=", ")
print()

for tr in redo_list:
    database.redo(name_table, tr)

for tr in undo_list:
    database.undo(name_table, tr)

print(redo)
print(undo)
print(tr_list)
print(redo_list)
print(undo_list)

"UPDATE public.initial SET id=?, a=?, b=? WHERE <condition>;"