import re


class StartPage:
    def __init__(self, page):
        self.page = page

    def add_player(self):
        """Click the add player action."""
        self.page.get_by_text("Lägg till spelare").click()

    def fill_player_name(self, name, player_index=0):
        """Fill the player name in the specified textbox (0 for first, 1 for second)."""
        self.page.get_by_role("textbox").nth(player_index).fill(name)

    def get_player(self, name):
        """Return the locator for a player with the given name and timer."""
        pattern = re.compile(r"(?i)" + re.escape(name) + r"\s+0:00[.,]0")
        return self.page.get_by_text(pattern)

    def has_error(self):
        """Check if an error message is present."""
        return self.page.get_by_text("Fyll i båda namnen")
