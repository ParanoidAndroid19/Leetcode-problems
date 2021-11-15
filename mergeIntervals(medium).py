def merge(intervals):
    merged = []
    start = 0
    end = 1
    
    # sort by start time
    intervals.sort(key = lambda x: x[start])
    
    # the first interval has nothing before it to overlap, so directly add it
    merged.append(intervals[0])
    
    for i in range(1, len(intervals)):
        # if curr interval's start comes before the prev interval ends (thus overlap)
        if intervals[i][start] <= merged[-1][end]:
            merged[-1][end] = max(merged[-1][end], intervals[i][end])
        else:
            merged.append(intervals[i])
            
    return merged