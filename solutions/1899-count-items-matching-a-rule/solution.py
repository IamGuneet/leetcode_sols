class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_dic ={"type":0,"color":1,"name":2}
        index = rule_dic[ruleKey] 
        return sum(1 for x in items if x[index] == ruleValue)
        
