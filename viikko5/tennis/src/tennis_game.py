class TennisGame:
    """TennisGame class for simulating tennis match scores.

    Returns:
        str: score
    """
    points = {0: 'Love', 1: 'Fifteen', 2: 'Thirty', 3: 'Forty'}

    def __init__(self, player1_name, player2_name):
        """Initializing TennisGame class with two players.

        Args:
            player1_name (str): Name of the player 1
            player2_name (str): Name of the player 2
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        """Adding score to player who won the ball.

        Args:
            player_name (str): Name of the player who won the ball
        """
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        """Get current scoring status of the game.

        Returns:
            str: Status of the game verbally
        """
        if self.player1_score == self.player2_score:
            return self.players_tied()
        elif self.player1_score >= len(self.points) or self.player2_score >= len(self.points):
            return self.later_stage()
        return f'{self.points[self.player1_score]}-{self.points[self.player2_score]}'

    def players_tied(self):
        """Status when players have equal amount of points.

        Returns:
            str: Status of the game when tied
        """
        if self.player1_score < 4:
            return self.points[self.player1_score] + "-All"
        return "Deuce"

    def score_difference(self):
        """Difference in players' scores.

        Returns:
            int: Difference in players' scores
        """
        return self.player1_score - self. player2_score

    def later_stage(self):
        """Status when players have more than 4 points each.

        Returns:
            str: Status of the game
        """
        difference = self.score_difference()

        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        return "Win for player2"
