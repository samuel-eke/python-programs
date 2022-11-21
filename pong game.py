import turtle


wn = turtle.Screen()
wn.title("Samuel's Pong Game")
#n.bgcolor ("blue")
wn.bgpic("pongg.gif")
wn.setup (width= 800, height=600)
wn.tracer(0)
player_a = wn.textinput("Player Name one", "Enter your player name ")
player_b = wn.textinput("Player Name two", "Enter your player name ")

#score
score_a = 0
score_b = 0


#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of the animation sets it to the maximum animatino speed
paddle_a.shape ("square")
paddle_a.color("white")
paddle_a.shapesize (stretch_wid=5, stretch_len=1) #this method strechs the lenght and width of the paddle. by default it is 20x20
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of the animation sets it to the maximum animatino speed
paddle_b.shape ("square")
paddle_b.color("white")
paddle_b.shapesize (stretch_wid=5, stretch_len=1) #this method strechs the lenght and width of the paddle. by default it is 20x20
paddle_b.penup()
paddle_b.goto(350, 0)

#for the ball
ball = turtle.Turtle()
ball.speed(0) #speed of the animation sets it to the maximum animatino speed
ball.shape ("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4 #this sets the directional speed of the ball, in either direction; 2px
ball.dy = -0.4

#pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #helps not to draw a line when the pen moves. every turtle starts from the middle of the screen
pen.hideturtle()
pen.goto (0, 260)
pen.write("{} 0 {} 0".format(player_a, player_b), align="center", font=("Arial", 24, "normal"))

def final_score_a ():
    pen.clear()
    pen.goto (0, 0)
    pen.write("{} has won".format(player_a), align="center", font=("arial", 28, "normal"))
    ball.goto (0, 0)
    ball.dx = 0
    ball.dy = 0

def final_score_b ():
    pen.clear()
    pen.goto (0, 0)
    pen.write("Game Over")
    pen.clear()
    pen.write("{} has won".format(player_b), align="center", font=("Arial", 28, "normal"))
    ball.dx = 0
    ball.dy = 0

#function for the movement of the paddles

def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)
    if paddle_a.ycor() > 250: #boundaries of the paddle 
        paddle_a.sety(250)

def paddle_a_down ():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)
    if paddle_a.ycor() < -250: #boundaries for the paddle
        paddle_a.sety(-250)

#this is for paddle b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)
    if paddle_b.ycor() > 250: #boundaries for the paddle
        paddle_b.sety(250)

def paddle_b_down ():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

#keyboard binding

wn.listen() #it listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "z")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#main game loop
while True:
    wn.update()
    

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check for y (up and down) we use the dimensions of the screen to determine this
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("{} has {} {} has {}".format(player_a, player_b, score_a, score_b), align="center", font=("Arial", 24, "normal"))
        if score_a == 5:
            final_score_a()


    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1 
        score_b += 1
        pen.clear()
        pen.write("{} has {} {} has {}".format(player_a, player_b, score_a, score_b), align="center", font=("Arial", 24, "normal"))
        if score_b == 5:
            final_score_b()

    #paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340) 
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340) 
        ball.dx *= -1

