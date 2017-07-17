class DataTable:

	def __init__(self, name):
		self._name = name

	def __getattr__(self, attr_name):
		print("Attributo não definido '{}' acessado".format(
		attr_name))

		if attr_name == "data":
			return []

		raise AttributeError("Atributo '{}' não existe".format(attr_name))

def __getattribute__(self, attr_name):
	print("Attributo {} acessado".format(attr_name))
	return object.__getattribute__(self, attr_name)

t = DataTable("ExecucaoFinanceira")

print(t._name)

print(t.data)

print(t.cols)
