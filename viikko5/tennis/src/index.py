from tennis_game import TennisGame


def main():
    game = TennisGame("player1", "player2")

    print(game.get_score()) # Love-All

    game.won_point("player1")
    print(game.get_score()) # Fifteen-Love

    game.won_point("player1")
    print(game.get_score()) # Thirty-Love

    game.won_point("player2")
    print(game.get_score()) # Thirty-Fifteen


    game.won_point("player2")
    print(game.get_score()) # Thirty-All
    game.won_point("player1")
    print(game.get_score()) # Forty-Thirty
    game.won_point("player2")
    print(game.get_score()) # Forty-All

    game.won_point("player1")
    print(game.get_score()) # Advantage player1
    game.won_point("player2")
    print(game.get_score()) # Deuce
    game.won_point("player2")
    print(game.get_score()) # Advantage player2

    game.won_point("player2")
    print(game.get_score()) # Win for player2


if __name__ == "__main__":
    main()
