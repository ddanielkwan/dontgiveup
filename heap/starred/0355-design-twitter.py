# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweetmap = defaultdict(list) #store userid and list of their  tweets (timestamp, tweetid)
        self.followmap = defaultdict(set) #store userId and who they follow
        #store who we are following followmap[me] = [i follow a ,b ,c]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.timestamp, tweetId])
        #step 1
        #eventually tweetmap[a] = [(-1,-1), (-2,-2), (-3,-3)]
        #eventually tweetmap[b] = [(-4,-4), (-5,-5), (-6,-6)]
        self.timestamp -= 1 #means most recently so we use negative

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        #were going to use a heap to keep track of the indices in the arrys tweet and see which one has most recent and pop from there
        self.followmap[userId].add(userId) #in case we want our feed as well

        #go through every single person i am following
        for followeeId in self.followmap[userId]: 
            #if that person has a tweet
            if followeeId in self.tweetmap: 
                #recall in step 1, do you agree that as person tweets, the timestamp increases so its the latest at the end
                index = len(self.tweetmap[followeeId]) - 1
                #this index is the latest possible tweet element of a person

                timestamp, tweetId = self.tweetmap[followeeId][index]
                #we want to use a minheap(technically maxheap) because lowest negative is most recent
                heapq.heappush(minHeap, [timestamp,tweetId, followeeId, index-1])
                #timestmap first, renember we did -timestmap so that higher most recent will be first 
        
        while minHeap and len(res) < 10:
            #pop the latest timestamp
            timestamp, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            #if there are more tweets
            if index >= 0:
                timestamp, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [timestamp, tweetId, followeeId, index-1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId) #foollower is following followee

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

