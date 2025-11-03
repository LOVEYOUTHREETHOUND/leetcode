#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30204
#
# [49] 字母异位词分组
#
# import collections

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashTable = collections.defaultdict(list)
        # for s in strs:
        #     key = ''.join(sorted(s))
        #     hashTable[key].append(s)
        # return list(hashTable.values())
        hashTable = dict()
        for s in strs:
            key =''.join(sorted(s))
            if key in hashTable:
                hashTable[key].append(s)
            else:
                hashTable[key] = [s]
        return list(hashTable.values())

# @lc code=end



#
# @lcpr case=start
# ["eat", "tea", "tan", "ate", "nat", "bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

