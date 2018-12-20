Feature: Acessa a Home da bus

  Scenario: Ver se a home existe
    Given a homepage é acessada
     When usuário procura o logotipo da bus
     Then logotipo está na página
