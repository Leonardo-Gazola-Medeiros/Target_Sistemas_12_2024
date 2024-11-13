
def faturamentos():
    lista_faturamentos = []

    #Vou popular a lista automaticamente até 30(simulando os dias de um mes)
    for i in range(1,31):
        lista_faturamentos.append(i)

    menor_faturamento = min(lista_faturamentos)
    maior_faturamento = max(lista_faturamentos)
    media_faturamento = sum(lista_faturamentos)/len(lista_faturamentos)
    dias_acima_da_media = 0

    for i in lista_faturamentos:
        if i > media_faturamento:
            dias_acima_da_media += 1

    print(f"O menor faturamento do mes foi: {menor_faturamento}")
    print(f"O maior faturamento foi: {maior_faturamento}")
    print(f"A quantidade de dias acima da média foi: {dias_acima_da_media}")

    return(menor_faturamento,maior_faturamento,dias_acima_da_media)
    



faturamentos()
