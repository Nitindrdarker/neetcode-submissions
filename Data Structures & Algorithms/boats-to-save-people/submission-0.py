class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        count = 0
        while left < right:
            if people[right] + people[left] <= limit:
                right -= 1
                left += 1
                count += 1
            elif people[right]:
                right -= 1
                count += 1
        if left == right:
            count += 1
        return count


