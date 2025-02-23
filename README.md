# Estudo de caso - RNF como código de controle de qualidade (WINE) 

## Descrição do Problema

A **WINE** é um clube de vinhos por assinatura que oferece uma plataforma digital para seus clientes explorarem, selecionarem e receberem vinhos personalizados. A plataforma precisa ser altamente eficiente e personalizada, garantindo que os usuários encontrem vinhos que atendam aos seus gostos e preferências. Além disso, a experiência do usuário deve ser fluida, com tempos de carregamento rápidos e recomendações precisas.

## Requisitos

### Requisitos Funcionais (RF)

**Requisito Funcional - Filtragem de Vinhos por Tipo (RF-001)**

Descrição: O sistema deve permitir que os usuários filtrem vinhos por tipo (tinto, branco, rosé) para encontrar opções que atendam ao seu gosto.

Critérios de Aceitação:

- O sistema deve exibir uma lista de vinhos filtrados com base no tipo selecionado.

- O sistema deve carregar a lista de vinhos filtrados em menos de 2 segundos.

- O sistema deve exibir uma mensagem clara caso não haja vinhos disponíveis para o tipo selecionado.

**Requisito Funcional - Recomendação de Vinhos (RF-002)**

Descrição: O sistema deve recomendar vinhos com base no histórico de compras e avaliações do usuário.
Critérios de Aceitação:

- O sistema deve analisar o histórico de compras e avaliações do usuário para gerar recomendações personalizadas.

- O sistema deve garantir que as recomendações sejam carregadas em menos de 2 segundos.

**Requisito Funcional - Detalhes do Vinho (RF-003)**

Descrição: O sistema deve exibir detalhes completos de um vinho selecionado, incluindo descrição, harmonização, preço e avaliações de outros usuários.

Critérios de Aceitação:

- O sistema deve garantir que a página de detalhes seja carregada em menos de 2 segundos.

- O sistema deve permitir que o usuário visualize avaliações de outros usuários, incluindo notas e comentários.

- O sistema deve exibir sugestões de harmonização (ex: pratos que combinam com o vinho).

### Requisitos Não Funcionais (RNF)

**Requisito Não Funcional - Desempenho do Sistema (RNF-001)**

Descrição: O sistema deve garantir alta disponibilidade, desempenho e segurança para suportar a plataforma de vinhos, assegurando que todas as requisições sejam processadas rapidamente e que os dados dos usuários sejam armazenados de forma segura.
Critérios de Aceitação:

- O sistema deve responder a todas as requisições em menos de 2 segundos, mesmo durante picos de acesso.

- O sistema deve estar disponível 99,9% do tempo, com monitoramento contínuo e alertas em caso de indisponibilidade.

- O sistema deve ser capaz de suportar um aumento de 50% no número de usuários simultâneos sem degradação do desempenho.



