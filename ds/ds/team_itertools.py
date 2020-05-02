from itertools import permutations, combinations


def friends_teams(friends_teams=[], team_size=2, order_does_matter=False):
    if order_does_matter:
        return permutations(friends_teams, team_size)
    else:
        return combinations(friends_teams, team_size)
