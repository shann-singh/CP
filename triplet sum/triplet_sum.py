import sys, os

if not os.environ.get('ONLINE_JUDGE'):
	sys.stdin = open('../input.txt', 'r')
	sys.stdout = open('../output.txt', 'w')


def triplet_sum(nums, target):
	res = []
	nums.sort()
	n = len(nums)
	for i in range(n-2):
		if i > 0 and nums[i-1] == nums[i]:
			continue
		j = i + 1
		k = n - 1
		while j < k:
			total = nums[i] + nums[j] + nums[k]
			if total == target:
				res.append([nums[i], nums[j], nums[k]])
				j += 1
				k -= 1
				while j < n and nums[j] == nums[j-1]:
					j += 1
				while k > 0 and nums[k] == nums[k+1]:
					k -= 1
			elif total < target:
				j += 1
			else:
				k -= 1
	return res



for _ in range(int(input())):
	nums = list(map(int, input().split()))
	target = int(input())
	res = triplet_sum(nums, target)
	print(res)