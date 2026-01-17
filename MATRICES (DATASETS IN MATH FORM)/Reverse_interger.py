class Solution(object):
    def reverse(self, x):
        reverse=0
        sign=-1 if x<0 else 1
        x=abs(x)
        
        while x!=0:
            digit=x%10
            reverse=reverse*10+digit
            x=x//10
        reverse=reverse*sign
        if -2**31<=reverse <=2**31 - 1:
            return reverse
        else:
            return 0
        
sl=Solution()

print(sl.reverse(-12344))
