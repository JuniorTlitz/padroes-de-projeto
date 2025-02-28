from payment import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    def calculate_amount(self, amount: float, installments: int):
        if installments > 10:
            return {
                'amount': round(amount * 1.1), 
                'installments': round((amount * 1.1) / installments)
            }

        return {
            'amount': amount, 
            'installments': round(amount / installments)
        }
