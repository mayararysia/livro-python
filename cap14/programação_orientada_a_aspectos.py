class Proxy:
	def __init__(self, obj):
		self.obj = obj


	def __getattr__(self, name):
		print("Acesso ao atributo {}".format(name))
		if hasattr(self.obj, name):
			return getattr(self.obj, name)
		else:
			raise Exception("Atributo desconhecido")

class DataTable:
	def __init__(self, name):
		self.name = name

class Query:
	def __init__(self, attributes):
		self.attributes = attributes


table_proxy = Proxy(DataTable('ExecucaoFinanceira'))
query_proxy = Proxy(Query(['id', 'valor']))
table_proxy.__dict__

query_proxy.__dict__

print(table_proxy.name)

print(query_proxy.attributes)
