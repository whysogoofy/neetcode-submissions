class TimeMap:

    def __init__(self):
        self.key_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr = self.key_map.get(key, [])
        if arr:
            self.key_map[key].append([timestamp, value])
        else:
            self.key_map[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        arr = self.key_map.get(key, [])

        if not arr:
            # print("base", arr)
            return ""
        
        l, r = 0, len(arr) - 1
        value = "" 

        while l <= r:
            mid = (l + r) // 2
            stamp = arr[mid][0]

            if stamp <= timestamp:
                value = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return value
            
