# -*- coding: utf-8 -*-

from cap09_domain import *

def main():
	
	table = DataTable("Empreendimento")
	col = Column("IdEmpreendimento", 'bigint')
	print(table)
if __name__ == "__main__":
	main()

