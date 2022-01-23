class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        # Sami Vatanen team CAR  goals 5 assists 18
        return f'{self.name} team {self.team} goals {self.goals} assists {self.assists}'
