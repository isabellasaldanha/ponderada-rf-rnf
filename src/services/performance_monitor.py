import time
from datetime import datetime, timedelta

class PerformanceMonitor:
    def __init__(self):
        self.request_times = []  
        self.system_uptime = datetime.now() 
        self.downtime = timedelta(0)  

    def measure_response_time(self, func):
        """
        Decorador para medir o tempo de resposta de uma função.
        """
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            response_time = end_time - start_time
            self.request_times.append(response_time)
            return result
        return wrapper

    def calculate_availability(self):
        """
        Calcula a disponibilidade do sistema.
        """
        total_time = datetime.now() - self.system_uptime
        if total_time.total_seconds() == 0:
            return 100.0  
        uptime = total_time - self.downtime
        availability = (uptime.total_seconds() / total_time.total_seconds()) * 100
        return availability

    def simulate_downtime(self, seconds):
        """
        Simula uma indisponibilidade no sistema.
        """
        self.downtime += timedelta(seconds=seconds)

    def check_scalability(self, current_users, additional_users):
        """
        Verifica se o sistema pode suportar um aumento de 50% no número de usuários.
        """
        new_users = current_users + additional_users
        return new_users <= current_users * 1.5