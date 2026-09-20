from database import database
import re

while True: # Utilizalção de while true break para validação de name
    name = input("Nome:")
    len_name = len(name)
    if len_name < 20 and len_name > 0 and name.replace(" ","").isalpha(): # Utiliza replace (retira os espaços) e isalpha para validar se os caracteres são válidos (apenas letras)
        break
    else:
        print("Digite um nome válido!!!")

while True:      
    cpf = input("CPF:")
    new_cpf = re.sub(r"\D", "", cpf, count=0, flags=0)
    len_cpf = len(new_cpf)
    if len_cpf == 11:
        break
    else:
        print("Digite um CPF válido")

# age = int(input("Idade:"))
# email = input("Email:")
# date = input("Data")

