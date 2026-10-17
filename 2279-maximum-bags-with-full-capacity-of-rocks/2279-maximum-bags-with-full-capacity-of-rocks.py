class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        
        remaining_capacity = [ capacity[bag]-rocks[bag] for bag in range(len(capacity))]

        
        remaining_capacity.sort()
        full_capacity_bag =0 
        for bag, remaining_capa in enumerate(remaining_capacity):

        
            if remaining_capa <= additionalRocks:
                additionalRocks -=remaining_capa
                full_capacity_bag+=1

            else:

                return full_capacity_bag

        return full_capacity_bag

            






