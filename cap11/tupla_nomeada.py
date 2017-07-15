from collections import namedtuple


def main():

	ExecucaoFianceira = namedtuple('ExecucaoFianceira',
					['IdExecucaoFinanceira', 						'IdEmpreendimento', 
					'IdInstituicaoContratado',
					'IdPessoaFisicaContratado',
					'IdLicitacao',
					'ValContrato',
					'ValTotal',
					'DatAssinatura',
					'DatInicioVigencia',
					'DatFinalVigencia'])


	execucao = ExecucaoFianceira(
		'1',
		'2',
		'132',
		'-1',
		'76',
		'100',
		'0',
		'19/03/2010',
		'23/03/2010',
		'05/10/2013')

	print(execucao.ValContrato)
	print(execucao)

if __name__ == "__main__":
	main()
