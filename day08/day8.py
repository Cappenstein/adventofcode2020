import sys
from math import ceil, floor
from typing import List


def parse_data(filename) -> List[str]:
	data = []

	with open('./day08/' + filename, 'r') as f:
		for n in f.readlines():
			n = n.strip()
			op, count = n.split(' ', 1)
			data.append({
				'op': op,
				'sign': count[0],
				'count': int(count[1:])
			})

	return data


def perform_instruction(instruction, idx):
	acc = 0
	if instruction['op'] == 'jmp':
		if instruction['sign'] == '+':
			return idx + instruction['count'], acc
		else:
			return idx - instruction['count'], acc

	if instruction['op'] == 'acc':
		acc = instruction['count']
		if instruction['sign'] == '-':
			acc *= -1

	return idx + 1, acc


def run_program(data, visited, modified, idx, acc):
	while idx < len(visited) and visited[idx] is False:
		visited[idx] = True

		# If we haven't modified an instruction yet
		if modified is False and data[idx]['op'] in ('jmp', 'nop'):
			instruction = {
				'count': data[idx]['count'],
				'sign': data[idx]['sign'],
				'op': 'jmp' if data[idx]['op'] == 'nop' else 'nop'
			}
			# Perform the modified instruction
			new_idx, add_acc = perform_instruction(instruction, idx)

			# And run the program from here
			ret = run_program(data, visited.copy(), True, new_idx, acc)
			if ret > 0:  # We found the right path, return up the tree
				return ret

		# We either need to not modify the instruction, or the modifying the instruction failed
		# so perform the instruction normally
		idx, add_acc = perform_instruction(data[idx], idx)
		acc += add_acc

	if idx == len(visited):
		return acc  # We found the correct modification
	else:
		return 0


def main2(args, test: bool):
	data = parse_data('datatest.txt' if test else 'data.txt')
	visited = [False for i in range(len(data))]

	acc = run_program(data, visited, False, 0, 0)

	print("The {0} is: {1}".format("final accumulator", acc))


def main(args, test: bool):
	data = parse_data('datatest.txt' if test else 'data.txt')

	idx = 0
	acc = 0
	visited = [False for i in range(len(data))]
	while visited[idx] is False:
		visited[idx] = True
		idx, add_acc = perform_instruction(data[idx], idx)
		acc += add_acc

	print("The {0} is: {1}".format("final accumulator", acc))


if __name__ == '__main__':
	main(sys.argv, True)
	main(sys.argv, False)
	main2(sys.argv, True)
	main2(sys.argv, False)
