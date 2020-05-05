/*
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
*/


class Solution:
    def findComplement(self, N: int) -> int:
        if N == 0: 
            return 1
        i = 0 
        val = 1
        while val <= N:
            N ^= 1 << i
            i += 1
            val = 2**i
        
        return N
            
