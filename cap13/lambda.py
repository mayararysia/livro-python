# coding: utf-8

from decimal import Decimal

total = Decimal('0')
_100M = Decimal('100000000')

def dec(element, index):
	try:
		return Decimal(element[index])
	except:
		return Decimal('0')

with open('data/data/ExecucaoFinanceira.csv', 'r') as data:
	splited_data = [line.split(';') for line in data]
	values = [dec(element, 12) for element in splited_data]
	total = sum(values)
	values_100M = filter(lambda x: x > _100M, values)
	total_gt_100M = sum(values_100M)

percent = lambda x, y: (x/y) * Decimal('100')

print("Total gasto: {}".format(total))
print("Apenas contratos com mais de 100MI: {}".format(
total_gt_100M))
print("Representam {:.2f}% do total".format(percent(
total_gt_100M, total)))
