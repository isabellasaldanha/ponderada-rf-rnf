#language: pt

Funcionalidade: Recomendar vinhos
  Como um usuário do WINE
  Eu quero receber recomendações de vinhos
  Para descobrir opções que combinem com o meu gosto

  Cenário: Receber recomendações com base no histórico
    Dado que eu tenho um histórico de compras e avaliações
    Quando eu acesso a página de recomendações
    Então eu devo ver uma lista de vinhos recomendados
    E o carregamento da lista deve ser concluído em menos de 2 segundos