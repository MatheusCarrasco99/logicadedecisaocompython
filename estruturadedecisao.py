salario = float(input("Qual é o seu salário? "))
salariomin = 1621.00
resultado = salario / salariomin
if resultado == 1:
    print(f'Você recebe {resultado:.2f} salário')
elif resultado >= 2:
    print(f'Voce recebe {resultado:.2f} salários')
else:
    print("Tu é muito pobre")
