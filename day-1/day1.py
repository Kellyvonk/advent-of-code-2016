input = open ('input', 'r').read()
# input = "R8, R4, R4, R8"
# north = n
# east = e
# south = s
# west = w

location_x = 0
location_y = 0
facing = 'n'

list_coordinates = []

# start = 0, 0 is facing north

directions = input.split(sep=', ')
    
for blocks in directions:
    if blocks[0] == 'R':
        if facing == 'n':
            facing = 'e'
        elif facing == 'e':
            facing = 's'
        elif facing == 's':
            facing = 'w'
        elif facing == 'w':
            facing = 'n'

    elif blocks[0] == 'L':
        if facing == 'n':
            facing = 'w'
        elif facing == 'w':
            facing = 's'
        elif facing == 's':
            facing = 'e'
        elif facing == 'e':
            facing = 'n'
    print("--------------------")
    print("instruction:", blocks)
    print("facing:", facing)

    start_x = location_x
    start_y = location_y


    if facing == 'n':  
        location_y = location_y +int(blocks[1:])
    elif facing == 'e':
        location_x = location_x +int(blocks[1:])
    elif facing == 's':
        location_y = location_y -int(blocks[1:])
    elif facing == 'w':
        location_x = location_x -int(blocks[1:])
    
    # list_coordinates.append((location_x, location_y))
    end_x = location_x
    end_y = location_y
    
    if end_y < start_y:
        step_y = -1
    else:
        step_y = 1
    if end_x < start_x:
        step_x = -1
    else:
        step_x = 1

    print("start_x", start_x, "end_x", end_x, "step_x", step_x)
    print("start_y", start_y, "end_y", end_y, "step_y", step_y)

    for x in range(start_x, end_x + step_x, step_x):
        for y in range(start_y, end_y + step_y, step_y):
            print("between", x, y)
            list_coordinates.append((x, y))
    
    list_coordinates = list_coordinates[:-1]
# print (list_coordinates)

# manhattan_distance = # blocks from start till end

start = 0, 0
end = location_x, location_y

print ("start:", start)
print ("end:", end)
distance_in_blocks = (abs(location_x) + abs(location_y))
print ("dinstance to end", distance_in_blocks)

# PART 2

print("------------- part 2 -------------")

# something with understanding the assignment...
l1=[]
for spot in list_coordinates:
   if spot not in l1:
       l1.append(spot)
   else:
       print(spot,end=' ')

