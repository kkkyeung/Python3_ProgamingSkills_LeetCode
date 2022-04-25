class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        AlienDictionary = {}
        NumList = []
        
        for i in range(len(order)):
                AlienDictionary[order[i]] = i
                
        for w in words:
            NewList = []
            for SingleLetter in w:
                #print(SingleLetter)
                NewList.append(AlienDictionary[SingleLetter])
                # print("Output1")
                # print(NewList)
            NumList.append(NewList)
        # print("Output2")
        # print(NumList)
        for w1, w2 in zip(NumList, NumList[1:]):
            #print(w1)
            #print(w2)
            if w1 > w2:
                return False
        return True