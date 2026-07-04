class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        length = len(hand)
        if length % groupSize:
            return False
        d = length // groupSize
        freq = {}
        start = min(hand)
        count = 0
        m = start
        for i in hand:
            freq[i] = freq.get(i, 0) + 1
        while freq:
            if start in freq:
                for j in range(groupSize):
                    val = start + j
                    if val not in freq:
                        return False
                    freq[val] -= 1
                    if freq[val] == 0:
                        del freq[val]

            else:
                while start not in freq:
                    start += 1
        return True
                    



        
        
        [1,2,2,3,3,4,4,5,6]
        [1,2,3,4,5,6]

            
            
                
            

        


        
        

        

 