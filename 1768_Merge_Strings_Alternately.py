class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_l = list(word1)
        word2_l = list(word2)
        if len(word1_l) >= len(word2_l):
            for i in range(len(word2_l)):
                word1_l.insert(i*2+1,word2_l[i])
            temp = ''.join(word1_l)
            return temp
        else:
            for i in range(len(word1_l)):
                word2_l.insert(2*i,word1_l[i])
            print(word2_l)
            temp = ''.join(word2_l)
            return temp