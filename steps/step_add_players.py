from behave import given, when, then
from pages.start_page import StartPage
from playwright.sync_api import expect

@given(u'spelaren är på startsidan')
def step_given_start_page(context):
    context.page.goto(context.base_url)
    context.start_page = StartPage(context.page)

@when(u'spelaren klickar på knappen "Lägg till spelare"')
def step_click_add_player(context):
    context.start_page.add_player()

@when(u'spelaren skriver "{name}" i textfältet')
def step_fill_player_name(context, name):
    context.start_page.fill_player_name(name)

@then(u'"{name}" dyker upp på sidan med texten "0:00.0"')
def step_check_player_visible(context, name):
    element = context.start_page.get_player(name)
    expect(element).to_be_visible(timeout=1000)

@then(u'ingen spelare tillagd')
def step_check_no_players(context):
    expect(context.start_page.get_players()).to_have_count(0, timeout=1000)