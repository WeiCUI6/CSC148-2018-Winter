"""
a test for calss RaceRegistry
"""

if __name__ == "__main__":
    from lab1 import RaceRegistry
    r1 = RaceRegistry()
    r1.add_member('gerhard@mail.utoronto.ca', 'under 40 minutes')
    r1.add_member('tom@mail.utoronto.ca', 'under 30 minutes')
    r1.add_member('toni@mail.utoronto.ca', 'under 20 minutes')
    r1.add_member('margot@mail.utoronto.ca', 'under 30 minutes')
    r1.add_member('gerhard@mail.utoronto.ca', 'under 30 minutes')
    result = r1.search_members('under 30 minutes')
    print(r1)
    print(result)
