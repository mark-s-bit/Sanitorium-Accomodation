def  solution(A):
    A.sort()


    rooms = 0
    current_room_size = 0

    for tolerance in A :
        if current_room_size + 1 > tolerance:
            rooms += 1
            current_room_size = 1
        
        else: 
            current_room_size += 1

    if current_room_size >  0:
     
        rooms += 1

        return rooms

# Example test cases
print(solution([1, 1, 1, 1, 1]))  # Output: 5
print(solution([2, 1, 4]))        # Output: 2
print(solution([2, 7, 2, 9, 8]))  # Output: 2
print(solution([7, 3, 1, 1, 4, 5, 4, 9]))  # Output: 4