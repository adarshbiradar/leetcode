class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        blue_count = 0
        max_value = 0
        blue_on = 0
        
        for i in light:
            max_value = max(max_value,i)
            blue_on+=1
            if blue_on == max_value:
                blue_count+=1
        return blue_count
