from calculo_imposto import TaxStrategy


class SalesTax(TaxStrategy):
    def calculate_tax(self, value: float) -> float:
        return {
            'SP': {
                'tax': 18,
                'value_tax': value * 1.18,
            },
            'RJ': {
                'tax': 20,
                'value_tax': value * 1.20,
            },
            'MG': {
                'tax': 25,
                'value_tax': value * 1.25,
            },
        }