from bisect import bisect_right

def isSubsequence(word, pos):

    prevIndex = -1

    for ch in word:

        indices = pos[ord(ch) - ord('a')]

        idx = bisect_right(indices, prevIndex)

     
        if idx == len(indices):
            return False

        prevIndex = indices[idx]

    return True


class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        # code here

        pos = [[] for _ in range(26)]

        for i in range(len(s)):
            pos[ord(s[i]) - ord('a')].append(i)

        res = ""

        for word in d:

   
            if len(word) < len(res):
                continue

            
            if isSubsequence(word, pos):

                if (len(word) > len(res) or
                        (len(word) == len(res) and word < res)):

                    res = word

        return res