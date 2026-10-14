from database.database import register_customer, show_customers
from functions.functions import validate_name, validate_cpf, validate_age, validate_email
from datetime import date

print("1.Cadastrar\n2.Mostrar tabela")
var_menu = int(input("Escolha uma  operação:"))

match var_menu:
    case 1:
        name = validate_name()
        new_cpf = validate_cpf()        
        age = validate_age()
        email = validate_email()
        date_register = date.today()

        register_customer(name, new_cpf, age, email, str(date_register))
    
    case 2:
        result = show_customers()

        print("ID|Nome                |CPF        |Idade|email                         |Data")
        print("-----------------------------------------------------------------------------")
        for id, name, cpf, age, email, date in result:
            print(f'{id:<2}|{name:<20}|{cpf}|{age:<5}|{email:<30}|{date}')