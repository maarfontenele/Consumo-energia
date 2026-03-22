
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (W): "))
horas_dia = float(input("Digite o tempo de uso diário (horas): "))

consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * 0.75

print("-" * 30)
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")
print("-" * 30)
