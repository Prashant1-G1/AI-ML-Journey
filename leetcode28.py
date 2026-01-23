class Solution(object):
    def strStr(self, haystack, needle):
       if needle in haystack:
            return haystack.index(needle)
       else:
            return -1

sl=Solution()

print(sl.strStr("ramhram","ram"))


# if we need to return last index 
# Index=[]
#         for x in range(len(haystack)-len(needle)+1):
#                 if haystack[x:x+len(needle)]==needle:
#                      Index.append(x)
                
        
            
#         return Index[-1] if Index else -1