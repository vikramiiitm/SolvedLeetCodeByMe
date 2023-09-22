class Solution:
    # We are looping through t for every element of s, we keep slicing(keep the right side) the t until the char is not found in the string2, if found add the char in parsed string
    #compare the parsed string after loop if it equals to s
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


# Other solution: Read it

'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x=iter(t)
        return all(ch in x for ch in s)
        

'''