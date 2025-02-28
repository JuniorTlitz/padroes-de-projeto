from payment import PaymentStrategy


class PaymentProcessor:
    def __init__(self, payment_strategy: PaymentStrategy, amount: float, installments: int):
        self._payment_strategy = payment_strategy
        self._amount = amount
        self._installments = installments
    
    @property
    def amount(self) -> float:
        return self._amount
    
    @amount.setter
    def amount(self, amount: float) -> None:
        self._amount = amount
    
    @property
    def installments(self) -> float:
        return self._installments
    
    @installments.setter
    def installments(self, installments: int) -> None:
        self._installments = installments
    
    def set_strategy(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy
    
    def process_payment(self):
        return self._payment_strategy.calculate_amount(self._amount, self._installments)
