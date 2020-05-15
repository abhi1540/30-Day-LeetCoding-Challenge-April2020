    def backspaceCompare(self, S: str, T: str) -> bool:
        
        max_len = max(len(S), len(T))
        
        S_mod = []
        T_mod = []
        for i in range(len(S)):
            if len(S_mod) >0 and S[i] == "#":
                S_mod.pop(-1)
            elif S[i] == "#":
                continue
            else:
                S_mod.append(S[i])
        for j in range(len(T)):
            if len(T_mod) >0 and T[j] == "#":
                T_mod.pop(-1)
            elif T[j] == "#":
                continue
            else:
                T_mod.append(T[j])
        #print(S_mod,T_mod)    
        if S_mod == T_mod:
            return True
        return False