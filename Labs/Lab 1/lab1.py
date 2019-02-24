# == Race Registry ==
#
# Context: a system for organizing a 5K running race.
#
# When runners register, they provide their email address
# and their speed category.  A speed category indicates how quickly they
# estimate that they can finish the race.  This allows organizers to start
# the runners in groups of roughly equivalent running speed so that
# faster runners aren't stuck behind slower runners.  The possible speed
# categories are: under 20 minutes, under 30 minutes, under 40 minutes,
# and 40 minutes or over.  We need to be able get a list of runners' emails in
# a given speed category.  We also need to be able to look up a runner by email
# to find their speed category.
#
# Design and implement a class for a race registry.

from typing import Any


class RaceRegistry:
    """
    a system for organizing a 5K running race
    """
    content: dict

    def __init__(self) -> None:
        self.content = {}

    def __eq__(self, other: Any) -> bool:
        return type(self) == type(other) and self.content == other.content

    def __str__(self) -> str:
        result = ''
        for key in self.content:
            result = result + key + ':'
            for member in self.content[key]:
                result = result + member + ' '

        return result

    def add_member(self, name: str, speed: str) -> None:
        """
        when a person registries for the race, we add him into the system
        """
        if speed not in self.content:
            self.content[speed] = []
            self.content[speed].append(name)
        else:
            self.content[speed].append(name)

    def search_members(self, speed: str) -> list:
        """
        we want to get a list of runner's eamil address in a given speed
        category
        """
        if speed in self.content:
            return self.content[speed]
        else:
            return []
