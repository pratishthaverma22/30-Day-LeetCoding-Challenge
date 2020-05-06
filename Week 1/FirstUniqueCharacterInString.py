/*
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
*/


from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ctr = Counter(s)
        for i in range(len(s)):
            if ctr[s[i]] == 1:
                return i
            
        return -1        
