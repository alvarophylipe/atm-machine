from .account import BankAccount
from .datamanager import DataManager
from application import menu
from .validations import number_valid, type_valid
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Machine:
    def __init__(self) -> None:
        self._bank_account = BankAccount()
        self.manager = DataManager()
        self._temp_account = None
        self._temp_agency = None
        self._temp_bal = None


    def update_temp_data(self) -> None:
        self._temp_account = self._bank_account.get_account()
        self._temp_agency = self._bank_account.get_agency()
        self._temp_bal = self._bank_account.get_bal()


    def set_data(self, tup:tuple, config=False) -> None:
        account, agency, type, nome, bal, passwd = tup
        temp_acc = BankAccount()
        temp_acc.set_all_atributes(type=type, account=account, agency=agency, name=nome, passwd=passwd)
        temp_acc.set_bal(bal)

        if config:
            self._bank_account = temp_acc
            self.update_temp_data()

        return temp_acc


    def option_inicial(self) -> int:
        menu.inicial()
        return number_valid(text="| ", condition=[0,1,2])
    

    def option_principal(self) -> int:
        menu.principal(self._temp_account, self._temp_agency)
        return number_valid(text="| ", condition=[0,1,2,3,4,5])

        
    def login(self) -> None:
        clear()
        menu.header()

        while True:
            print('| Conta ', end="")
            account = int(number_valid())
            break

        while True:
            print("| Agencia ", end="")
            agency = int(number_valid())
            break
        
        passwd = input("| Senha >>> ")

        if self.manager.passwd_validation(account=account, agency=agency, passwd=passwd):
            self.set_data(self.manager.get_data(account=account, agency=agency), config=True)
            self.home_page()

        else:
            self.run()


    def sign_up(self) -> None:
        clear()
        menu.header()

        while True:
            print('| Conta ', end="")
            account = int(number_valid())
            break

        while True:
            print("| Agencia ", end="")
            agency = int(number_valid())
            break
        
        type = type_valid()
        nome = input("| Titular >>> ").title()
        passwd = input("| Senha >>> ")

        new_acc = BankAccount()
        new_acc.set_all_atributes(account=account, agency=agency,
                                type=type, name=nome, passwd=passwd)
        
        if not self.manager.data_sign_up(new_acc):
            print('+',''.center(96,'-'), '+')
            print("| (1) Tentar novamente? \n| (0) Voltar pro menu")
            op = int(input(">>> "))
            
            if op == 1:
                self.sign_up()
            else:
                self.run()
        
        else:
            self._bank_account = new_acc
            self.home_page()
        
    
    def sacar_option(self) -> None:
        clear()
        menu.sacar_tela(self._temp_account, self._temp_agency)

        value = number_valid(text="| Valor a sacar [Encerrar - 0] ")

        if self._bank_account.sacar(value):
            self.manager.data_update(self._bank_account)
            self.update_temp_data()
            clear()
            menu.sacar_sucesso(value)
            sleep(2)
            self.home_page()
        else:
            clear()
            menu.sacar_error()
            sleep(2)
            self.sacar_option()


    def depositar_option(self) -> None:
        clear()
        menu.depositar_tela(self._temp_account, self._temp_agency)
        
        value = number_valid(text="| Valor a depositar ")

        if self._bank_account.depositar(value):
            self.manager.data_update(self._bank_account)
            self.update_temp_data()
            clear()
            menu.depositar_sucesso(value)
            sleep(2)
            self.home_page()
        else:
            clear()
            menu.depositar_error()
            sleep(2)
            self.depositar_option()


    def transferir_option(self) -> None:
        clear()
        menu.transferir_tela(self._temp_account, self._temp_agency)

        account = number_valid(text="| Digite a Conta [Encerrar - 0] ")
        agency = number_valid(text="| Digite a Agencia [Encerrar - 0] ")

        if account == 0 or agency == 0:
            self.home_page()

        if self.manager.data_verification(account=account, agency=agency):

            acc = self.set_data(self.manager.get_data(account=account, agency=agency))
            value = number_valid(text="| Digita o valor a transferir [Tudo - 0]")

            if value == 0:
                value = self._temp_bal

            if self._bank_account.transferir(value):
                acc.set_bal(acc.get_bal() + value)
                self.manager.data_update(acc)
                self.manager.data_update(self._bank_account)
                self.update_temp_data()
                clear()
                menu.transferir_sucesso(value=value, nome=acc.get_name())
                sleep(2)
                self.home_page()

            else:
                clear()
                menu.transferir_error()
                sleep(2)
                self.transferir_option()


    def delete_account(self) -> None:
        clear()
        menu.delete_tela()

        option = number_valid(text="| ")

        if option == 0:
            self.transferir_option()
        
        if option == 1:
            clear()
            self.manager.data_delete(self._temp_account, self._temp_agency)
            menu.apagar()
            sleep(2)
            self.run()


    def home_page(self) -> None:
        clear()
        option = self.option_principal()

        if option == 1:
            self.sacar_option()

        if option == 2:
            self.depositar_option()

        if option == 3:
            clear()
            menu.extrato_tela(self._temp_account, self._temp_agency, self._temp_bal)
            sleep(3)
            self.home_page()
            
        if option == 4:
            self.transferir_option()
        
        if option == 5:
            self.delete_account()

        if option == 0:
            clear()
            self.run()



    def run(self) -> None:
        clear()
        option = self.option_inicial()

        if option == 1:
            self.login()
        
        if option == 2:
            self.sign_up()
        
        if option == 0:
            clear()
            menu.encerrar()
            sleep(2)
            clear()
            return

    

if __name__=='__main__':
    object = Machine()
    object.run()