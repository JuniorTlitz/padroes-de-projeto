from frete import Frete


class FreteComun(Frete):
    def calculate(self, orderValue: float) -> float:
        return orderValue * 0.05