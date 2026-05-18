class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            
            aMap = defaultdict(list)

            for word in strs:
                wrd = [0] * 26
                for letter in word: 
                    wrd[ord(letter) - ord('a')] += 1
                aMap[tuple(wrd)].append(word)
            
            return list(aMap.values())