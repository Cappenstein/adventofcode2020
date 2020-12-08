import sys
from math import ceil, floor
from typing import List


def parse_data(filename) -> List[str]:
	data = []
	group = []

	with open('./day06/' + filename, 'r') as f:
		for n in f.readlines():
			n = n.strip()
			if len(n) == 0:
				data.append(group)
				group = []
				continue
			group.append(n)

	if len(group) > 0:
		data.append(group)

	return data


def main2(args, test: bool):
	data = parse_data('datatest.txt' if test else 'data.txt')

	total_answers = 0

	for group in data:
		response = [a for a in group[0]]
		for person in group:
			if len(response) == 0:
				break
			missing = [answer for answer in response if answer not in person]
			[response.remove(c) for c in missing]

		total_answers += len(response)

	print("The {0} is: {1}".format("total number of answers", total_answers))


def main(args, test: bool):
	data = parse_data('datatest.txt' if test else 'data.txt')

	total_answers = 0

	for group in data:
		response = []
		for person in group:
			[response.append(answer) for answer in person if answer not in response]

		total_answers += len(response)

	print("The {0} is: {1}".format("total number of answers", total_answers))


if __name__ == '__main__':
	main(sys.argv, True)
	main(sys.argv, False)
	main2(sys.argv, True)
	main2(sys.argv, False)
