class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} #for the freqlist
        ans = []
        index = 0
        for word in strs:
            freqlist = [0]*26
            for letter in word:
                freqlist[ord(letter)-ord('a')] += 1
            freqlist = ''.join(str(freqlist))
            if freqlist in hashmap:
                ans[hashmap[freqlist]].append(word)
            else:
                hashmap[freqlist] = index
                ans.append([word])
                index += 1
        return ans
        