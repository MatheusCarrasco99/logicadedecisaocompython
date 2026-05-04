nome = input("Digite seu nome ")
peso = float(input("Digite seu peso "))
altura = float(input("Digite sua altura "))
imc = (peso / (altura ** 2))
print(f'Olá, {nome} sua altura é de {altura} e seu peso é de {peso}kb e seu IMC é: {imc:.3f}') #.3f representa a quantidade de número pós a vírgula