class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictList = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            dictList[key].append(s)
        return list(dictList.values())