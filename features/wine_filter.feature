#language: pt

Funcionalidade: Filtrar vinhos por tipo
  Como um usuário do WINE
  Eu quero poder filtrar vinhos por tipo
  Para encontrar opções que atendam ao meu gosto

  Cenário: Filtrar vinhos por tipo "tinto"
    Dado que eu estou na página de vinhos para filtrar
    Quando eu seleciono o filtro "tinto"
    Então eu devo ver apenas vinhos do tipo "tinto"
    E o carregamento da lista de filtro deve ser concluído em menos de 2 segundos