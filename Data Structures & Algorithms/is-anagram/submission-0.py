class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        else:
            t="".join(sorted(t))
            s="".join(sorted(s))
            if s==t:
                return True
            else:
                return False
        