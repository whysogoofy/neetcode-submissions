class Twitter:

    def __init__(self):
        self.followers_map = {}
        self.user_to_twts = {}
        self.counter = 0
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # print("post twt")
        hashmap = self.user_to_twts.get(userId, {})
        # print(arr)
        hashmap[self.counter] = tweetId
        # arr.append([tweetId, self.counter])
        self.user_to_twts[userId] = hashmap
        self.counter += 1
        # print(arr)
        # print(self.user_to_twts)

    def getNewsFeed(self, userId: int) -> List[int]:
        # print("getNews", userId)
        # print(self.followers_map)
        arr = self.followers_map.get(userId, []) + [userId]
        # print(arr)
        heap = []
        hashmap = {}

        for follower in arr:
            twts_map = self.user_to_twts.get(follower, [])
            for count in twts_map:
                heapq.heappush(heap, count)
                hashmap[count] = twts_map[count]
        
        # print("heap", heap)
        
        if not heap:
            return []
        
        while len(heap) > 10:
            heapq.heappop(heap)
        
        # print(heap)
        heap.sort()
        # print(heap)

        output = []

        for ele in heap[::-1]:
            output.append(hashmap[ele])

        # print("heap rest", heap)
        
        return output
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # print("follow")
        arr = self.followers_map.get(followerId, [])
        # print(arr)
        if not followeeId in arr and followeeId != followerId: 
            arr.append(followeeId)
            self.followers_map[followerId] = arr
        # print(arr)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # print("unfollow")
        arr = self.followers_map.get(followerId, [])
        # print(arr)
        if followeeId in arr and followeeId != followerId:
            arr.remove(followeeId)
            self.followers_map[followerId] = arr
        # print(arr)