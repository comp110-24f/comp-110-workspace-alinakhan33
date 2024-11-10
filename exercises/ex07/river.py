"""File to define River class."""

from ex07.fish import Fish
from ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove fish and bears from the river based on their age."""
        # Filter out fish older than 3
        surviving_fish = [fish for fish in self.fish if fish.age <= 3]
        # Filter out bears older than 5
        surviving_bears = [bear for bear in self.bears if bear.age <= 5]

        # Update the fish and bear lists with only the surviving animals
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        """if there are at least 5 fish in the river, the bear eats 3 fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                # Remove 3 fish from the river
                self.remove_fish(3)
                # Bear eats 3 fish
                bear.eat(3)
        return None

    def check_hunger(self):
        """Remove bears from the river if their hunger_score < 0"""
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:  # keep bears with a hunger_score of 0 or higher
                surviving_bears.append(bear)
        # surviving bears
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Each pair of fish produces 4 offspring"""
        num_new_fish = (len(self.fish) // 2) * 4  # Each pair produces 4 new fish
        for _ in range(num_new_fish):
            self.fish.append(Fish())  # Add a new fish to the river
        return None

    def repopulate_bears(self):
        """Add new bears to the river. Each produces one"""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())  # Add a new bear to the river
        return None

    def view_river(self):
        """Print the current state of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """all one_river_day seven times."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Remove a specified number of Fish from the front of the fish list."""
        # Ensure that the amount to remove does not exceed the current number of fish
        if amount > len(self.fish):
            amount = len(self.fish)  # avoid removing more fish than available

        # Remove the fish from the beginning of the list
        self.fish = self.fish[amount:]
