# Approach 1:
def canCompleteCircuit(self, magic, dist):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    n = len(magic)
    starts = n
    start = -1
    i = 0
    fuel = 0
    
    #          0  1  2
    # magic = [4, 0, 1]
    # dist  = [3, 2, 1]
    
    while starts >= 0:
        if start == -1:
            if magic[i] >= dist[i]:
                fuel = magic[i] - dist[i] + magic[(i+1)%n]
                start = i
            starts = starts - 1
                
            i = (i + 1)%n
            
        else:
            # we complete the round
            if (i+1)%n == start:
                if fuel >= dist[i]:
                    return start
            
            # if we run out of fuel
            if fuel < 0:
                start = -1
                
            elif fuel < dist[i]:
                start = -1
                
            else:
                fuel = fuel - dist[i] + magic[(i+1)%n]
                
            i = (i+1)%n
            
    return -1



# Approach 2:
def canCompleteCircuit(gas, cost):
    n = len(gas)
    
    total_tank = 0
    curr_tank = 0
    start = 0
    
    for i in range(0, n):
        total_tank = total_tank + gas[i] - cost[i]
        curr_tank = curr_tank + gas[i] - cost[i]
        
        # out of fuel
        if curr_tank < 0:
            start = i + 1
            curr_tank = 0
            
    if total_tank >= 0:
        return start
    else:
        return -1
    