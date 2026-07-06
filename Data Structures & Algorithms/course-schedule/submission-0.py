from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course_prereq_map = {c: [] for c in range(numCourses)}
        course_prereq_map = defaultdict(list)
        visit = set()

        # create a dict cou: pre
        for cou, pre in prerequisites: # O(n)
            course_prereq_map[cou].append(pre)

        # checks if taking a course is possible or not
        def dfs(course) -> bool:
            # Base Case 1: if course already visited, cycle detected
            if course in visit:
                return False
            # Base case 2: if no prerequisites, return True
            if course_prereq_map[course] == []:
                return True
            
            # course has prerequisites, perform dfs on each and check if all can be completed
            visit.add(course)
            for pre in course_prereq_map[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)

            # if every prerequisites can be completed, clear prereq of this course
            course_prereq_map[course] = []
            return True
            
        # go through every course and confirm if completable with dfs
        for c in range(numCourses):
            # return res=False if any course is not completable
            if not dfs(c):
                return False
        
        return True