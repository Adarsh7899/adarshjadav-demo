from turtle import *

win = False

speed(0)
bgcolor("lightgreen")
yanse="black"
gz=40

judge = Turtle()
judge.up()
judge.goto(-460, 330)
judge.write("Next", font=("Arial", 40, "bold"))
judge.color(yanse)
judge.goto(-420, 300)
judge.dot(30)

for i in range(19):
    up()
    goto(-gz*9, gz*(9-i))
    down()
    fd(gz*18)
    bk(gz*18)

rt(90)

for i in range(19):
    up()
    goto(gz*(9-i), gz*9)
    down()
    fd(gz*18)
    bk(gz*18)

pensize(5)
for i in range(4):
    fd(gz*18)
    rt(90)

# m = [[0] * 19 for i in range(19)]
m =[
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def check(i, j):
    global win

    player = m[i][j]

    directions = [(1,0), (0,1), (1,1), (1,-1)]

    for dx, dy in directions:
        count = 1

        x = i + dx
        y = j + dy

        while 0 <= x < 19 and 0 <= y < 19 and m[x][y] == player:
            count += 1
            x += dx
            y += dy

        x = i - dx
        y = j - dy

        while 0 <= x < 19 and 0 <= y < 19 and m[x][y] == player:
            count += 1
            x -= dx
            y -= dy

        if count >= 5:
            win = True
            penup()
            goto(0,0)

            if player == 1:
                write("BLACK WINS!", align="center",
                      font=("Arial",40,"bold"))
            else:
                write("WHITE WINS!", align="center",
                      font=("Arial",40,"bold"))
            return
def play(x, y):
    global yanse

    if not win:

        color(yanse)
        penup()

        x = round(x / gz) * gz
        y = round(y / gz) * gz

        i = int(9 - y / gz)
        j = int(x / gz + 9)

        if 0 <= i <= 18 and 0 <= j <= 18:

            if m[i][j] == 0:

                goto(x, y)
                dot(30)

                if yanse == "black":
                    m[i][j] = 1
                    check(i, j)
                    yanse = "white"

                else:
                    m[i][j] = 2
                    check(i, j)
                    yanse = "black"

                judge.color(yanse)
                judge.dot(30)    


onscreenclick(play,1)
done()