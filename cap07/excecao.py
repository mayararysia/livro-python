# -*- coding: utf-8 -*-

import zipfile

banco_zip = None

try:
	banco_zip = zipfile.ZipFile("saida.zip")
	banco_zip.extractall(path="banco")
except PermissionError:
	print("Algum problema ao ler o arquivo")
finally:
	#banco_zip.extractall(path="banco")
	banco_zip.close()