equipamento=[]
valor=[]
seriais=[]
departamento=[]
resposta = "S"

while resposta == "S":
    equipamento.append(input("Equipamento: "))
    valor.append(float(input("Valor: ")))
    seriais.append(int(input("Número de serial: ")))
    departamento.append(input("Departamento: "))
    resposta = input('Digite "S" para continuar ').upper()

for item in equipamento:
    print("Equipamento: ", equipamento)