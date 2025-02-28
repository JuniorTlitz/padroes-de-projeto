# onde eu tenho um algoritmo que pode ser implementado de diferentes formas
from abc import ABC, abstractmethod

# Tenho minha Strategy
class Frete(ABC):
    @abstractmethod
    def calculate(self, orderValue: float):
        pass

# Implementação da interface Frete
class FreteComun(Frete):
    def calculate(self, orderValue: float) -> float:
        return orderValue * 0.05

# Implementação da interface Frete
class FreteExpresso(Frete):
    def calculate(self, orderValue: float) -> float:
        return orderValue * 0.1

class Pedido:
    def __init__(self, frete: Frete, value: float):
        self._frete = frete
        self._value = value
    
    @property
    def value(self) -> float:
        return self._value
    
    @value.setter
    def value(self, value: float) -> None:
        self._value = value
    
    def setFreteType(self, frete: Frete):
        self._frete = frete

    def calculate_shipping(self):
        return self._frete.calculate(self._value)

if __name__ == '__main__':
    pedido = Pedido(FreteComun(), 100)
    print(pedido.calculate_shipping())

    pedido = Pedido(FreteExpresso(), 100)
    print(pedido.calculate_shipping())