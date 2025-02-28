from frete import Frete


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
