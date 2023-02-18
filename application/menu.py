

def header() -> None:
    print('+',''.center(96,'-'), '+')
    print('|', 'ATM Machine'.center(96, ' '), '|')
    print('+',''.center(96,'-'), '+')


def inicial() -> None:
    header()
    print("|", " ".center(96, " "), "|")
    print("|", "(1) LOGIN".center(96, " "), "|")
    print("|", "(2) CADASTRAR".center(96, " "), "|")
    print("|", "(0) SAIR".center(96, " "), "|")
    print("|", " ".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def principal(account:int, agency:int) -> None:
    header()
    print("|", " ".center(96, " "), "|")
    print("|", f"Conta: {account}  Agencia: {agency}".center(96," "), "|")
    print("|", " ".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")
    print("|", " ".center(96, " "), "|")
    print("|", "(1) SACAR".center(96, " "), "|")
    print("|", "(2) DEPOSITAR".center(96, " "), "|")
    print("|", "(3) EXTRATO".center(96, " "), "|")
    print("|", "(4) TRANSFERIR".center(96, " "), "|")
    print("|", "(5) EXCLUIR CONTA".center(96, " "), "|")
    print("|", "(0) SAIR".center(96, " "), "|")
    print("|", " ".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def sacar_tela(account:int, agency:int) -> None:
    header()
    print("|", " ".center(96, " "), "|")
    print("|", f"Conta: {account}  Agencia: {agency}".center(96," "), "|")
    print("|", " ".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def sacar_sucesso(value:float|int) -> None:
    print("+", "".center(96, "-"), "+")
    print("|", f"VALOR DE R$ {value:.2f} SACADO".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def sacar_error() -> None:
    print("+", "".center(96, "-"), "+")
    print("|", "VALOR INSUFICIENTE/INVÁLIDO".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def depositar_tela(account:int, agency:int) -> None:
    header()
    print("|", " ".center(96, " "), "|")
    print("|", f"Conta: {account}  Agencia: {agency}".center(96," "), "|")
    print("|", " ".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def depositar_sucesso(value:float|int) -> None:
    print("+", "".center(96, "-"), "+")
    print("|", f"VALOR DE R$ {value:.2f} DEPOSITADO".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def depositar_error() -> None:
    print("+", "".center(96, "-"), "+")
    print("|", "VALOR INVÁLIDO".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def transferir_tela(account:int, agency:int) -> None:
    header()
    print("|", " ".center(96, " "), "|")
    print("|", f"Conta: {account}  Agencia: {agency}".center(96," "), "|")
    print("|", " ".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def transferir_sucesso(value:float|int, nome:str) -> None:
    print("+", "".center(96, "-"), "+")
    print("|", f"VALOR DE R$ {value:.2f} TRANSFERIDO PARA {nome.upper()}".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def transferir_error() -> None:
    print("+", "".center(96, "-"), "+")
    print("|", "VALOR INSUFICIENTE/INVÁLIDO".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def extrato_tela(account:int, agency:int, bal:float|int) -> None:
    header()
    print("|", " ".center(96, " "), "|")
    print("|", f"Conta: {account}  Agencia: {agency}".center(96," "), "|")
    print("|", " ".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")
    print("|", " ".center(96, " "), "|")
    print("|", f"SALDO: R$ {bal:.2f}".center(96, " "), "|")
    print("|", " ".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def delete_tela() -> None:
    header()
    print("|", " ".center(96, " "), "|")
    print("|", "[0] - Transferir o dinheiro".center(96, " "), "|")
    print("|", "[1] - Apagar para sempre".center(96, " "), "|")
    print("|", " ".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def apagar() -> None:
    print("+", "".center(96, "-"), "+")
    print("|", "APAGANDO...".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")


def encerrar() -> None:
    print("+", "".center(96, "-"), "+")
    print("|", "ENCERRANDO...".center(96, " "), "|")
    print("+", "".center(96, "-"), "+")