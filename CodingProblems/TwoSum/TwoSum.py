from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create dict: Keys indices, values actual values
        pairs = defaultdict(int)
        for i in range(len(nums)):
            for j in range(len(nums)):
                # same element can't be used twice
                if i == j:
                    continue
                # For uniform listing in dict / to prevent duplication, list elements in order of size
                elif i < j:
                    key = (i, j)
                else:
                    key = (j, i)

                if pairs[key] != 0:
                    val = (nums[i], nums[j])
                    pairs[key : val]

        # Find sums of these terms, return indices when solution found
        pairitems = pairs.items()
        for key, value in pairitems:
            if value[0] + value[1] == target:
                return list(key)
        #Should only return if error
        return pairitems


if __name__ == '__main__':
    samplenums = [2, 7, 11, 15]
    sampletarget = 9
    test = Solution.twoSum(samplenums, sampletarget)
