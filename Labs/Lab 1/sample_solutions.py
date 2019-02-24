from typing import Any, Dict, List


class Registry:
    """A registry of runners in a 5K race.  Each runner is identified by
    their email address and is registered in a speed category.

    === Attributes ===
    groups - runners grouped by category
    """
    groups: Dict[str, list]
    runners: Dict[str, str]

    # The names of the speed CATEGORIES for a race.
    CATEGORIES = ['<20', '<30', '<40', '>=40']

    def __init__(self) -> None:
        """ Initialize a new race registry with no runners entered.
        """
        self.groups = {}
        self.runners = {}
        for c in Registry.CATEGORIES:
            self.groups[c] = []

    def __eq__(self, other: Any) -> bool:
        """
        Return whether Registry self has same value as other.
        """
        if type(self) != type(other):
            return False
        for c in Registry.CATEGORIES:
            if self.groups[c] != other.groups[c]:
                return False
        # note that runners contains the same information
        # as groups, so we don't have to explicitly compare.
        return True

    def register(self, email: str, category: str) -> None:
        """ Register runner with email andd category.
        """
        # remove the runner from all categories they are
        # currently in.
        for c in Registry.CATEGORIES:
            if email in self.groups[c]:
                self.groups[c].remove(email)
        self.groups[category].append(email)
        self.groups[category].sort()
        self.runners[email] = category

    def get_runner_category(self, email: str) -> str:
        """ Return what speed category a given runner is in.
        """
        return self.runners[email]

    def get_runners_in_category(self, category: str) -> List[str]:
        return self.groups[category]
