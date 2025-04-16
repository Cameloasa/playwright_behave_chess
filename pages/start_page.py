import re

class StartPage:
    def __init__(self, page):
        self.page = page

    def add_player(self):
        """Click the add player button."""
        self.page.get_by_role("button").get_by_text("Lägg till spelare").click()

    def fill_player_name(self, name):
        """Fill the player name in the input field."""
        self.page.get_by_role("textbox").fill(name)

    def is_add_button_visible(self):
        """Return the locator for the add player button."""
        return self.page.get_by_role("button").get_by_text("Lägg till spelare")


    def get_player(self, name):
        """Return the locator for a player with the given name and timer."""
        pattern = re.compile(name + r"\s+0:00\.0")
        return self.page.locator(".player").get_by_text(pattern)

    def get_players(self):
        """Return the locator for all player elements."""
        return self.page.locator(".player")