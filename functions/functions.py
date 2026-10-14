from prompt_toolkit import prompt
import re

def validate_name(name = None):
    while True: # Utilizalção de while true break para validação de name
                name = prompt("Nome: ", default = "")
                len_name = len(name)
                if len_name < 20 and len_name > 0 and name.replace(" ","").isalpha(): # Utiliza replace (retira os espaços) e isalpha para validar se os caracteres são válidos (apenas letras)
                    return(name)
                else:
                    print("Digite um nome válido!!!")

def validate_cpf(cpf = None):
      while True:      
                  cpf = prompt("CPF: ", default = "")
                  new_cpf = re.sub(r"\D", "", cpf, count=0, flags=0)
                  len_cpf = len(new_cpf)
                  if len_cpf == 11:
                      return(new_cpf)
                  else:
                      print("Digite um CPF válido")

def validate_age(age = None):
      while True:
                  try:
                      age = int(prompt("Idade: ", default = ""))
                      if age > 0 and age < 100:
                          return(age)
                      else:
                          print("Digite uma idade válida!")
                  except ValueError:
                      print("Digite um número válido")

def validate_email(email = None):
      while True:
                  email = prompt("email: ", default = "")
                  if "@" in email and "." in email:
                      return(email)
                  else:
                      print("Digite um email válido")