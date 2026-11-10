def calcular_frete(valor_compra, retirada_na_loja=False):
    if retirada_na_loja:
        return 0
    if valor_compra >= 200:
        return 0
    return 15
