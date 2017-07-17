class DataTable:
	def __init__(self, name, filename):
		self._name = name
		with open(filename) as data:
			self._data = data.readlines()
	@property
	def name(self):
		return self._name

	def __len__(self):
		return len(self._data)

table = DataTable("ExecucaoFinanceira", "data/data/ExecucaoFinanceira.csv")

print(len(table))
