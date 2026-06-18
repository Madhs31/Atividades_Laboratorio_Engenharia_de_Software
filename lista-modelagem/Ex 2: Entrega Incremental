class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    def get_preco(self):
        return self.__preco

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.get_preco() * self.quantidade
