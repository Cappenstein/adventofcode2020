import re
import sys


def parse_data(filename):
	data = {}

	with open('./day07/' + filename, 'r') as f:
		for n in f.readlines():
			n = n.strip('.\n')
			bag, contains = n.split(' bags contain ')
			if contains == 'no other bags':
				data[bag] = []
			else:
				data[bag] = [re.sub('( bags| bag)', '', i).split(' ', 1) for i in contains.split(', ')]

	return data


def count_sub_bags(all_bags, current_bag):
	total_bags = 0
	for bag in all_bags[current_bag]:
		total_bags += int(bag[0])
		total_bags += int(bag[0]) * count_sub_bags(all_bags, bag[1])

	return total_bags


def main2(args, test: bool):
	data = parse_data('datatest2.txt' if test else 'data.txt')

	bag_to_start = 'shiny gold'

	total_bags = count_sub_bags(data, bag_to_start)

	print("The {0} is: {1}".format("number of bags", total_bags))


def find_my_bag(find_bag, all_bags, current_bag):
	if find_bag == current_bag:
		return 1

	found_bags = 0
	for bag in all_bags[current_bag]:
		found = find_my_bag(find_bag, all_bags, bag[1])
		if found:
			found_bags += found
			break  # If any path is true, then it's true, don't double count

	return found_bags


def main(args, test: bool):
	data = parse_data('datatest.txt' if test else 'data.txt')

	found_bags = 0
	bag_to_find = 'shiny gold'
	for bag in data:
		if bag != bag_to_find:
			found_bags += find_my_bag(bag_to_find, data, bag)

	print("The number of bags is: {0}".format(found_bags))


if __name__ == '__main__':
	main(sys.argv, True)
	main(sys.argv, False)
	main2(sys.argv, True)
	main2(sys.argv, False)
