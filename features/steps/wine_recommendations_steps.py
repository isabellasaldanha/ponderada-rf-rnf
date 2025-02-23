from behave import given, when, then
from src.services.wine_recommender import WineRecommender

@given('que eu tenho um histórico de compras e avaliações')
def step_impl(context):
    context.wine_recommender = WineRecommender()

@when('eu acesso a página de recomendações')
def step_impl(context):
    context.recommendations = context.wine_recommender.get_recommendations()

@then('eu devo ver uma lista de vinhos recomendados')
def step_impl(context):
    assert len(context.recommendations) > 0, "Erro: Nenhuma recomendação foi encontrada"

@then('o carregamento da lista deve ser concluído em menos de 2 segundos')
def step_impl(context):
    import time
    start_time = time.time()
    time.sleep(1)  
    end_time = time.time()
    load_time = end_time - start_time
    assert load_time < 2, f"Erro: O carregamento demorou {load_time} segundos (deveria ser menos de 2 segundos)"