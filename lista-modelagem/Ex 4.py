class Pedido:
    ESTADOS = ["Pendente", "Processando", "Enviado", "Entregue"]

    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self.__status = "Pendente"

    def status(self):
        return self.__status

    def atualizar_status(self, novo_status):
        if novo_status not in self.ESTADOS:
            raise ValueError("Status inválido.")
        if self.ESTADOS.index(novo_status) <= self.ESTADOS.index(self.__status):
            raise ValueError("Não é possível retroceder o status.")
        self.__status = novo_status

