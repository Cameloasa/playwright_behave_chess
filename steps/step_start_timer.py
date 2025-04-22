
from behave import given, when, then
from pages.start_page import StartPage
from playwright.sync_api import expect

def setup_game_with_players(context):
    context.page.goto(context.base_url)
    context.start_page = StartPage(context.page)

    # Add Ana
    context.start_page.add_player()  # ← face input-ul să apară
    context.start_page.fill_player_name("Ana")
    context.start_page.add_player()

    # Add Bob
    context.start_page.fill_player_name("Bob")
    context.start_page.add_player()

@given(u'två spelare "Ana" och "Bob" är tillagda')
def step_given_two_players(context):
    setup_game_with_players(context)
    players = context.start_page.get_players()
    expect(players).to_have_count(2)

@when(u'spelaren klickar på knappen "Börja ditt drag"')
def step_when_start_your_move_button(context):
    context.start_page.start_your_move()

@then(u'timern för "{name}" börjar räkna')
def step_then_timer_starts_for_player(context, name):
    is_running = context.start_page.is_timer_running_for_player(name)
    print(f"[DEBUG] Timer for {name} is running: {is_running}")
    assert is_running, f"Timern för {name} har inte börjat räkna"

@then(u'knappen visar texten "Överlämna till {name}"')
def step_then_show_text(context,name):
    button = context.start_page.get_active_move_button()
    expect(button).to_have_text(f"Överlämna till {name}", timeout=1000)


@given(u'spelaren "Ana" har påbörjat sin tur')
def step_given_player_start_turn(context):
    setup_game_with_players(context)
    context.start_page.start_your_move()






