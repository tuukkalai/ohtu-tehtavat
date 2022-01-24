from player_reader import PlayerReader


class PlayerStats:
	def __init__(self, reader: PlayerReader) -> None:
		self.reader = reader
		self.players = self.reader.get_players()

	def top_scorers_by_nationality(self, nationality: str) -> list:
		return list(filter(lambda x : x.nationality == nationality, self.players))
