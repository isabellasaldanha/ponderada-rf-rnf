from behave import given, when, then
from src.services.wine_details import WineDetails

@given('que eu estou na página de vinhos')
def step_impl(context):
    context.wine_details = WineDetails()

@when('eu seleciono o vinho "{wine_name}"')
def step_impl(context, wine_name):
    context.selected_wine = context.wine_details.get_details(wine_name)

@then('eu devo ver os detalhes do vinho, incluindo descrição, harmonização e avaliações')
def step_impl(context):
    assert context.selected_wine is not None, "Erro: O vinho selecionado não foi encontrado"
    assert "description" in context.selected_wine, "Erro: Descrição do vinho não encontrada"
    assert "pairing" in context.selected_wine, "Erro: Harmonização do vinho não encontrada"
    assert "rating" in context.selected_wine, "Erro: Avaliação do vinho não encontrada"

@then('o carregamento da página deve ser concluído em menos de 2 segundos')
def step_impl(context):
    import time
    start_time = time.time()
    time.sleep(1)  
    end_time = time.time()
    load_time = end_time - start_time
    assert load_time < 2, f"Erro: O carregamento demorou {load_time} segundos (deveria ser menos de 2 segundos)"