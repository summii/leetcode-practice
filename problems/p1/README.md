#Approach1

First i tried to divide the original array into zeroes and non-zeroes array. return the sum of both

#Approach2

I asked claude to write a solution for the same. It came with basic solution, add no-zeroes to new array and count number of zeroes then extend the result to count_zeroes

#Approach3

It was more diffcult for me to come up. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array. 

```code
class Solution:
    def moveZeroes(self, nums):
        # slow pointer keeps track of position for next non-zero element
        slow = 0
        
        # fast pointer finds non-zero elements
        for fast in range(len(nums)):
            # When we find a non-zero element
            if nums[fast] != 0:
                # Place it at the slow pointer position
                nums[slow] = nums[fast]
                slow += 1
        
        # Fill remaining positions with zeros
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
            
        return nums

```