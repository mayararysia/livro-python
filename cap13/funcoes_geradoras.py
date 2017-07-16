def get_list():
	numbers = []
	for i in range(10):
		numbers.append(i)
	return numbers

for number in get_list():
	print(number)

#sempre que se usa yield, cria-se uma função geradora
def get_generator():
	for i in range(10):
		yield i
for number in get_generator():
	print(number)

def main():

	my_generator = get_generator()
	print(my_generator)
	print(next(my_generator))
	print(next(my_generator))
	print(next(my_generator))
	print(next(my_generator))
	print(next(my_generator))
	print(next(my_generator))
	print(next(my_generator))
	print(next(my_generator))
	print(next(my_generator))
	print(next(my_generator))
	print(next(my_generator))



if __name__ == "__main__":
	main()
