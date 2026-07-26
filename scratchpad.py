
from typing import List

def majorityElement(nums):
        candidate = None
        vote = 0
        for num in nums:
            if num == candidate:
                vote+= 1
            elif vote == 0:
                candidate = num
                vote = 1
            else:
                vote -= 1
        return candidate


print(majorityElement([1,1,1,2,2,2,2,3,3,3,3,3,1,1,1]))