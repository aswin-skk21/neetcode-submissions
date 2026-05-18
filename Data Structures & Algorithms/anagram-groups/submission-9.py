class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        for i in strs:
            sorted_key = "".join(sorted(i))
            check[sorted_key].append(i)
        return list(check.values())