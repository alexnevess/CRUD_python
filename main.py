from database.database import register_customer, show_customers, search_customer, update_customer
from functions.functions import validate_name, validate_cpf, validate_age, validate_email
from datetime import date

print("1.Cadastrar\n2.Mostrar tabela\n3.Atualizar")
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

    case 3:
        search = input("Pesquise um registro pelo CPF: ")
        old_cpf = search
        search = search_customer(search)

        name_update = validate_name(search[0])
        cpf_update = validate_cpf(str(search[1]))
        age_update = validate_age(str(search[2]))
        email_update = validate_email(search[3])
        date_update = date.today()

        update_customer(old_cpf, name_update, cpf_update, age_update, email_update, date_update)