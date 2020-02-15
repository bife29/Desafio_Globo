import requests


print("################")
print("###### Consulta")
print("################")
print()

cep_input = input("Digite CEP")

if len(cep_input) != 8:
    print("quantidade invalida")
    exit()

requests = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

address_data = requests.json()

if 'erro' not in address_data:
    print("Cep valido")

    print("Cep: {}".format(address_data['cep']))
print(requests.json())