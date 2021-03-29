#Code for question TwoSum in LeetCode

class Solution:
	def twoSum(self, nums, target):
		i = 0
		while i < len(nums):
			j = 0
			while j < len(nums):
				if i != j:
					if nums[i] + nums[j] == target:
						return [i, j]
				j += 1
			i += 1

	def twoSumOptimal(self, nums, target):
		compliments = {}
		for i, num in enumerate(nums):
			compliment = target - num
			if compliment in compliments:
				return [compliments[compliment], i]
			compliments[num] = i

if __name__ == '__main__':
	solution = Solution()
	print(solution.twoSumOptimal([3,2,4], 6))
