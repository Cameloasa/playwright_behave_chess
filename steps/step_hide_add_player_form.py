from behave import given, when, then
from playwright.sync_api import expect
from pages.start_page import StartPage

@given(u'knappen "Lägg till spelare" är synlig')
def step_given_add_button_is_visible(context):
    expect(context.start_page.get_add_button()).to_be_visible(timeout=1000)

@then(u'formuläret för att lägga till spelare visas')
def step_then_form_is_visible(context):
    label, input_text = context.start_page.get_form_elements()
    expect(label).to_be_visible(timeout=1000)
    expect(input_text).to_be_visible(timeout=1000)

@when(u'spelaren klickar pe knappen "Dölj"')
def step_when_click_hide_button(context):
    context.start_page.click_hide_button()

@then(u'formuläret för att lägga till spelare inte visas')
def step_then_form_is_not_visible(context):
    label, input_text = context.start_page.get_form_elements()

    expect(label).not_to_be_visible(timeout=1000)
    expect(input_text).not_to_be_visible(timeout=1000)

@then(u'knappen "Lägg till spelare" är synlig')
def step_given_add_button_is_visible(context):
    expect(context.start_page.get_add_button()).to_be_visible(timeout=1000)
