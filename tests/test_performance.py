import unittest
import time
from src.services.performance_monitor import PerformanceMonitor

class TestPerformanceMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = PerformanceMonitor()

    def test_response_time(self):
        """
        Testa se o tempo de resposta é menor que 2 segundos.
        """
        @self.monitor.measure_response_time
        def mock_request():
            time.sleep(1)  
            return "Resposta"

        response = mock_request()

        self.assertLess(self.monitor.request_times[-1], 2, "Erro: O tempo de resposta excedeu 2 segundos")

    def test_availability(self):
        """
        Testa se a disponibilidade do sistema é de 99,9%.
        """
        time.sleep(1)

        # Simula 0,001 segundos de indisponibilidade
        self.monitor.simulate_downtime(0.001)

        availability = self.monitor.calculate_availability()

        self.assertGreaterEqual(availability, 99.9, "Erro: A disponibilidade do sistema é inferior a 99,9%")

    def test_scalability(self):
        """
        Testa se o sistema suporta um aumento de 50% no número de usuários.
        """
        current_users = 1000
        additional_users = 500 

        is_scalable = self.monitor.check_scalability(current_users, additional_users)
        self.assertTrue(is_scalable, "Erro: O sistema não suporta um aumento de 50% no número de usuários")