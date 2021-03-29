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
if __name__ == '__main__':
	solution = Solution()
	print(solution.twoSum([-1,-2,-3,-4,-5], -8))
