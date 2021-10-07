# https://leetcode.com/problems/meeting-rooms-ii/

def minMeetingRooms(intervals):
    # grouping and sorting the start and end times
    start = sorted([i[0] for i in intervals])
    end = sorted(i[1] for i in intervals)
    
    s = 0
    e = 0
    rooms = 0
    
    while s < len(start):
        # condition for reusing conference room
        # meeting ended before another one began, so reuse a room
        if start[s] >= end[e]:
            rooms = rooms - 1
            e = e + 1
            
        s = s + 1
        rooms = rooms + 1
        
    return rooms
