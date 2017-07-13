# -*- coding: utf-8 -*-

#Method Resolution Order (MRO)

class A:
	def run(self):
		return "A"

class B:
	def run(self):
		return "B"

class C(A, B):
	pass


def main():
	print(C.__mro__)
if __name__ == "__main__":
	main()
