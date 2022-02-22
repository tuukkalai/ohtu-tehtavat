from matchers import All, And, HasAtLeast, HasFewerThan, Or, PlaysIn


class QueryBuilder:
	def __init__(self, queries = All()) -> None:
		self.queries = queries

	def build(self):
		return self.queries

	def playsIn(self, team):
		return QueryBuilder(And(PlaysIn(team), self.queries))

	def hasAtLeast(self, value, attr):
		return QueryBuilder(And(HasAtLeast(value, attr), self.queries))

	def hasFewerThan(self, value, attr):
		return QueryBuilder(And(HasFewerThan(value, attr), self.queries))

	def oneOf(self, query_1, query_2):
		return QueryBuilder(Or(query_1, query_2))
