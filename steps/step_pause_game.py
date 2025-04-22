from behave import given, when, then
from pages.start_page import StartPage



def setup_game_with_players(context):
    context.page.goto(context.base_url)
    context.start_page = StartPage(context.page)

    # Ana
    context.start_page.add_player()
    context.start_page.fill_player_name("Ana")
    context.start_page.add_player()

    # Bob
    context.start_page.fill_player_name("Bob")
    context.start_page.add_player()


@given(u'spelet är i gång')
def step_given_game_is_running(context):
    setup_game_with_players(context)
    context.start_page.start_your_move()


@when(u'spelaren klickar på knappen "Pausa"')
def step_when_player_clicks_pause_button(context):
    context.start_page.click_pause_button()  # Pausa spelet


@then(u'spelet ska pausa och timern ska stanna')
def step_then_game_should_pause(context):
    is_paused = context.start_page.is_game_paused()
    assert is_paused, "Spelet är inte pausat"

    is_running = context.start_page.is_timer_running_for_player("Ana")
    assert not is_running, "Timern för Ana stannat"


@given(u'spelet är pausat')
def step_given_game_is_paused(context):
    setup_game_with_players(context)
    context.start_page.start_your_move()
    context.start_page.click_pause_button()  # Pausa spelet


@when(u'spelaren klickar på knappen "Pausa" igen')
def step_when_player_clicks_pause_button_again(context):
    context.start_page.click_pause_button()  # Starta spelet


@then(u'spelet ska återupptas och timern ska börja igen')
def step_then_game_should_resume(context):
    is_paused = context.start_page.is_game_paused()
    assert not is_paused, "Spelet återuppta"

    is_running = context.start_page.is_timer_running_for_player("Ana")
    assert is_running, "Timern för Ana har inte börjat"

@then('spelet ska visa att det är pausat')
def step_game_should_be_paused(context):
    assert context.start_page.is_game_paused(), "Spelet är inte pausat"

@then('spelet ska visa att det är återupptaget')
def step_game_should_be_resumed(context):
    assert not context.start_page.is_game_paused(), "Spelet är fortfarande pausat"
