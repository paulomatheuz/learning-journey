def somar_por_categoria(itens):
    totais = {}
    for item in itens:
        categoria = item["categoria"]
        totais[categoria] = totais.get(categoria, 0) + item["valor"]
    return totais
