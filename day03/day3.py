import sys
from typing import List

def parse_data() -> List[str]:
	data = [ ]

	with open('./day03/data.txt', 'r') as f:
		for n in f.readlines():
			data.append(n.strip())

	return data

def check_slope(data: List[str], horiz_move: int, vert_move: int) -> int:
	horiz_index = 0
	vert_index = 0
	num_trees = 0
	data_len = len(data[0])

	for geo in data:
		# Not sure this is the best way to skip rows in a list comprehension, couldn't find a better way with quick searches
		vert_index -= 1
		if vert_index > 0:
			continue
		else:
			vert_index = vert_move
		if geo[horiz_index % data_len] == '#':
			num_trees += 1
		horiz_index += horiz_move

	return num_trees

def main(args):
	data = parse_data()
	
	num_trees1 = check_slope(data, 1, 1)
	num_trees2 = check_slope(data, 3, 1)
	num_trees3 = check_slope(data, 5, 1)
	num_trees4 = check_slope(data, 7, 1)
	num_trees5 = check_slope(data, 1, 2)

	print("The number of trees for Right 3, Down 1 (Part 1) is: {0}".format(num_trees2))
	print("The number of trees encountered is: {0}, {1}, {2}, {3}, {4}".format(num_trees1, num_trees2, num_trees3, num_trees4, num_trees5))
	print("The product of all trees encounterd is: {0}".format(num_trees1 * num_trees2 * num_trees3 * num_trees4 * num_trees5))

if __name__ == '__main__':
    main(sys.argv)
    # main2(sys.argv)
