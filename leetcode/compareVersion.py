class Solution:
   def compareVersion(self, version1: str, version2: str) -> int:
       l1=version1.split(".")
       l2=version2.split(".")
       m=len(l1)
       n=len(l2)
  
       if(m>n):
           l2.extend(["0"]*(m-n))
       elif(m<n):
           l1.extend(["0"]*(n-m))
      
       length=max(m,n)
  
       for i in range(length):
           if(int(l1[i])>int(l2[i])):
               return 1
           elif(int(l1[i])<int(l2[i])):
               return -1
       return 0
