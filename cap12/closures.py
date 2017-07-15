# coding: utf-8

def greater(fixed_val):
	def _greater(val):
		return val > fixed_val
	return _greater

def main():

	greater_100K = greater(100000)
	print(greater_100K(99999))
	print(greater_100K(99999 + 2))

if __name__ == "__main__":
	main()
