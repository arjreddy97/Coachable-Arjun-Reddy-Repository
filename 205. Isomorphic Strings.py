def isIsomorphic(self, s, t):
       mappingsOne={}
       mappingsTwo={}
       for i in range(len(s)):
           if s[i] not in mappingsOne:
               mappingsOne[s[i]]=t[i]
           else:
               if mappingsOne[s[i]]!=t[i]:
                   return False
           if t[i] not in mappingsTwo:
               mappingsTwo[t[i]]=s[i]
           else:
               if mappingsTwo[t[i]]!=s[i]:
                   return False
       return True
          
