import json
import os
import sys

class DataManager():

    def __init__(self) -> None:
        self.account = None
        self.FILE_PATH = "./data/data.json"
    
    def data_create(self):
        while True:
            try:
                f = open(self.FILE_PATH, 'x')
                with open(self.FILE_PATH, 'w') as file:
                    file.write("[]")
                print('Arquivo Criado com Sucesso!')
            except Exception:
                break
    
    
    def data_access(self):

        self.data_create()

        with open(self.FILE_PATH, encoding='utf-8') as read_file:
            data = json.load(read_file)
        
        return data


    def data_sign_up(self, object) -> bool:
        
        self.data_create()

        if self.data_validation(object):

            data_list = self.data_access()
            data_list.append(object.to_dict())

            self.data_write(data_list=data_list)

            print("| Conta Criada com Sucesso!")
            return True
        else:
            print("| Cadastro já existente!")
            return False


    def data_write(self, data_list):
        with open(self.FILE_PATH, 'w') as write_file:
            json.dump(data_list, write_file, indent=4)
    
    
    def data_delete(self, account:int, agency:int):
        data_list= self.data_access()

        delete = False

        for item in data_list:
            if item['account'] == account and item['agency'] == agency:
                data_list.remove(item)
                delete = True

        self.data_write(data_list=data_list)

        if not delete:
            print('| Conta inexistente!')


    def data_validation(self, object) -> bool:
        data_list = self.data_access()

        if len(data_list) == 0:
            return True

        for item in data_list:
            if item['account'] != object.get_account() or item['agency'] != object.get_agency():
                return True
        
        return False


    def data_update(self, object, return_name=False) -> None|str:
        data_list = self.data_access()

        for item in data_list:
            if (item['account'] == object.get_account()) and \
                (item['agency'] == object.get_agency()):

                item['balance'] = object.get_bal()
                
        self.data_write(data_list=data_list)



    def data_verification(self, account:int, agency:int) -> bool:
        data_list = self.data_access()

        for item in data_list:
            if item['account'] == account and \
                item['agency'] == agency:
                return True
        
        return False

    def get_data(self, account:int, agency=int) -> tuple:
        data_list = self.data_access()
        data = []

        for item in data_list:
            if item['account'] == account and \
                item['agency'] == agency:
                for key, value in item.items():
                    data.append(value)
        
        return tuple(data)



    def passwd_validation(self, account, agency, passwd) -> bool:
        data_list = self.data_access()

        for item in data_list:
            if item['account'] == account and \
                item['agency'] == agency and \
                item['password'] == passwd:
                return True
        
        return False
                



if __name__=='__main__':
    manager = DataManager()

    manager.data_delete(account=103, agency=20)