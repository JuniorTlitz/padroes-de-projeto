from payment import PaymentStrategy


class PixPayment(PaymentStrategy):
    def calculate_amount(self, amount: float, installments = 0):
        return {
            'amount': round(amount - (amount * 0.1))
        }
