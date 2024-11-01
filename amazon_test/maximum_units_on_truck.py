class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        '''
        You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, 
        where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
        numberOfBoxesi is the number of boxes of type i.
        numberOfUnitsPerBoxi is the number of units in each box of the type i.
        You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. 
        You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
        Return the maximum total number of units that can be put on the truck.'''

        # we will use the greedy algorithm - will take the largest box that can fit right now and that is available
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        loaded = 0
        weight = 0
        row = 0

        while truckSize >= loaded and row < len(boxTypes):            
            if truckSize - loaded > 0: # we still have room for this box
                
                boxTypes[row][0] -= 1
                
                loaded += 1
                weight += boxTypes[row][1]
                # print("Loaded " + str(loaded))
                if boxTypes[row][0] == 0:
                    row += 1
            else:
                break
        return weight

        
