from recomendation_strategy import RecomendationStrategy

class BestSellerRec(RecomendationStrategy):
    def recommend(self, user_id: str):
        return {
            'user_id': user_id, 
            'best_sellers': [
                'product1', 
                'product2', 
                'product3'
            ]
        }
