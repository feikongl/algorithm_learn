# encoding: utf-8
"""
    @Time   : 2021-02-02 17:06
    @Author : feikong
"""
from typing import List


class Solution:
    """
    给定一个排序数组，
    你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        i = 1
        while True:
            if nums[i+1] == nums[i]:
                nums.pop(i)
                i = -1
            i += 1
            if i > len(nums)-2:
                break
        return len(nums)

    def removeDuplicates02(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        res = 1
        flag = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[flag] = nums[i + 1]
                flag += 1
                res += 1
        print(nums)
        return res


if __name__ == '__main__':
    nums = [0,0,1,1,2,2]

    print(Solution().removeDuplicates02(nums))
