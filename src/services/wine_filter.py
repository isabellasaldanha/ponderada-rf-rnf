from src.services.performance_monitor import PerformanceMonitor

class WineFilter:
    def __init__(self):
        self.wines = [
            {"name": "Vinho Tinto A", "type": "tinto", "price": 50, "region": "Rio Grande do Sul"},
            {"name": "Vinho Branco B", "type": "branco", "price": 40, "region": "Santa Catarina"},
            {"name": "Vinho Rosé C", "type": "rosé", "price": 60, "region": "São Paulo"},
        ]
        self.monitor = PerformanceMonitor()

    @PerformanceMonitor().measure_response_time
    def filter_by_type(self, wine_type):
        """Filtra vinhos por tipo."""
        return [wine for wine in self.wines if wine["type"] == wine_type]

    @PerformanceMonitor().measure_response_time
    def filter_by_price_range(self, min_price, max_price):
        """Filtra vinhos por faixa de preço."""
        return [wine for wine in self.wines if min_price <= wine["price"] <= max_price]