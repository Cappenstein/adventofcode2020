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


def find_seat(seat):
	minrow = 0
	maxrow = 127
	mincol = 0
	maxcol = 7

	for region in seat:
		if region == 'F':
			maxrow -= ceil((maxrow - minrow) / 2)
		elif region == 'B':
			minrow += ceil((maxrow - minrow) / 2)
		elif region == 'L':
			maxcol -= ceil((maxcol - mincol) / 2)
		elif region == 'R':
			mincol += ceil((maxcol - mincol) / 2)

	return maxrow * 8 + maxcol


def main2(args):
	data = parse_data('data.txt')

	all_seats = [False for i in range(1023)]
	first_occupied = False
	my_seat = 0

	for seat in data:
		seat_id = find_seat(seat)
		all_seats[seat_id] = True

	for seat_id, occupied in enumerate(all_seats, 0):
		if occupied is False:
			if first_occupied is True:
				print("My seat is {0}".format(seat_id))
				break
		else:
			first_occupied = True


def main(args, test: bool):
	if test:
		print("Seat id is {0}, should be: 357".format(find_seat('FBFBBFFRLR')))
		print("Seat id is {0}, should be: 567".format(find_seat('BFFFBBFRRR')))
		print("Seat id is {0}, should be: 119".format(find_seat('FFFBBBFRRR')))
		print("Seat id is {0}, should be: 820".format(find_seat('BBFFBBFRLL')))
		return

	data = parse_data('data.txt')
	max_seat = 0

	for seat in data:
		seat_id = find_seat(seat)
		if seat_id > max_seat:
			max_seat = seat_id

	print("The highest seat id is: {0}".format(max_seat))


if __name__ == '__main__':
	main(sys.argv, True)
	main(sys.argv, False)
	main2(sys.argv)
