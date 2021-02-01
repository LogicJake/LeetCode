#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#


# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mem = {}
        ans = -1
        for i, c in enumerate(s):
            if c not in mem:
                mem[c] = i
            else:
                ans = max(ans, i - mem[c] - 1)

        return ans


# @lc code=end
