def percentual_desconto(valor_compra, cliente_vip=False):
    if cliente_vip:
        return 20
    if valor_compra >= 100:
        return 10
    return 0
