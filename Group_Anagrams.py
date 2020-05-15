    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = {}
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) not in dict1:
                dict1[''.join(sorted(strs[i]))] = [strs[i]]
            else:
                dict1[''.join(sorted(strs[i]))].append(strs[i])
            
        return list(dict1.values())