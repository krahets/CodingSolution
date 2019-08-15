class Solution:
    def singleNumber(self, nums: [int]) -> int:
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num # ones & num 提取两个数都为1的位，与twos作或操作保留出现2次的位
            ones ^= num  # 当 ones 和 num 同时为 1 or 0 时，ones = 0，因为同时为1已经加到twos里了，这里不做count
            threes = ones & twos # 当 ones 和 twos 都为1时，说明到出现了3次
            ones &= ~threes # three 为1时将one和two归零
            twos &= ~threes
        return ones


class Solution:
    def singleNumber(self, nums: [int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
        
s = Solution()
print(s.singleNumber([2,2,3,2]))