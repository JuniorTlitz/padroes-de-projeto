from payment import PaymentStrategy


class BoletoPayment(PaymentStrategy):
    def calculate_amount(self, amount: float, installments = 0):
        return {
            'amount': amount
        }
