from frete import Frete


class FreteExpresso(Frete):
    def calculate(self, orderValue: float) -> float:
        return orderValue * 0.1