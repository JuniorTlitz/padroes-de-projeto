from tax_calculator import TaxCalculator
from tax_types.gst_tax import GstTax
from tax_types.sales_tax import SalesTax
from tax_types.vat_tax import VatTax

if __name__ == '__main__':
    tax_calculator = TaxCalculator(GstTax(), 100)
    print(tax_calculator.calculate_tax())

    tax_calculator = TaxCalculator(SalesTax(), 1000)
    print(tax_calculator.calculate_tax())

    tax_calculator = TaxCalculator(VatTax(), 10000)
    print(tax_calculator.calculate_tax())

