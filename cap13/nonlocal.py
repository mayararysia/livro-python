def make_counter(count):
	def counter():
		nonlocal count
		count += 1
		return count
	return counter

count = make_counter(0)

print(count())
print(count())
print(count())
