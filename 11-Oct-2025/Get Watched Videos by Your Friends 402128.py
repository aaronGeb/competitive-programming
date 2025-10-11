# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        '''
        wv[i] == p[i]
        f[i] == [] p[i]
        id st 
        l1 =  fr
        l2 = fr= fr

        '''
        n = len(friends)
        current_level = 0
        visit = {id}
        q = deque([id])
        while q and current_level < level:
            for _ in range(len(q)):
                p = q.popleft()
                for f in friends[p]:
                    if f not in visit:
                        visit.add(f)
                        q.append(f)
            current_level +=1
        fri_lev = list(q)
        count = Counter()
        for f in fri_lev:
            count.update(watchedVideos[f])
        def sort_key(video):
            return (count[video], video)
        ans = sorted(count.keys(), key = sort_key)
        return ans