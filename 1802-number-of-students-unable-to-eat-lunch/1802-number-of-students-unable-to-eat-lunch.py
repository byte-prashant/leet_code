class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud_freq = Counter(students)
        sand_freq = Counter(sandwiches)
        if stud_freq == sand_freq:
            return 0

        for i in range(len(sandwiches)):
            if sandwiches[i] in stud_freq and stud_freq[sandwiches[i]] >0:
                stud_freq[sandwiches[i]]-=1
            else:
                return len(sandwiches)-i

        