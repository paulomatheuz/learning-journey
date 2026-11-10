def contar_vogais(texto):
    return sum(1 for caractere in texto.lower() if caractere in "aeiou")
