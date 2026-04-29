class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        ans = 0
        left = 0
        right = len(people)-1
        print(people)
        while left<=right:

            if people[right]>=limit:
                ans+=1
                right-=1
            elif people[left]+people[right]<=limit:
                ans+=1
                left+=1
                right-=1
            else:
                ans+=1
                right-=1

        return ans

        