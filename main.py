from database import database

while True: # Utilizalção de while true break para validação de name
    len_name = 0
    name = input("Nome:")
    len_name = len(name)
    if len_name < 20 and len_name > 0 and name.replace(" ","").isalpha(): # Utiliza replace (retira os espaços) e isalpha para validar se os caracteres são válidos (apenas letras)
        break
    else:
        print("Digite um nome válido!!!")
        
# cpf = input("CPF:")
# age = int(input("Idade:"))
# email = input("Email:")
# date = input("Data")

