from calculo_imposto import TaxStrategy


class GstTax(TaxStrategy):
    def calculate_tax(self, value: float) -> float:
        return {
            'tax': '17%',
            'value_tax': value * 1.17 
        }
