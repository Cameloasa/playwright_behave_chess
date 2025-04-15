import os

from playwright.sync_api import sync_playwright

def before_all(context):
    print("DEBUG: Starting Playwright")
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    # Support for headless from environmental variable
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    slow_mo = int(os.getenv("SLOW_MO", "0"))
    print(f"DEBUG: Launching browser (headless={headless}, slow_mo={slow_mo})")
    context.browser = context.browser_type.launch(headless=headless, slow_mo=slow_mo)
    # set base_url
    context.base_url = "https://forverkliga.se/JavaScript/whose-turn/"

def before_scenario(context, scenario):
    print(f"DEBUG: Starting scenario '{scenario.name}'")
    context.page = context.browser.new_page()
    print(f"DEBUG: New page created, base_url={context.base_url}")
    # stabilize the page
    context.page.set_default_timeout(5000)  # 5s for all actions
    context.page.wait_for_load_state("domcontentloaded")

def after_scenario(context, scenario):
    if context.page:
        print(f"DEBUG: Closing page for scenario '{scenario.name}'")
        context.page.close()

def after_all(context):
    if context.browser:
        print("DEBUG: Closing browser")
        context.browser.close()
    if context.playwright:
        print("DEBUG: Stopping Playwright")
        context.playwright.stop()