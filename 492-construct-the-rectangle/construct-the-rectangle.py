class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sl = area
        sw = 1
        
        res = [sl, sw]
        while sl >= sw:
            sw += 1
            if area % sw == 0:
                sl = int(area / sw)
                res[0], res[1] = sw, sl
        return res