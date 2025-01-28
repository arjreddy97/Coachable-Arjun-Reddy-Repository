class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervalToInsert = newInterval[::]
    
        
        res = []
        for i in range(len(intervals)):
            currMeeting = intervals[i]
            
            if (intervalToInsert[1] < currMeeting[0]):
                return res + [intervalToInsert] + intervals[i:]
            
            elif (currMeeting[1] < intervalToInsert[0]):
                res.append(currMeeting)
                
                
            else:
                intervalToInsert[0] = min(intervalToInsert[0],currMeeting[0])
                intervalToInsert[1] = max(intervalToInsert[1],currMeeting[1])
        
        res.append(intervalToInsert)
        
        return res
