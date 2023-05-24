import json
from tr import TR

class RM:
    def __init__(self, path_json : str, path_log : str):
        self.__path_json = path_json
        self.__path_log = path_log
        self.__name_table = get_name_table_1(path_json)
    
    
    def get_name_table(self) -> str:
        return self.__name_table
    
    
    def get_columns_list(self) -> list:
        with open(self.__path_json, "r") as my_json:
            data = json.load(my_json)

        columns_list = list()

        for column in data[self.__name_table]:
            columns_list.append(column)
        
        return columns_list
        
        
    def get_data_list(self) -> list:
        with open(self.__path_json, "r") as my_json:
            data = json.load(my_json)
            
        data_list = list()
        
        for column in data[self.__name_table]:
            data_list.append(data[self.__name_table][column])
        
        return data_list


    def get_log_list(self) -> list:
        log = list()

        with open(self.__path_log, "r") as arquivo:
            for row in arquivo:
                log.append(row.replace('\n', '').replace('<', '').replace('>', ''))

        return log


    def get_redo_undu_tr(self, log : list) -> list:
        tag_redo = set()
        tag_undu = set()
        tr_list = list()
        
        for row in log:
            aux = row.split(" ")
            if (len(aux) == 2):        
                if (aux[0] == "start"):
                    tag_undu.add(aux[1])
                else:
                    tag_undu.remove(aux[1])
                    tag_redo.add(aux[1])
            else:
                a = list(row.split(","))
                tr1 = TR(*a)
                tr_list.append(tr1)
        
        return tag_redo, tag_undu, tr_list
    

    def split_tr(self, tr_list : list, redo : set, undu : set) -> list:
        redo_list = list()
        undu_list = list()
        
        for tr in tr_list:
            if (tr.get_title() in redo):
                redo_list.append(tr)
            else:
                undu_list.append(tr)

        return redo_list, undu_list


def get_name_table_1(path_json) -> str:
        with open(path_json, "r") as my_json:
            data = json.load(my_json)
        return list(data.keys())[0]
    
        
