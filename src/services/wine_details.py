from src.services.performance_monitor import PerformanceMonitor

class WineDetails:
    def __init__(self):
        self.wines = [
            {"name": "Vinho Tinto A", "type": "tinto", "description": "Um vinho encorpado com notas de frutas vermelhas.", "pairing": "Carnes vermelhas", "price": 50, "rating": 4.5},
            {"name": "Vinho Branco B", "type": "branco", "description": "Um vinho leve e refrescante.", "pairing": "Peixes e frutos do mar", "price": 40, "rating": 4.0},
        ]
        self.monitor = PerformanceMonitor()

    @PerformanceMonitor().measure_response_time
    def get_details(self, wine_name):
        """Retorna detalhes de um vinho específico."""
        for wine in self.wines:
            if wine["name"] == wine_name:
                return wine
        return None