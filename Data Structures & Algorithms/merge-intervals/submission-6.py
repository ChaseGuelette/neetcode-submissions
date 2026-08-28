class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])  
        output = [intervals[0]]

        i = 0
        while i < len(intervals):
            start, end = intervals[i][0], intervals[i][1]
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append(intervals[i])
            i += 1
        return output            

        