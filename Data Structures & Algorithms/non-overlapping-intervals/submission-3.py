class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x : x[0])
        output = [intervals[0]]
        res = 0
        i = 1
        print(output)
        print(intervals)
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            # print([lastStart, lastEnd])
            # print(start, end)
            if lastEnd > start:
                res += 1
                lastStart, lastEnd = output.pop()
                winner =  min(end, lastEnd)
                if winner == lastEnd:
                    output.append([lastStart, lastEnd])
                else:
                    output.append([start, end])
            else:
                output.append([start, end])
        print(output)
        return res
        