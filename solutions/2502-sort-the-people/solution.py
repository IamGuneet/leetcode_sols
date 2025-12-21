class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_name = {}

        for i in range(len(names)):
            height_name[heights[i]] = names[i]
        
        desc_heights = sorted(height_name.keys(),reverse=True)

        result = []
        for h in desc_heights:
            result.append(height_name[h])

        return result

        
