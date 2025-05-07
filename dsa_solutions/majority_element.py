# Input: [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]


arr = [2,2,1,1,1,2,2]
print(majorityElement(arr))