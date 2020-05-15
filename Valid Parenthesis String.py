class Solution:
    def checkValidString(self, arg: str) -> bool:
        if len(arg) == 1 and arg[0] != "*":
            return False
        if len(arg) == 1 and arg[0] == "*":
            return True
        s = []
        t = []
        for i in range(len(arg)):
            if arg[i] == "(":
                s.append(i)
            elif arg[i] == "*":
                t.append(i)
            else:
                if len(s) != 0:
                    s.pop()
                elif len(t) != 0:
                    t.pop()
                else:
                    return False
        try:
            while len(s) != 0 and len(t) != 0:
                if s[-1] < t[-1]:
                    s.pop()
                    t.pop()
                else:
                    break
        except:
            pass
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) == 0 and len(t) != 0:
            return True