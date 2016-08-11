class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        for i in range(len(p)): #start match with the head of s
            if s[0]==p[i] and p[i]!='.':
                p=p[i:]
                break
            
        for j in range(len(s)):
            if s[j]==p[j] and j==len(p)-1:
                return True
            elif s[j]==p[j] or p[j]=='.':
				continue
            elif p[j]=='*':
                p[j]==p[j-1]
                if s[j]==p[j] or p[j]=='.':
                    continue
            else:
                return False

				
ob = Solution()
print ob.isMatch("aa","a") # false
print ob.isMatch("aa","aa") # true
print ob.isMatch("aaa","aa") # false
print ob.isMatch("aa", "a*") # true
print ob.isMatch("aa", ".*") # true
print ob.isMatch("ab", ".*") # true
print ob.isMatch("aab", "c*a*b") # true