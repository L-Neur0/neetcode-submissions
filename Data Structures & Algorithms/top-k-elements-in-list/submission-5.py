class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []
        out = []
        for n in nums:
            freq[n] += 1

        heapq.heapify(res)

        for n, f in freq.items():
            heapq.heappush(res, (-f, n)) # O(logn)
        
        return [heapq.heappop(res)[1] for _ in range(k)]


        
