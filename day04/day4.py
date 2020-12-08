import re
import sys
from typing import List


class Passport:
	valid = False
	byr = None
	iyr = None
	eyr = None
	hgt = None
	hcl = None
	ecl = None
	pid = None
	cid = None

	def __init__(self):
		valid = False

	def isValid(self):
		return self.byr is not None and self.iyr is not None and self.eyr is not None and self.hgt is not None and \
			self.hcl is not None and self.ecl is not None and self.pid is not None


def parse_data(filename) -> List[object]:
	data = []
	passport = {}

	with open('./day04/' + filename, 'r') as f:
		for n in f.readlines():
			n = n.strip()
			if len(n) == 0:
				data.append(passport)
				passport = {}
				continue
			key_vals = n.split(' ')
			for kv in key_vals:
				key, value = kv.split(':', 2)
				passport[key] = value

	if len(passport):
		data.append(passport)

	return data


def is_valid2(passport):
	# Make sure we have all the keys
	if is_valid(passport) is False:
		return False

	byr = int(passport['byr'])
	if byr < 1920 or byr > 2002:
		return False

	iyr = int(passport['iyr'])
	if iyr < 2010 or iyr > 2020:
		return False

	eyr = int(passport['eyr'])
	if eyr < 2020 or eyr > 2030:
		return False

	hgt = passport['hgt']
	hgt_re = re.compile('(\\d+)(cm|in)')
	match = hgt_re.match(hgt)
	if match is None:
		return False
	units = match.group(2)
	height = int(match.group(1))
	if units == 'cm' and (height < 150 or height > 193):
		return False
	elif units == 'in' and (height < 59 or height > 76):
		return False

	hcl = passport['hcl']
	hcl_re = re.compile('#[0-9a-f]{6}')
	if hcl_re.match(hcl) is None:
		return False

	if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return False

	pid_re = re.compile('\\d{9}')
	if len(passport['pid']) != 9 or pid_re.match(passport['pid']) is None:
		return False

	return True


"""
Validation rules
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
	If cm, the number must be at least 150 and at most 193.
	If in, the number must be at least 59 and at most 76.

hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
"""


def is_valid(passport):
	if 'byr' in passport and \
		'iyr' in passport and \
		'eyr' in passport and \
		'hgt' in passport and \
		'hcl' in passport and \
		'ecl' in passport and \
		'pid' in passport:
		return True

	return False


def main2_test(args):
	data = parse_data('datatest_valid.txt')
	valid_passport = 0

	for p in data:
		if is_valid2(p):
			valid_passport += 1

	print("The number of valid passports is: {0} (should be 4)".format(valid_passport))

	data = parse_data('datatest_invalid.txt')
	valid_passport = 0

	for p in data:
		if is_valid2(p):
			valid_passport += 1

	print("The number of invalid passports is: {0} (should be 0)".format(valid_passport))


def main2(args, test: bool):
	if test:
		main2_test(args)
		return

	data = parse_data('data.txt')
	valid_passport = 0

	for p in data:
		if is_valid2(p):
			valid_passport += 1

	print("The number of valid passports is: {0}".format(valid_passport))


def main(args, test: bool):
	data = parse_data('datatest.txt' if test else 'data.txt')
	valid_passport = 0

	for p in data:
		if is_valid(p):
			valid_passport += 1

	print("The number of valid passports is: {0}".format(valid_passport))


if __name__ == '__main__':
	main(sys.argv, True)
	main(sys.argv, False)
	main2(sys.argv, True)
	main2(sys.argv, False)
6