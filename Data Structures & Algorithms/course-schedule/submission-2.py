class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visitSet = set() 
        
        def dfs(crs):
            # base case:
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True 
            visitSet.add(crs)
            for pre in preMap[crs]:
                # if we see a loop
                if not dfs(pre): return False
            visitSet.remove(crs)
            # we modify it, and we set him without prereq
            preMap[crs] = []

            return True 

        for crs in range(numCourses):
            if not dfs(crs): return False 
        return True 