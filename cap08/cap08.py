from domain import Column
import unittest

class DataTable:
	def add_column(self, name, kind, description=""):
		self._validate_kind(kind)
		column = Column(name, kind, description=description)
		self._columns.append(column)
		return column

	def _validate_kind(self, kind):
		if not kind in ('bigint', 'numeric', 'varchar'):
			raise Exception("Tipo inválido")

class DataTableTest(unittest.TestCase):
	
	def setUp(self):
		self.table = DataTable('A')

	def test_add_column(self):
		self.assertEqual(0, len(self.table._columns))
		
		self.table.add_column('BId', 'bigint')
		self.assertEqual(1, len(self.table._columns))
		
		self.table.add_column('value', 'numeric')
		self.assertEqual(2, len(self.table._columns))
		
		self.table.add_column('desc', 'varchar')
		self.assertEqual(3, len(self.table._columns))
	
	def test_add_column_invalid_type(self):
		self.assertRaises(Exception,
			self.table.add_column, ('col', 'invalid'))
