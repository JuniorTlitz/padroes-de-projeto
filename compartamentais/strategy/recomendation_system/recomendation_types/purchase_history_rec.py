from recomendation_strategy import RecomendationStrategy


class PurchaseHistoryRec(RecomendationStrategy):
    def recommend(self, user_id: str):
        return {
            'user_id': user_id, 
            'PurchaseHistory': [
                'product4', 
                'product5', 
                'product6'
            ]
        }
