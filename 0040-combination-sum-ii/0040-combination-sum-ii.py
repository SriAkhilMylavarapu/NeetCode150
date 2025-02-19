class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, tot):
            if tot == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or tot > target:
                return
            
            cur.append(candidates[i])
            tot += candidates[i]
            dfs(i+1, cur, tot)
            cur.pop()
            tot -= candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, tot)

        dfs(0, [], 0)
        return res

        
        