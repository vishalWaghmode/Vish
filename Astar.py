#Based On https://www.redblobgames.com/pathfinding/a-star/introduction.html
#This Program Uses Sorting Instead of PriorityQuee To lessen line of code
#1 => Path , 0 => RoadBlock
maze = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]
heurestic = lambda a , b : abs(a[0] - b[0]) + abs(a[1] - b[1])#Using Eucledian Distance as Heurestic Function
goal = (len(maze)-1,len(maze[0])-1)
Quee = [(0,0)]
came_from = {(0,0):None}
cost_so_far = {(0,0):0}
while Quee:
    Quee = sorted(Quee,key = lambda x:heurestic(x,goal))
    current = Quee.pop(0)
    if goal in Quee:
        break
    
    for direction in [(0,1),(1,0),(-1,0),(0,-1)]:
        ele = (current[0] + direction[0] , current[1] + direction[1])
        if ele[0] >=0 and ele[1]<len(maze[0]) and ele[1]>=0 and ele[0]<len(maze) and maze[ele[0]][ele[1]]:#Check for out of bound and path
            new_cost = cost_so_far[current] + 1
            if ele not in cost_so_far or new_cost < cost_so_far[ele]:
                cost_so_far[ele] = new_cost
                Quee.append(ele)
                came_from[ele] = current
if goal in came_from:
    print("Path Length Is " ,cost_so_far[goal])
    print("Actual Path is :")
    current = goal
    str_ = ""
    while came_from[current]:
        str_ += str(current)+"-"
        current = came_from[current]
    print("->".join((str_+str(current)).split("-")[::-1]))
else:
    print("Path Doesnt Exist")

