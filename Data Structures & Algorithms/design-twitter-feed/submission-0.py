import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)   # userId -> [(timestamp, tweetId)...]
        self.following = defaultdict(set) # userId -> {followeeId,...}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        users = self.following[userId] | {userId}

        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                cnt, tweetId = self.tweets[u][idx]
                heapq.heappush(heap, (cnt, tweetId, u, idx - 1))

        result = []
        while heap and len(result) < 10:
            cnt, tweetId, u, idx = heapq.heappop(heap)
            result.append(tweetId)
            # Push the next most recent tweet from the same user
            if idx >= 0:
                cnt2, tweetId2 = self.tweets[u][idx]
                heapq.heappush(heap, (cnt2, tweetId2, u, idx - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)