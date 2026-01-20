class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        from collections import Counter
        
        # Count occurrences of nums2[j] * k
        count2 = Counter(x * k for x in nums2)
        
        result = 0
        for num in nums1:
            # Find all divisors of num that exist in count2
            for d in range(1, int(num**0.5) + 1):
                if num % d == 0:
                    if d in count2:
                        result += count2[d]
                    if d != num // d and (num // d) in count2:
                        result += count2[num // d]
        
        return result