class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for word in strs:
            strr=''.join(sorted(word))
            if strr in hm:
                hm[strr].append(word)
            else:
                hm[strr]=[word]
        return list(hm.values())
