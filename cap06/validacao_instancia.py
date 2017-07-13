# -*- coding: utf-8 -*-

from domain_instancia import *

def main():
	
	#Teste da função validate() no console:
	c1 = Column("IdEmpreendimento", "bigint")
	print(c1.validate(100))
	print(not c1.validate(10.1))
	print(not c1.validate("Texto"))

	c1 = Column("DescEmpreendimento", "varchar")
	print(c1.validate("Contrato"))
	print(not c1.validate(10.1))
	print(not c1.validate(10))

	c1 = Column("ValTotalPrevisto", "numeric")
	print(c1.validate(10.1))
	print(c1.validate(10))
	print(not c1.validate("Texto"))
if __name__ == "__main__":
	main()
