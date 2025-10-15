# Refatoração do sistema de processamento de pedidos, fiz o exercício até onde consegui sem copiar código da IA.

from abc import ABC, abstractmethod

#criei uma classe apenas para representar o pedido
class Pedido:
   def __init__ (self, id, valor, cliente_email, telefone_cliente):
       self.id = id
       self.valor = valor
       self.cliente_email = cliente_email
       self.telefone_cliente = telefone_cliente

#notificação e pagamento são classes abstratas, que serão implementadas por classes concretas como Email, SMS, CartaoCredito e Boleto.

class Notificacao(ABC):
    @abstractmethod
    def enviar_confirmacao(self, pedido):
        pass

class Email(Notificacao):
    def enviar_confirmacao(self, pedido):
      super().enviar_confirmacao(pedido)
      print(f"E-mail enviado para {pedido['cliente_email']} com detalhes do pedido #{pedido['id']}.")

class SMS(Notificacao):
    def enviar_confirmacao(self, pedido):
      super().enviar_confirmacao(pedido)
      print(f"SMS enviado para {pedido['telefone cliente']} com detalhes do pedido #{pedido['id']}.")

class Pagamento:
  def realizar_pagamento(self, pedido):
      pass

class CartaoCredito(Pagamento):
    def realizar_pagamento(self, pedido):
      print(f"Processando pagamento com cartão de crédito no valor de R$ {pedido['valor']:.2f}...")
            # Lógica específica para pagamento com cartão de crédito

class Boleto(Pagamento):
    def realizar_pagamento(self, pedido):
      print(f"Gerando boleto no valor de R$ {pedido['valor']:.2f}...")
            # Lógica específica para pagamento com boleto

#tentei fazer a classe processador de pedidos receber as classes de pagamento e notificação como parâmetros, mas não consegui fazer funcionar.
class ProcessadorDePedidos:
    def __init__ (self, pedido, Pagamento, Notificacao):
        self.pedido = pedido
        self.pagamento = Pagamento
        self.notificacao = Notificacao
        print(f"Processando o pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")

        pedido['status'] = 'concluido'
        print("Pedido concluído!")

# estou com dificuldades para criar o objeto pedido e passar ele para o processador de pedidos
pedido_1 = Pedido(123, 250.75)