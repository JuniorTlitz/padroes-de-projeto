from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def calculate_amount(self, amount: float, installments: int):
        pass
