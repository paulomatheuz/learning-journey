# Anotações sobre testes

# Teardown
Teardown é a etapa de limpeza após um teste. Ela desfaz o que foi preparado para que um teste não atrapalhe os próximos.

Por exemplo:
- Fechar uma conexão com o banco de dados.
- Apagar um arquivo temporário.
- Fechar o navegador usado no teste.

O fluxo é: setup (preparar) → teste (verificar) → teardown (limpar).

# Escopo de Fixtures:
- Function: Padrão. Criada e Destruída para cada função que utilizar ela.
- Class: Criada e Destruída uma vez para cada instância da Classe.
- Module: Criada e Destruída uma vez para cada módulo ou o equivalente ao Arquivo de teste. Ela será compartilhada para todos os testes.
- Package: Criada e Destruída uma vez para cada Package.
- Session: Toda a seção de testes compartilha a mesma fixture.