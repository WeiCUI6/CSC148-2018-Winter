"""
Read the name of subclass BookRoster below, and then add a str
method, including a docstring, to subclass BookRoster. You do not need
examples in this docstring. Your str method should be used to display a list of
all items.

Assume BookRoster.add() takes a list in the form [book number, name,
genre] where book number is an int.

Context: an book-tracking system.
A library tracks books that are registered in it, each one having a name.
Books are identified by their book number, and they also have a name, such as
'CLRS', and a genre such as 'Educational'. We must be able to display a list of
books where each line of the list has the following format:
Book Number: <book number>, Name: <name>, Genre: <genre>
"""

class Roster:
    """
    Represents a roster of members.
    @param dict members: represents this rosterâ€™s members
    """
    def __init__(self) -> None:
        """
        Initialize new roster self.
        @param Roster self: this Roster
        @rtype: None
        """
        self.members = {}

    def add(self, member: tuple) -> None:
        """
        Add member to roster self.
        @param Roster self: this Roster
        @param tuple member: member record to add
        @rtype: None
        Assume:
        -- member is a tuple with member[0] not in self.members,
        -- len(member) > 1
        """
        self.members[member[0]] = member[1:]

    def remove(self, member: tuple) -> None:
        """
        Remove member from roster self.
        @param Roster self: this Roster
        @param tuple member: member record to be removed
        @rtype: None
        Assume:
        --member is a tuple with member[0] in self.members
        --len(member) > 1
        """
        del(self.members[member[0]])

    def __str__(self) -> str:
        """
        Return a string representation of the members of roster self.
        @param Roster self: this Roster
        @rtype: str
        """
        raise NotImplementedError

class BookRoster(Roster):
    """
    Represents a roster of books.
    """

    def __str__(self) -> str:
        """
        Return a string representation of the members of BookRoster self.

        @param BookRoster self: this BookRoster
        @rtype str
        """
        ret_str = ""
        for number in self.members:
            (name, genre) = self.members[number]
            ret_str += ("Book Number: {}, Name: {}, " +
                        "Genre: {}\n").format(str(number), name, genre)

        return ret_str[:-1] # Remove the last newline
