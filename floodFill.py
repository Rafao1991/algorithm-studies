def floodFillBFS(screen, x, y, newC, oldC):
    vis=[]
    q = [(x,y)]
    while q:
        x,y = q.pop(0)
        screen[x][y] = newC
        if (x,y) not in vis:
            vis.append((x,y))
        
        if x + 1 < len(screen):
            if (x + 1,y) not in vis:
                if screen[x + 1][y] == oldC:
                    q.append((x + 1, y))

        if x - 1 >= 0:
            if (x - 1,y) not in vis:
                if screen[x - 1][y] == oldC:
                    q.append((x - 1, y))
        
        if y + 1 < len(screen[x]):
            if (x,y + 1) not in vis:
                if screen[x][y + 1] == oldC:
                    q.append((x, y + 1))

        if y - 1 >= 0:
            if (x,y - 1) not in vis:
                if screen[x][y - 1] == oldC:
                    q.append((x, y - 1))

def floodFill(screen, x, y, newC):
    oldC = screen[x][y]
    floodFillBFS(screen, x, y, newC, oldC)
    
# Dimentions of paint screen
M = 8
N = 8

# Driver Code
screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]
 
x = 4
y = 4
newC = 3
floodFill(screen, x, y, newC)
 
print ("Updated screen1 after call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end = ' ')
    print()
    
screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]
 
x = 0
y = 0
newC = 9
floodFill(screen, x, y, newC)
 
print ("Updated screen2 after call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end = ' ')
    print()
    
screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]
 
x = 7
y = 2
newC = 5
floodFill(screen, x, y, newC)
 
print ("Updated screen3 after call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end = ' ')
    print()
    
screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]
 
x = 2
y = 7
newC = 6
floodFill(screen, x, y, newC)
 
print ("Updated screen3 after call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end = ' ')
    print()