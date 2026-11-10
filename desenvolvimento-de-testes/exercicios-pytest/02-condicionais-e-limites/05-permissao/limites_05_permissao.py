def pode_acessar(ativo, bloqueado, possui_permissao):
    return ativo and not bloqueado and possui_permissao
