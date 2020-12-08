import sys
from math import ceil, floor
from typing import List


def parse_data(filename) -> List[str]:
	data = []

	with open('./day05/' + filename, 'r') as f:
		for n in f.readlines():
			n = n.strip()
			data.append(n)

	return data


def main2(args, test: bool):
	data = parse_data('datatest.txt' if test else 'data.txt')

	print("The {0} is: {1}".format("answer", "0"))


def main(args, test: bool):
	data = parse_data('datatest.txt' if test else 'data.txt')

	print("The {0} is: {1}".format("answer", "0"))


if __name__ == '__main__':
	main(sys.argv, True)
	# main(sys.argv, False)
	# main2(sys.argv, True)
	# main2(sys.argv, False)
