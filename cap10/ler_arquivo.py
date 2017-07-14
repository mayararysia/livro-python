# -*- coding: utf-8 -*-

def main():
	
	data = open('data/data/ExecucaoFinanceira.csv', 'r')
	#especifica a quantidade de bytes a ser lida
	#print(data.read(19))
	for line in data:
		print(line)
	data.close()

if __name__ == "__main__":
	main()


