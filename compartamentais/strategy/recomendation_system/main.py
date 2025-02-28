from recomendation_types.best_seller_rec import BestSellerRec
from recomendation_types.purchase_history_rec import PurchaseHistoryRec
from recomendation_types.trending_rec import TrendingRec
from recomendation_system import RecomendationSystem


if __name__ == '__main__':
    recomendation_system = RecomendationSystem(BestSellerRec(), 'user_id_1')
    print(recomendation_system.recommend())

    recomendation_system = RecomendationSystem(PurchaseHistoryRec(), 'user_id_2')
    print(recomendation_system.recommend())

    recomendation_system = RecomendationSystem(TrendingRec(), 'user_id_3')
    print(recomendation_system.recommend())
