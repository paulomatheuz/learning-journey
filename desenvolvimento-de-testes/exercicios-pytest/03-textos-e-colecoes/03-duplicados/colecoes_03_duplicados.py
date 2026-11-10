def remover_duplicados(numeros):
    resultado = []
    for numero in numeros:
        if numero not in resultado:
            resultado.append(numero)
    return resultado
