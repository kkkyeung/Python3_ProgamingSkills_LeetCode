class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        flag = 0
        output = []
        if len(temperatures) == 1:
            return [0]
        
        for i in range(len(temperatures)-1):
            if temperatures[i] >= temperatures[i+1]:
                if i+1 != len(temperatures)-1:
                    for j in range(i+2, len(temperatures)):
                        if j == len(temperatures)-1 and (not temperatures[j] > temperatures[i]):
                            output.append(0)
                        elif temperatures[j] > temperatures[i]:
                            output.append(j-i)
                            break
                        else:
                            continue
                else:
                    output.append(0)
            else:
                output.append(1)
        output.append(0)
        return output

# my solution , but Time Limit Exceeded @@......