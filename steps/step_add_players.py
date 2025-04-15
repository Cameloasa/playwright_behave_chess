from behave import given, then, when
from pages.start_page import StartPage
from playwright.sync_api import expect


@given(u'spelaren är på startsidan')
def step_given_start_page(context):
    context.page.goto(context.base_url)
    context.start_page = StartPage(context.page)

@when(u'spelaren klickar på "Lägg till spelare"')
def step_when_add_player(context):
    add_button = context.start_page.get_button_add_player()
    add_button.click(timeout= 100)

@when(u'spelaren skriver "{user}" i textfälten')
def step_when_player_types_name(context,user):
    context.start_page.fill_player_name(user)

@then(u'"{user}" dyker upp på sidan med texten "0:00.0"')
def step_then_player_name_visible(context, user):
    element = context.start_page.player_visible(user)
    expect(element).to_be_visible(timeout= 100)



