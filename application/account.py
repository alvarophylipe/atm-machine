

class BankAccount:
    def __init__(self) -> None:

        self._account:int = None
        self._agency:int = None
        self._type:str = None
        self._name:str = None
        self._bal:float = 0
        self._passwd:str = None

    def set_all_atributes(self, account, agency, type, name, passwd) -> None:
        self._account = account
        self._agency = agency
        self._type = type
        self._name = name
        self._passwd = passwd


    def get_account(self) -> int:
        return self._account
    

    def set_account(self, x:int) -> None:
        self._account = x


    def get_agency(self) -> int:
        return self._agency
    

    def set_agency(self, x:int) -> None:
        self._agency = x


    def get_type(self) -> str:
        return self._type
    

    def set_type(self, x:str) -> None:
        self._type = x


    def get_name(self) -> str:
        return self._name
    

    def set_name(self, x:str) -> None:
        self._name = x


    def get_bal(self) -> float:
        return self._bal

    def set_bal(self, x:float) -> None: 
        self._bal = x

    def set_passwd(self, x:str) -> None:
        self._passwd = x


    def get_passwd(self) -> str:
        return self._passwd


    def sacar(self, x:float) -> None:
        if x > self._bal:
            return False
        
        if x < 0:
            return False
        
        self._bal -= x
        return True
    

    def depositar(self, x:float) -> None:
        if x < 0:
            return False
        
        self._bal += x
        return True


    def transferir(self, x:float) -> bool:
        if x > self._bal:
            return False
        
        if x < 0:
            return False
        
        self._bal -= x
        return True

    def to_dict(self) -> dict:
        data = {
            "account": self.get_account(),
            "agency": self.get_agency(),
            "type": self.get_type(),
            "name": self.get_name(),
            "balance": self.get_bal(),
            "password": self.get_passwd()
        }

        return data