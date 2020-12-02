import sys
from typing import List, Tuple

def parse_data() -> List[Tuple[int, int, str, str]]:
	data = [ ]

	with open('data.txt', 'r') as f:
		for n in f.readlines():
			reqs, passwd = n.strip().split(":", 1)
			count, char = reqs.split(" ")
			minr, maxr = count.split("-")
			data.append((int(minr), int(maxr), char, passwd.strip()))

	return data

def main2(args):
	data = parse_data()
	correct_password = 0

	for pos1, pos2, char, passwd in data:
		char1 = passwd[pos1 - 1]
		char2 = passwd[pos2 - 1]
		if char1 != char2 and (char1 == char or char2 == char):
			correct_password += 1


	print("Num OK: {0}".format(correct_password))

def main(args):
	data = parse_data()
	correct_password = 0
				
	for minr, maxr, char, passwd in data:
		cur_count = 0
		passwd_good = True

		for c in passwd:
			if c == char:
				cur_count += 1
			if cur_count > maxr:
				passwd_good = False
				break
		
		if cur_count < minr:
			passwd_good = False
		
		if passwd_good == True:
			correct_password += 1

	print("Num OK: {0}".format(correct_password))

if __name__ == '__main__':
    main(sys.argv)
    main2(sys.argv)
