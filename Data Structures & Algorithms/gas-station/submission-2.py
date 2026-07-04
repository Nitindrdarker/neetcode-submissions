class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total = 0
        tank = 0
        res =0
        for i in range(len(gas)):
            d = gas[i] - cost[i]
            
            total += d
            tank += d
            if tank < 0:
                res = i + 1
                tank = 0
            

        
        if total < 0:
            return -1
        return res
        

        
        
