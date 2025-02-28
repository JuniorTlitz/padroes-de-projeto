from abc import ABC, abstractmethod

class TaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, value: float) -> float:
        pass