from recomendation_strategy import RecomendationStrategy


class RecomendationSystem():
    def __init__(self, recomendation_strategy: RecomendationStrategy, user_id: str):
        self._recomendation_strategy = recomendation_strategy
        self._user_id = user_id
    
    def set_recomendation_strategy(self, recomendation_strategy: RecomendationStrategy):
        self._recomendation_strategy = recomendation_strategy
    
    def recommend(self):
        return self._recomendation_strategy.recommend(self._user_id)
