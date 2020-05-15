    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for items in shift:
            if items[0] == 1:
                s = s[len(s)-items[1]:] + s[0:len(s)-items[1]]
            elif items[0] == 0:
                s = s[items[1]:len(s)] + s[0:items[1]]
        return s