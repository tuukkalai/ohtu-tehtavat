class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __gt__(self, other):
        return (self.goals + self.assists) > (other.goals + other.assists)

    def __str__(self):
        points = self.goals + self.assists
        goals = str(self.goals)
        assists = str(self.assists)
        return f'{self.name:21} {self.team:4}{goals:>2} + {assists:>2} = {points:>2}'
