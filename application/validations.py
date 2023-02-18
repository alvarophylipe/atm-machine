
def number_valid(text:str= "", condition=None) -> float|int:

    try:
        number = float(input(f"{text}>>> "))
        if number < 0:
            print("| Valor Inferior a 0!")
            return number_valid(text=text, condition=condition)

        if condition == None:
            return number

        if number in condition:
            return number
        else:
            return number_valid(text=text, condition=condition)
    except Exception:
        print("| Valor Inválido!")
        return number_valid(text=text, condition=condition)
    



def type_valid() -> str:
    option = ["Corrente", "Poupanca"]
    
    type = input("| Tipo (Corrente, Poupanca) >>> ").title()
    
    if type not in option:
        type_valid()
    
    return type
        


if __name__ == "__main__":
    print(number_valid(condition=[0,5]))