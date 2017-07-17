class TesteLT:
	def __init__(self, n):
		self.n = n

def __lt__(self, other):
	return self.n < other.n

print(TesteLT(3) < TesteLT(4))
print(TesteLT(4) < TesteLT(3))

