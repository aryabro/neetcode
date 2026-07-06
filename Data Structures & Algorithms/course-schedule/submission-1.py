from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Pattern: DFS on Directed Graph + Cycle Detection.

        Problem:
        There are numCourses courses labeled from 0 to numCourses - 1.
        prerequisites[i] = [course, prereq] means:
            To take course, we must first take prereq.
        Return True if it is possible to finish all courses.
        Return False if there is a cycle.

        Key idea:
        This is a directed graph problem.
        Each course points to the courses it depends on.
        Example:
            [1, 0] means course 1 depends on course 0.
            Graph: 1 -> 0
        If we ever revisit a course that is already in the current DFS path,
        that means there is a cycle.

        We use:
        - course_prereq_map:
            Maps each course to its prerequisites.
        - visit:
            Tracks courses in the current DFS path only.
            This helps detect cycles.

        Optimization:
        Once we prove a course can be completed, we set its prerequisites to [].
        This means future DFS calls can immediately return True for that course.

        Time: O(numCourses + prerequisites), because each course and edge is processed once.
        Space: O(numCourses + prerequisites), for the graph and recursion stack.
        """
        # build adjacency list
        # course_prereq_map = {c: [] for c in range(numCourses)}
        course_prereq_map = defaultdict(list)
        for cou, pre in prerequisites: # O(n)
            course_prereq_map[cou].append(pre)

        # track current DFS path
        visit = set()

        # Returns bool if taking a course is possible or not
        def dfs_isCompletable(course) -> bool:
            # Base Case 1: if course already visited, cycle detected
            if course in visit:
                return False
            # Base case 2: if no prerequisites, return True
            if course_prereq_map[course] == []:
                return True
            
            # course has prerequisites, perform dfs on each and check if all can be completed
            visit.add(course)
            for pre in course_prereq_map[course]:
                if not dfs_isCompletable(pre):
                    return False
            visit.remove(course)

            # if every prerequisites can be completed, clear prereq of this course
            course_prereq_map[course] = []
            return True
            
        # go through every course and confirm if completable with dfs
        for c in range(numCourses):
            # return res=False if any course is not completable
            if not dfs_isCompletable(c):
                return False
        
        return True