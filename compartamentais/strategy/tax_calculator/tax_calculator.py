from tax_strategy import TaxStrategy

class TaxCalculator:
    def __init__(self, tax_strategy: TaxStrategy, value: float):
        self._value = value
        self._tax_strategy = tax_strategy
    
    def set_tax_strategy(self, tax_strategy: TaxStrategy) -> None:
        self._tax_strategy = tax_strategy
    
    def calculate_tax(self):
        return self._tax_strategy.calculate_tax(self._value)
