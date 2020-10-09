#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return len(set(s))
        n, res = len(s), 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                l = len(set(s[i:j]))
                if l == j - i:
                    res = max(res, l)
        return res

# @lc code=end

a = Solution()
print(a.lengthOfLongestSubstring("pwwkew"))
