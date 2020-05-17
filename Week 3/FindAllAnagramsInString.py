/*
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
*/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP = collections.Counter(p)
        currentCounter = collections.Counter(s[:len(p)])
        ans = []
        if countP == currentCounter: ans = [0]
        for i in range(len(p),len(s)):
            toberemoved = currentCounter[s[i-len(p)]]
            if toberemoved == 1:
                del currentCounter[s[i-len(p)]]  
            else:
                currentCounter[s[i-len(p)]]  -= 1 
            currentCounter[s[i]] += 1
            if currentCounter == countP:
                ans.append(i-len(p)+1)
        return ans
