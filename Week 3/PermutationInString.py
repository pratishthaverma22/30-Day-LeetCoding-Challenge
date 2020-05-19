/*
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

*/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # only contain lower case letters            
        s1_char_to_cnt = [0] * 26
        for c in s1:
            s1_char_to_cnt[ord(c) - ord("a")] += 1
            
        s2_char_to_cnt = [0] * 26
        for idx in range(len(s1)):
            s2_char_to_cnt[ord(s2[idx]) - ord("a")] += 1
            
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            if s1_char_to_cnt == s2_char_to_cnt:
                return True
            
            s2_char_to_cnt[ord(s2[left]) - ord("a")] -= 1
            left += 1
            right += 1
            if right < len(s2):
                s2_char_to_cnt[ord(s2[right]) - ord("a")] += 1
        
        return False
