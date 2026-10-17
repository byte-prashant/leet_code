class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1],reverse = True)
        no_of_units_uploaded = 0
        for no_of_boxex, no_of_units in boxTypes:

            posssible_boxes = min(no_of_boxex,truckSize)
            truckSize -= posssible_boxes
            no_of_units_uploaded+= posssible_boxes*no_of_units

            if truckSize==0:
                return  no_of_units_uploaded

        return no_of_units_uploaded

            
               




        