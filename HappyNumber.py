class Solution:
    def isHappy(self, n: int) -> bool:
        listNum = {}
        while True:
            sum = 0
            
            while n >= 1:
                sum += (n%10)*(n%10)
                n //= 10
            n = sum
            
            if sum == 1:
                return True
            elif sum in listNum:
                return False
            listNum[n] = 1