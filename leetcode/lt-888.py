# encoding: utf-8
"""
    @Time   : 2021-02-01 14:12
    @Author : feikong
"""
from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a, sum_b = sum(A), sum(B)
        diff = (sum_a-sum_b) // 2
        ans = None
        set_a = set(A)
        for y in B:
            x = y + diff
            if x in set_a:
                ans = [x, y]
                break
        return ans


if __name__ == '__main__':
    print(Solution().fairCandySwap([1,1], [2,2]))
