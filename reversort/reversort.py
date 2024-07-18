import sys, os

if not os.environ.get('ONLINE_JUDGE'):
	sys.stdin = open('../input.txt', 'r')
	sys.stdout = open('../output.txt', 'w')


def reversort(n, nums):
	cost = 0
	for i in range(n-1):
		min_index = nums.index(min(nums[i: n]))
		nums[i:min_index+1] = nums[i:min_index+1][::-1]
		cost += min_index - i + 1
	return cost


for _ in range(int(input())):
	n = int(input())
	nums = list(map(int, input().split()))
	cost = reversort(n, nums)
	print(cost)