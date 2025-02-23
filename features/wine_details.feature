#language: pt

Funcionalidade: Visualizar detalhes do vinho
  Como um usuário do WINE
  Eu quero visualizar detalhes de um vinho
  Para tomar uma decisão informada sobre a compra

  Cenário: Visualizar detalhes de um vinho específico
    Dado que eu estou na página de vinhos
    Quando eu seleciono o vinho "Vinho Tinto A"
    Então eu devo ver os detalhes do vinho, incluindo descrição, harmonização e avaliações
    E o carregamento da página deve ser concluído em menos de 2 segundos