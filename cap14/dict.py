class DataTable:
	def __init__(self, name, data=[]):
		self._name = name
		self._data = data

def add_row(self, row):
	self._data.append(row)

t = DataTable('ExecucaoFinanceira')

#dicionário normal
print(t.__dict__)

print(DataTable.__dict__.keys())
