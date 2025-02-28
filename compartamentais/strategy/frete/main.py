from type_pedidos.frete_comum import FreteComun
from type_pedidos.frete_expresso import FreteExpresso
from pedido import Pedido

if __name__ == '__main__':
    pedido = Pedido(FreteComun(), 100)
    print(pedido.calculate_shipping())

    pedido = Pedido(FreteExpresso(), 100)
    print(pedido.calculate_shipping())