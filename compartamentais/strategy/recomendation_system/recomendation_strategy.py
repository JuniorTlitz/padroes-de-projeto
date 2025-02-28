from abc import ABC, abstractmethod


class RecomendationStrategy(ABC):
    @abstractmethod
    def recommend(self, user_id: str):
        pass
