from random import randint
from time import \
    sleep as \
    wait  
# #* import sleep so we can use it (as wait so it looks better)

def printnice(lis):
    s = ""
    for i in lis:
        s += str(i) + " "
    print(s)

grid = [["7", "8",  "9"],
        ["4", "5", "6"],
        ["1", "2", "3"]] 
##* Create a grid

P1 = True ##* Set player 1 to true and p2 to false
AI = False

numbers = { ##* Provide the coridenaites for each number
    1:[1, 3],
    2:[2, 3],
    3:[3, 3],
    4:[1, 2],
    5:[2, 2],
    6:[3, 2],
    7:[1, 1],
    8:[2, 1],
    9:[3, 1]
}

corner = (1, 7, 9, 3)
edge = (2, 6, 8, 4)

class robot:
    def checkAIwin(self):
        global grid
        for i in range(0,3):
            for j in range(0,3):
                if str(grid[i][j]) in str(list(range(1, 10))):
                    temp = grid[i][j]
                    grid[i][j] = "O"
                    if checkwin(n=False) != "O":
                        grid[i][j] = temp
                    else:
                        return True
        return False
    def checkPlayerWin(self):
        global grid
        for i in range(0,3):
            for j in range(0,3):
                if str(grid[i][j]) in str(list(range(1, 10))):
                    temp1 = grid[i][j]
                    grid[i][j] = "X"
                    if checkwin(n=False) == "X":
                        grid[i][j] = "O"
                        return True
                    else:
                        grid[i][j] = temp1
        return False
    def placeCenter(self):
        global grid
        if grid[1][1] in str(list(range(1, 10))):
            grid[1][1] = "O"
            return True
        else:
            return False
    def placeCorner(self):
        global grid
        nums = []
        for i in corner:
            [x,y] = numbers[i]
            if str(grid[y-1][x-1]) in str(list(range(1, 10))):
                nums.append([x,y])
        i = randint(0, len(nums))
        [x, y] = nums[i]
        if str(grid[y-1][x-1]) in str(list(range(1, 10))):
            grid[y-1][x-1] = "O"
            return True
        else:
            return False
    def placeEdge(self):
        global grid
        nums = []
        for i in edge:
            [x,y] = numbers[i]
            if str(grid[y-1][x-1]) in str(list(range(1, 10))):
                nums.append([x,y])
        i = randint(0, len[nums])
        [x, y] = nums[i]
        if str(grid[y-1][x-1]) in str(list(range(1, 10))):
            grid[y-1][x-1] = "O"
            return True
        else:
            return False

def checkwin(n=True):
    for i in range(0, 3):
        if grid[i][0] == grid[i][1] and grid[i][0] == grid[i][2]: ##* Check row
            return grid[i][0]
        if grid[0][i] == grid[1][i] and grid[0][i] == grid[2][i]: ##* Check colomn
            return grid[0][i]
    if grid[0][0] == grid[1][1] and grid[2][2] == grid[0][0]: ##* Check diagolnal 1
        return grid[0][0]
    if grid[0][2] == grid[1][1] and grid[2][0] == grid[1][1]: ##* Check diagolnal 2 
        return grid[2][0]
    if n:
        result = checktie()
        return result

def checktie():
    tie = True 
    for i in range(0, 3): ##* Check tie
        for j in range(1, 10):
            if str(j) in grid[i]:
                tie = False
                return
    return "tie"

def update(n): ##* Update screen
    ##* Print grid
    print("")

    printnice(grid[0])
    printnice(grid[1])
    printnice(grid[2])

    if n:
        p = "Player 1"
    else:
        p = "AI"
    
    print("")
    print("It is %s's turn" %p)
    print("")

    if n:
        d = int(input("Input: "))
        [x,y] = numbers[d]
        if grid[y-1][x-1] not in str(list(range(1, 10))):
            print("Try again, the spot is already taken")
            return update(n)
        grid[y-1][x-1] = "X"
    else:
        wait(1)
        if not bot.checkAIwin():
            if not bot.checkPlayerWin():
                if not bot.placeCenter():
                    if not bot.placeCorner():
                        bot.placeEdge()
        wait(1)

    i = checkwin(n=True)
    if i == "X" or i == "O":
        printnice(grid[0])
        printnice(grid[1])
        printnice(grid[2])
        if i == "O":
            i = "Ai"
        print("%s wins!!" %i)
        wait(1)
        exit()
    if i == "tie":
        wait(1)
        printnice(grid[0])
        printnice(grid[1])
        printnice(grid[2])
        print("")
        print("It is a tie")
        wait(1)
        exit()

def main():
    i = 1
    while True:
        if i % 2 == 0:
            update(AI)
        else:
            update(P1)
        i += 1

if __name__ == "__main__":
    bot = robot()
    main()