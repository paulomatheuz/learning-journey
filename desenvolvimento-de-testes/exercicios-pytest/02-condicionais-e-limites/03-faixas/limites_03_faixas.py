def classificar_pontuacao(pontos):
    if pontos < 50:
        return "iniciante"
    if pontos < 80:
        return "intermediario"
    return "avancado"
