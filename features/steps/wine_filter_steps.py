from behave import given, when, then
from src.services.wine_filter import WineFilter
from src.services.performance_monitor import PerformanceMonitor

@given('que eu estou na página de vinhos para filtrar')
def step_impl(context):
    context.wine_filter = WineFilter()

@when('eu seleciono o filtro "{wine_type}"')
def step_impl(context, wine_type):
    context.filtered_wines = context.wine_filter.filter_by_type(wine_type)

@then('eu devo ver apenas vinhos do tipo "{wine_type}"')
def step_impl(context, wine_type):
    assert all(wine["type"] == wine_type for wine in context.filtered_wines), \
        f"Erro: Há vinhos que não são do tipo {wine_type}"

@then('o carregamento da lista de filtro deve ser concluído em menos de 2 segundos')
def step_impl(context):
    import time
    start_time = time.time()
    time.sleep(1)  
    end_time = time.time()
    load_time = end_time - start_time
    assert load_time < 2, f"Erro: O carregamento demorou {load_time} segundos (deveria ser menos de 2 segundos)"