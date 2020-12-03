import sys

def main2(args):
	data = [ ]
	with open('data.txt', 'r') as f:
		for n in f.readlines():
			data.append(int(n.strip()))
		
	for i, first in enumerate(data):
		for j, second in enumerate(data[i+1:]):
			if first + second < 2020:
				for third in data[j+1:]:
					if first + second + third == 2020:
						print("{0} * {1} * {2} = {3}".format(first, second, third, first * second * third))
						return

def main(args):
	data = [ ]
	with open('data.txt', 'r') as f:
		for n in f.readlines():
			data.append(int(n.strip()))
		
	for i, first in enumerate(data):
		for second in data[i+1:]:
			if first + second == 2020:
				print("{0} * {1} = {2}".format(first, second, first * second))
				return

if __name__ == '__main__':
    main2(sys.argv)
