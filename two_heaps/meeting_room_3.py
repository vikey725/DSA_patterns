import heapq

def most_booked(meetings, rooms):
    count_tracker = [0] * rooms
    used_rooms = []
    available_rooms = [i for i in range(rooms)]
    heapq.heapify(available_rooms)

    meetings.sort()

    for st, et in meetings:

        while used_rooms and used_rooms[0][0] <= st:
            end, room = heapq.heappop(used_rooms)
            heapq.heappush(available_rooms, room)

        if not available_rooms:
            end, room = heapq.heappop(used_rooms)
            et = end + (et - st)
            heapq.heappush(available_rooms, room)
        
        available_room = heapq.heappop(available_rooms)
        heapq.heappush(used_rooms, (et, available_room))
        count_tracker[available_room] += 1

    return count_tracker.index(max(count_tracker))




