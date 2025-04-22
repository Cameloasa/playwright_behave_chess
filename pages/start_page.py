import re
import time
from playwright.sync_api import expect

class StartPage:
    def __init__(self, page):
        self.page = page

    def add_player(self):
        """Click the add player button."""
        self.page.get_by_role("button").get_by_text("Lägg till spelare").click()

    def fill_player_name(self, name):
        """Fill the player name in the input field."""
        self.page.get_by_role("textbox").fill(name)

    def get_add_button(self):
        """Return the locator for the 'Lägg till spelare' button."""
        return self.page.get_by_role("button").get_by_text("Lägg till spelare")

    def get_player(self, name):
        """Return the locator for a player with the given name and timer."""
        pattern = re.compile(name + r"\s+0:00\.0")
        return self.page.locator(".player").get_by_text(pattern)

    def get_form_elements(self):
        """Return the label and input field for the add player form (those that toggle visibility)."""
        name_regex = re.compile("Nya spelarens namn", re.IGNORECASE)
        label = self.page.get_by_text(name_regex)
        input_text = self.page.get_by_role("textbox")
        return label, input_text

    def click_hide_button(self):
        """Click the hide form button."""
        self.page.get_by_role("button").get_by_text("Dölj").click()

    def get_players(self):
        """Return the locator for all player elements."""
        return self.page.locator(".player")

    def start_your_move(self):
        """Click the start your move button."""
        self.page.get_by_role("button").get_by_text("Börja ditt drag").click()

    def get_active_move_button(self):
        """Return the button used to start/hand over the move (its text changes)."""
        return self.page.get_by_role("button", name=re.compile(r"Börja ditt drag|Överlämna till .+"))

    def click_active_move_button(self, expected_text):
        """Click the button only if it matches the expected text."""
        button = self.get_active_move_button()
        expect(button).to_have_text(expected_text)
        button.click()

    def get_player_timer_element(self, name):
        """Return the <code> element (timer) for the player with the given name."""
        player_section = self.page.locator("section.large", has_text=name)
        return player_section.locator("code")

    def is_timer_running_for_player(self, name):
        """Return True if the timer for the given player is increasing."""
        timer_element = self.get_player_timer_element(name)
        initial_time = timer_element.inner_text()
        time.sleep(1.5)
        updated_time = timer_element.inner_text()
        return initial_time != updated_time

    def get_pause_button(self):
        """Return pause button"""
        self.page.get_by_role("button").get_by_text("Pausa").click()

    def is_game_paused(self):
        return self.page.locator(".game-paused").is_visible()

