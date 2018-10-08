# Given a char array representing tasks CPU need to do. 
# It contains capital letters A to Z where different letters represent different tasks.
# Tasks could be done without original order. Each task could be done in one interval. 
# For each interval, CPU could finish one task or just be idle.
# However, there is a non-negative cooling interval n that means between two same tasks, 
# there must be at least n intervals that CPU are doing different tasks or just be idle.
# You need to return the least number of intervals the CPU will take to finish all the given tasks.


def leastInterval(self, tasks, N):
    task_counts = collections.Counter(tasks).values()
    M = max(task_counts)
    Mct = task_counts.count(M)
    return max(len(tasks), (M - 1) * (N + 1) + Mct)