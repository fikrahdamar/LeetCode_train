class Solution(object):
    def isPalindrome(self, x):
            if x < 0 or ( x % 10 == 0 and x != 0):
                return False
            
            reversed_sum = 0
            original_x = x
            while x > 0 :
                reversed_sum =  reversed_sum * 10 + x % 10
                x //= 10
            
            return original_x == reversed_sum
    
solution = Solution()
print(solution.isPalindrome(121))  
print(solution.isPalindrome(-121)) 
print(solution.isPalindrome(10))   
    