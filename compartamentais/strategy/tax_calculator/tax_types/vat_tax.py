from tax_calculator import TaxStrategy

class VatTax(TaxStrategy):
    def calculate_tax(self, value: float) -> float:
        return {
            'tax': 20,
            'value_tax': value * 1.20
        }
