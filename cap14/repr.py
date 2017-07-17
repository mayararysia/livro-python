class DataTable:
	def __init__(self, name):
		self._name = name

	def __repr__(self):
		return "Tabela {}".format(self._name)

table = DataTable("ExecucaoFinanceira")
print(table)

print(str(table))
