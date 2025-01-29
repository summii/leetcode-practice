class Solution:
    def moveZeroes(self, nums):
        result = []
        zero_count = 0

        for num in nums:
            if num != 0:
                result.append(num)
            else:
                zero_count +=1
        result.extend([0]*zero_count)
        #replace the in-place list
        for i in range(len(nums)):
            nums[i] = result[i]
        return result


s = input()
arr = list(map(int, s.strip('[]').split(',')))
solution = Solution()
ret = solution.moveZeroes(arr)
print(ret)