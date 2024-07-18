import sys, os

if not os.environ.get('ONLINE_JUDGE'):
	sys.stdin = open('../input.txt', 'r')
	sys.stdout = open('../output.txt', 'w')
