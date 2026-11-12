# MARCADORES NO PYTEST
- Permite organizar testes através de categorias
- Atribuímos 'etiquetas' aos testes
- Execução seletiva por (etiquetas) feitas através de um decorador

# EXEMPLOS:
- Testes apenas certas funcionalidades:
  - Conexões
  - Carga de Dados
  - Transformação

- Sistema de Gestão:
  - Emissão da Nota Fiscal
  - Módulo Contábil
  - Importação de arquivos

# TIPOS DE TESTES: (DÁ PRA RODAR SOMENTE ESSES. CATEGORIZA POR TIPO DE TESTE)
  - Testes unitários (verifica o comportamento da menor parte testável do programa);

  - Testes de integração (verifica uma "parte funcional" ex: o módulo de login);

  - Testes de interface de usuário UI (verifica os elementos visuais da interface "botões, menus, formulários, cores e etc");

  - Testes de acesso ao banco de dados (veerifica se a aplicação consegue ler, gravar, atualizar e excluir dados (CRUD));

  - Testes de API (verifica se a API "ponte" entre sistemas, responde corretamente quando recebe uma requisição).



  Dá pra executar todos menos um com uma marca específica.
  EXEMPLO: python -m pytest -m "not lento"