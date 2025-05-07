# Input: [100, 4, 200, 1, 3, 2]
# Output: 4

def func2(nums):
    nums = set(nums)
    ml = 0
    for i in nums:
        if i - 1 not in nums:
            c = i
            l = 1
            while c + 1 in nums:
                c += 1
                l += 1
            ml = max(ml, l)
    return ml

print(func2([100, 4, 200, 1, 3, 2]))
