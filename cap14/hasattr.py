class DataTable:
	def __init__(self, name, data=[]):

		self.name = name

		self._data = data

	def add_row(self, row):

		self._data.append(row)

t = DataTable('ExecucaoFinanceira')

print(hasattr(t, 'name'))

print(hasattr(t, '_data'))

