import time

class PerformanceMonitor:
    @staticmethod
    def measure_execution_time(func):
        """Decorador para medir o tempo de execução de uma função."""
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"{func.__name__} executado em {execution_time:.4f} segundos")
            return result
        return wrapper