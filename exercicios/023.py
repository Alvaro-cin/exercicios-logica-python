nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 100:
    print("Aprovado com Distinção")
elif media >= 70:
    print("Aprovado")
else:
    print("Reprovado")