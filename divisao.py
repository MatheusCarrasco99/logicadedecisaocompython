num1 = float(input("Digite o dividendo "))
num2 = float(input("Digite o divisor "))
# result = num1 // num2 #O uso de uma barra na divisão o valor é real, com duas barras ele arredonda o resultado mesmo que seja float
result = num1 % num2 #Porcentagem indica o RESTO da divisão
print(f'O resultado da divisão entre {num1} e {num2} é de {result}')
