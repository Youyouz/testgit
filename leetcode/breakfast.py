#小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，
#一维整型数组 drinks 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，
#且花费不超过 x 元。请返回小扣共有多少种购买方案。

#注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，
#请返回 1

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/2vYnGI

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        m, n = len(staple), len(drinks)
        nums, i, j = 0, 0, n - 1
        while i < m and j >= 0:
            if staple[i] + drinks[j] <= x: 
                nums += j + 1
                i += 1
            else:
                j -= 1
        return nums % 1000000007