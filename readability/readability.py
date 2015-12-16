import sys

from pyreadability.readability import Readability

if __name__ == '__main__':
	f = str(sys.argv)[1]
	r = Readability(f[0])
	print(r.result)
