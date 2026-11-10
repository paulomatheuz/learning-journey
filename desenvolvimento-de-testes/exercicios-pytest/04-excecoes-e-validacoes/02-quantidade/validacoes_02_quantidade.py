def validar_quantidade(quantidade):
    if type(quantidade) is not int:
        raise TypeError("A quantidade deve ser um inteiro.")
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser positiva.")
    return quantidade
