import sys

def main2(args):
	data = [ ]
	with open('data.txt', 'r') as f:
		for n in f.readlines():
			data.append(int(n.strip()))
		
	num = len(data)

	for x in range(num):
		i = x + 1
		curNum = data[x]
		while i < num:
			secondNum = curNum + data[i]
			if curNum + data[i] < 2020:
				j = i + 1
				while j < num:
					if secondNum + data[j] == 2020:
						print("{0} * {1} * {2} = {3}".format(curNum, data[i], data[j], curNum * data[i] * data[j]))
						return
					j += 1
			i += 1



def main(args):
	data = [ ]
	with open('data.txt', 'r') as f:
		for n in f.readlines():
			data.append(int(n.strip()))
		
	num = len(data)

	for x in range(num):
		i = x + 1
		curNum = data[x]
		while i < num:
			if curNum + data[i] == 2020:
				print("{0} * {1} = {2}".format(curNum, data[i], curNum * data[i]))
				return
			i += 1

if __name__ == '__main__':
    main2(sys.argv)
