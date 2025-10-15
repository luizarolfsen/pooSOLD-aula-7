## Violações do princípio SOLID no código

## SRP (Princípio da Responsabilidade Única)  
A classe `ProcessadorDePedidos` foi dividida em partes menores com responsabilidades específicas. Agora, `Pedido` cuida apenas dos dados do pedido, `Pagamento`, `CartaoCredito` e `Boleto` tratam do pagamento, e `Notificacao`, `Email` e `SMS` lidam com o envio de confirmação. Cada classe tem uma única razão para mudar, conforme o SRP.

## OCP (Princípio Aberto/Fechado)  
O código foi estruturado com abstrações para pagamento e notificação, permitindo adicionar novas funcionalidades sem alterar as classes existentes. Por exemplo, para incluir Pix, basta criar `Pix(Pagamento)`, e para outro canal de notificação, uma nova subclasse de `Notificacao`. A ideia está aplicada corretamente, mas o `ProcessadorDePedidos` ainda precisa invocar essas dependências para cumprir o OCP na prática.

## DIP (Princípio da Inversão de Dependência)  
O `ProcessadorDePedidos` foi ajustado para receber instâncias de pagamento e notificação via construtor (`self, pagamento, notificacao`), em vez de decidir os tipos internamente. Isso mostra intenção de injeção de dependência. No entanto, os métodos `realizar_pagamento` e `enviar_confirmacao` ainda não são chamados diretamente, então o DIP está presente conceitualmente, mas precisa de ajustes para funcionar plenamente.

## ISP (Princípio da Segregação de Interfaces)  
As interfaces foram divididas em contratos pequenos e específicos: `Notificacao` tem apenas `enviar_confirmacao`, e `Pagamento` tem `realizar_pagamento`. As classes concretas implementam apenas o que precisam, como `Email.enviar_confirmacao` e `CartaoCredito.realizar_pagamento`. Isso garante que os clientes dependam apenas dos métodos que realmente usam.

## LSP (Princípio da Substituição de Liskov)  
O design foi pensado para permitir substituição via herança e polimorfismo. `CartaoCredito` e `Boleto` seguem a mesma assinatura de `realizar_pagamento`, então o processador pode usar qualquer implementação. Para garantir o LSP por completo, é necessário padronizar `Pagamento` como uma classe abstrata (ABC com `@abstractmethod`) e remover chamadas inadequadas a `super()` em métodos abstratos. O princípio está bem encaminhado, mas ainda não totalmente implementado.
