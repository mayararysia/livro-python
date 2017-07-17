class DataTable:
	def __init__(self, name, data=[]):
		self._name = name
		self._data = data


t = DataTable('ExecucaoFinanceira')
print(t._data)
t = DataTable('ExecucaoFinanceira', data=['linha1', 'linha2'])
print(t._data)
print(t._name)

