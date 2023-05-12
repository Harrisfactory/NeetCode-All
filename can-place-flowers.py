class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        #loop through flowerbed
            #if 0 is hit, check left for 0 or none, AND check right for 0 or none
                #change 0 in place to 1
                #subtract 1 from n
            #else
                #continue

        #if n is > 0 return false

        #return true


        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i - 1 < 0 or flowerbed[i-1] == 0) and (i + 1 > len(flowerbed) - 1 or flowerbed[i+1] == 0):
                    flowerbed[i]=1
                    n-=1
                else:
                    continue
        if n > 0: return False

        return True

        #runtime is O(n) where n is the number of elements in the flowerbed