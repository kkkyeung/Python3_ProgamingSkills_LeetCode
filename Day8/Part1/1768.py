class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        output = ''
        
        for i in range(min(len(word1),len(word2))):
            output += word1[i] + word2[i]
        #print(output)
        #print(word1[i+1:])
        #print(word2[i+1:])
        return output + word1[i+1:] + word2[i+1:]