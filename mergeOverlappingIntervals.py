intervals = [
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]

# two key learnings:
# array[-1] to access the last value in an array
# max(value1, value2) to get the max value between multiple values

def mergeOverlappingIntervals(intervals):
    out = []
    intervals.sort()
    for i in range(len(intervals)):
        print(intervals[i])
        if i == 0:
            out.append(intervals[i])
            print(out)
        if intervals[i][0] <= out[-1][1]:
            out[-1][1] = max(intervals[i][1],out[-1][1])
            print(out)
        if intervals[i][0] > out[-1][1]:
            out.append(intervals[i])
    print(out)
    return(out)
        

    #     start = intervals[i][0]
    #     end = intervals[i][1]
    #     print(start, end)
    #     if i == len(intervals) - 1:
    #         out.append(intervals[i])
    #         break
    #     if end < intervals[i + 1][0]:
    #         out.append(intervals[i])
    #     if end >= intervals[i+1][0]:
    #         intervals[i+1][0] = start
    # print(out)
    # return out

a = mergeOverlappingIntervals(intervals)
print(a)