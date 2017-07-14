# -*- coding: utf-8 -*-

def main():

	#fecha arquivos automaticamente
	with open('data/data/ExecucaoFinanceira.csv', 'r') as data:
		#content = data.read()
			#print(content)
		for line in data:
			print(line.split(';')[5])

if __name__ == "__main__":
	main()


