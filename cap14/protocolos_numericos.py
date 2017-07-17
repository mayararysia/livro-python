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

class Select:
	def __init__(self):
		self._c = 0

	def __lshift__(self, table):
		self.table = table
		return self

	def __iter__(self):
		return self

	def __next__(self):
		try:
			element = self.table._data[self._c]
		except IndexError as ie:
			self._c = 0
			raise StopIteration
		self._c += 1
		return element

select = Select()

table = DataTable("ExecucaoFinanceira", "data/data/ExecucaoFinanceira.csv")

for line in select << table:
	print(line)
