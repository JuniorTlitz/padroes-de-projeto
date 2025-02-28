from recomendation_strategy import RecomendationStrategy


class TrendingRec(RecomendationStrategy):
    def recommend(self, user_id: str):
        return {
            'user_id': user_id, 
            'trending_sellers': [
                'product7', 
                'product8', 
                'product9'
            ]
        }
