class Column:
	def __init__(self, name, kind, description=""):
		print(type(self))


class PrimaryKey(Column):
	def __init__(self, table, name, kind, description=""):
		Column.__init__(self, name, kind, description=description)
		self._is_pk = True

	def get_name(self):
		return self._name

pk = PrimaryKey(None, 'PK', 'int')

