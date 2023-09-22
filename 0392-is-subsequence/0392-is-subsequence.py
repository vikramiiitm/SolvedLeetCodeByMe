class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        parsed = ''
        for i in s:
            while len(t)>0 and t[0] != i:
                t = t[1:]
            
            if len(t)>0 and t[0] == i:
                parsed+= t[0]
                t=t[1:]
        if parsed == s:
            return True