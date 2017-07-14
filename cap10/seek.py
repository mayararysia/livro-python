# -*- coding: utf-8 -*-

def main():
	
	data = open('data/data/ExecucaoFinanceira.csv', 'r')

	print(data.read(5))
	print(data.read(5))
	print(data.read(5))
	print(data.read(5))
	print(data.seek(0))
	print(data.read(20))
if __name__ == "__main__":
	main()


