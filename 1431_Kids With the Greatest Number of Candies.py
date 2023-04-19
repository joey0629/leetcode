def find_greatest(kids:list[int]):
    max = kids[0]
    for i in range(1,len(kids)):
        if kids[i]>max:
            max = kids[i]
    return max
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max = find_greatest(candies)
        result = []
        for i in candies:
            if i+extraCandies >= max :
                result.append(True)
            else :
                result.append(False)
        return result
