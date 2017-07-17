class DataTable:
	pass

t = DataTable()

setattr(t, 'name', 'ExecucaoFinanceira')

print(t.name)

#t.name é o mesmo que getattr. A diferença é que com getattr podemos passar uma string arbitrária
print(getattr(t, 'name'))
