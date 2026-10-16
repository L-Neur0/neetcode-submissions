class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for O(n) you need hashmap 

        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for l in s: 
            s_map[l] +=1 
        for l in t:
            t_map[l] +=1 
        return s_map == t_map

        