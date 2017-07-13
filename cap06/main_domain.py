# -*- coding: utf-8 -*-

from domain import *

#cap 6.11
class DuckType:
	pass

def print_name(table):
	print(table.name)
	
def main():	
	table_empreedimento = DataTable("Empreendimento")

	table = DataTable("Empreendimento")
	
	#cap 6.11 DuckType
	duck = DuckType()
	duck.name = "quack"
	
	print_name(table)
	print_name(duck)
	
	#cap 6.9
	print(table.name)
	table.name='Alerta'
	del table.name
	
	print(Column('IdEmpreendimento', 'bigint'))
	print(PrimaryKey(table, 'IdEmpreendimento', 'bigint'))

	col_id = table_empreedimento.add_column('IdEmpreendimento', 'bigint')
	
	col_aditivo = table_empreedimento.add_column('IdAditivo','bigint')

	col_alerta = table_empreedimento.add_column('IdAlerta','bigint')

	table_aditivo = DataTable("Aditivo")

	col_id = table_aditivo.add_column('IdAditivo', 'bigint')
	
	col_emp_id = table_empreedimento.add_column('IdEmpreendimento', 'bigint')

	table_empreedimento.add_references("IdAditivo", table_aditivo, col_aditivo)

	table_aditivo.add_referenced("IdEmpreendimento", table_empreedimento, col_emp_id)
	
	#Teste da função validate() no console:
	#c1 = Column("IdEmpreendimento", "bigint")
	#c1.validate(100)

	#print("%s" not c1.validate(10.1))
	#print("%s" not c1.validate("Texto"))

	#c1 = Column("DescEmpreendimento", "varchar")
	#print("%s" c1.validate("Contrato"))
	#print("%s" not c1.validate(10.1))
	#print("%s" not c1.validate(10))

	#c1 = Column("ValTotalPrevisto", "numeric")
	#print("%s" c1.validate(10.1))
	#print("%s" c1.validate(10))
	#print("%s" not c1.validate("Texto"))
	print("Finished")
if __name__ == "__main__":
	main()
