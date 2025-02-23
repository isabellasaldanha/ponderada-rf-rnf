class WineRecommender:
    def __init__(self):
        self.user_history = [
            {"wine_name": "Vinho Tinto A", "rating": 5},
            {"wine_name": "Vinho Branco B", "rating": 4},
        ]

    def get_recommendations(self):
        """Gera recomendações com base no histórico do usuário."""
        return [
            {"name": "Vinho Tinto A", "type": "tinto", "reason": "Você avaliou este vinho com 5 estrelas"},
            {"name": "Vinho Rosé C", "type": "rosé", "reason": "Baseado em suas preferências"},
        ]