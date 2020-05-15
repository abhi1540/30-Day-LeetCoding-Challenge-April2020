def isHappy(self, n: int) -> bool:
        list1 = []
        while n != 1:
            sum = 0
            while n > 0:
                a = n % 10
                sum += a**2
                n = n // 10    
            n = sum
            if n in list1:
                return False
            list1.append(n)
        return True