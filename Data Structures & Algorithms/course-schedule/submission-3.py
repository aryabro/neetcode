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
        - dfs_path:
            Tracks courses in the current DFS path only.
            This helps detect cycles.

        Optimization:
        Once we prove a course can be completed, we set its prerequisites to [].
        This means future DFS calls can immediately return True for that course.

        Time: O(numCourses + prerequisites), because each course and edge is processed once.
        Space: O(numCourses + prerequisites), for the graph and recursion stack.
        """
        # build adjacency list
        # course_prereq_map = defaultdict(list) # another way but below is better for this problem
        course_prereq_map = {c: [] for c in range(numCourses)}
        for cou, pre in prerequisites: # O(n)
            course_prereq_map[cou].append(pre)

        # track current DFS path
        dfs_path = set()

        # Returns bool if taking a course is possible or not
        def dfs_isCompletable(course) -> bool:
            # Base Case 1: if we come back to course currently in dfs path, cycle detected
            if course in dfs_path:
                return False

            # Base case 2: if no prerequisites, return True
            if course_prereq_map[course] == []:
                return True
            
            # this course has prerequisites. Add it to dfs_path and perform dfs on its prerequisites
            dfs_path.add(course)
            for pre in course_prereq_map[course]:
                if not dfs_isCompletable(pre):
                    return False # if any prerequisites are false, then this is false as well
            dfs_path.remove(course) # remove from path once done

            # if every prerequisites can be completed, empty values of key
            course_prereq_map[course] = []
            return True
            
        # go through every course and confirm if completable with dfs
        for c in range(numCourses):
            # if any course creates a cycle, finishing all is impossible
            if not dfs_isCompletable(c):
                return False
        
        return True