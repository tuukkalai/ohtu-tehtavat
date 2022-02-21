from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )

    # matcher = And(
        # HasFewerThan(1, "goals"),
        # PlaysIn("NYR")
    # )

    # Response
    # Tony DeAngelo        NYR          0  + 1  = 1
    # Tim Gettinger        NYR          0  + 0  = 0
    # Tarmo Reunanen       NYR          0  + 1  = 1
    # Zac Jones            NYR          0  + 4  = 4
    # Justin Richards      NYR          0  + 1  = 1
    # Keith Kinkaid        NYR          0  + 0  = 0
    # Igor Shesterkin      NYR          0  + 0  = 0
    # Alexandar Georgiev   NYR          0  + 0  = 0

    # matcher = And(
        # HasAtLeast(5, "goals"),
        # HasAtLeast(5, "assists"),
        # PlaysIn("PHI")
    # )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
