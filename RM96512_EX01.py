value = float(input('Qual foi o seu faturamento em R$ '))
subscribe = input('Qual é a sua categoria: BASIC, SILVER, GOLD ou PLATINUM ').upper()


BASIC = value * 0.30
SILVER = value * 0.20
GOLD = value * 0.10
PLATINUM = value * 0.05

if subscribe == "BASIC":
    print(f"A taxa total a ser paga é de R${BASIC: .2f}")
elif subscribe == "SILVER":
    print(f"A taxa total a ser paga é de R${SILVER: .2f}")
elif subscribe == "GOLD":
    print(f"A taxa total a ser paga é de R${GOLD: .2f}")
elif subscribe == "PLATINUM":
    print(f"A taxa total a ser paga é de R${PLATINUM: .2f}")
else:
    print("Por favor, digite uma categoria que exista")