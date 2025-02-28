from payment_types.payment_boleto import BoletoPayment
from payment_types.payment_credit import CreditCardPayment
from payment_types.payment_pix import PixPayment
from payment_processor import PaymentProcessor

if __name__ == '__main__':
    payment_processor = PaymentProcessor(BoletoPayment(), 100, None)
    print(payment_processor.process_payment())

    payment_processor = PaymentProcessor(CreditCardPayment(), 100, 10)
    print(payment_processor.process_payment())

    payment_processor = PaymentProcessor(CreditCardPayment(), 100, 12)
    print(payment_processor.process_payment())

    payment_processor = PaymentProcessor(PixPayment(), 100, None)
    print(payment_processor.process_payment())
