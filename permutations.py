

#backtracking implimentation for generating
#all possible permutations 

nums = [1,2,3]

def permute(nums):
    def backtracking(start: int):
        if start == len(nums):
            res.append(nums.copy())
            return
        for i in range(start, len(nums)):
            print("start is =>",start)
            nums[start], nums[i] = nums[i], nums[start]
            backtracking(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    res = []
    backtracking(0)
    return res


nums = [1,2,3]
res = permute(nums)
print(res)
