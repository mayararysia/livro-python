# -*- coding: utf-8 -*-
import io

def main():

	data = io.StringIO("a\nb\nc")
	lines = data.readlines()
	print(lines)
	data.close()
	print(data.closed)

if __name__ == "__main__":
	main()
