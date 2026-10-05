bateria = float(input("Bateria atual (%): "))
duracao = float(input("Duração da missão (minutos): "))
consumo_por_minuto = float(input("Consumo por minuto (%): "))


consumo_total = duracao * consumo_por_minuto

if bateria < 0 or bateria > 100 or duracao <= 0 or consumo_por_minuto <= 0:
    print("Valor inválido.")
else:
    if consumo_total <= bateria:
        bateria_restante = bateria - consumo_total
        print(f"Missão pode ser concluída. Bateria restante: {bateria_restante:.2f}%.")
    else:
        faltam = consumo_total - bateria
        print(f"Missão não pode ser concluída. Faltam {faltam:.2f} pontos percentuais de bateria.")
