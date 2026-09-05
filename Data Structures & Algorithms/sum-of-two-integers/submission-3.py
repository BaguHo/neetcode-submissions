class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            # carry값
            carry = (a & b) << 1
            # XOR 연산
            a = (a ^ b) & mask
            b = carry & mask
            
        return a if a <= max_int else ~(a ^ mask)