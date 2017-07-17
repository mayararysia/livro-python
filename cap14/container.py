class TenhoTudo:

	def __contains__(self, obj):
		return True

tem_tudo = TenhoTudo()

print(1 in tem_tudo)

print("qualquercoisa" in tem_tudo)

print([] in tem_tudo)

