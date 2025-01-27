class TimeMap:
    
    def __init__(self):
        self.dataStore = {}
    
    

    def set(self, key: str, value: str, timestamp: int) -> None:
    
        if (key in self.dataStore):
            self.dataStore[key].append((value, timestamp))
        else:
            self.dataStore[key] = [(value, timestamp)]
    
    
    

    def get(self, key: str, timestamp: int) -> str:
    
        if key not in self.dataStore:
            return ""
    
        timestamps = self.dataStore[key]
    
    
    
        if timestamp < timestamps[0][1]:
            return ""

        lo, hi = 0, len(timestamps) - 1
    
        while (lo <= hi):
            mid = lo + (hi - lo) // 2
        
            if timestamp > timestamps[mid][1]:
                lo = mid + 1
            elif timestamp < timestamps[mid][1]:
                hi = mid - 1
            
            else:
                return timestamps[mid][0]
        
        return timestamps[hi][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
