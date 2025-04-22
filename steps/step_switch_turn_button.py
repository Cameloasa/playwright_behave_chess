import re
from behave import when
from playwright.sync_api import expect

@when('spelaren klickar på knappen "Överlämna till {name}"')
def step_click_specific_button(context, name):
    button = context.start_page.get_active_move_button()
    expect(button).to_have_text(f"Överlämna till {name}", timeout=2000)
    button.click()