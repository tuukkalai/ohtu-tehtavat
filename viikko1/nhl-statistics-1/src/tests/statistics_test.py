import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_correct_player(self):
        self.assertEqual(str(self.statistics.search("Gretzky")), "Gretzky EDM 35 + 89 = 124")

    def test_search_returns_none_if_not_found(self):
        self.assertIsNone(self.statistics.search("Mäntylä"))

    def test_team_returns_players_of_a_team(self):
        self.assertEqual(str(self.statistics.team("PIT")[0]), str(Player("Lemieux", "PIT", 45, 54)))

    def test_team_returns_empty_list_if_illegal_team(self):
        self.assertEqual(self.statistics.team("HIFK"), [])

    def test_top_scorers_returns_right_players(self):
        top_scorers = []
        top_scorers.append(Player("Gretzky", "EDM", 35, 89))
        top_scorers.append(Player("Lemieux", "PIT", 45, 54))
        self.assertEqual(str(self.statistics.top_scorers(2)[0]), str(top_scorers[0]))
        self.assertEqual(str(self.statistics.top_scorers(2)[1]), str(top_scorers[1]))

