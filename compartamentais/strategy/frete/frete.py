# Tenho minha Strategy
from abc import ABC, abstractmethod


class Frete(ABC):
    @abstractmethod
    def calculate(self, orderValue: float):
        pass