# Jogo do pong
# Francisco Vicente 20/06/2021

import turtle
#import winsound

wn = turtle.Screen()          # comando para opcoes do screen
wn.title ("Bem-vindo ao jogo do Pong")
wn.bgcolor("black")           # background do jogo
wn.setup(width=800,height=600)   # medidas do ecra
wn.tracer(0)

#Golo
resul_a = 0
resul_b = 0

#plataforma A

paddle_a = turtle.Turtle()    # classe Turtle e modulo turtle
paddle_a.speed(0)    # animaçao plataforma
paddle_a.shape("square")  #forma da plataforma
paddle_a.color("blue")    #cor da plataforma
paddle_a.shapesize(stretch_wid=5,stretch_len=1)  #dimensoes da plataforma
paddle_a.penup() # para nao chocar com as bordas do window
paddle_a.goto(-350,0)  #posicao da plataforma

#plataforma b

paddle_b = turtle.Turtle()    # classe Turtle e modulo turtle
paddle_b.speed(0)    # animaçao plataforma
paddle_b.shape("square")  #forma da plataforma
paddle_b.color("red")    #cor da plataforma
paddle_b.shapesize(stretch_wid=5,stretch_len=1)  #dimensoes da plataforma
paddle_b.penup() # para nao chocar com as bordas do window
paddle_b.goto(350,0)  #posicao da plataforma

#bola
bola = turtle.Turtle()    # classe Turtle e modulo turtle
bola.speed(0)    # animaçao bola
bola.shape("square")  #forma da bola
bola.color("white")    #cor da bola
bola.penup() # para nao chocar com as bordas do window
bola.goto(0,0)  #posicao da bola
bola.dx=0.20
bola.dy=-0.20

#score
score = turtle.Turtle()
score.speed(0)
score.color("Green")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write ("Player1:0   Player2:0", align="center", font=("Courier", 24,  "normal"))

#funcao para mover a plataforma a para cima
def paddle_a_mover_up():
    y = paddle_a.ycor() #le as coordenadas de y
    y += 20            # acrescenta mais 20 pixes
    paddle_a.sety(y)   # faz o set

#funcao para mover a plataforma a para baixo
def paddle_a_mover_dwon():
    y = paddle_a.ycor() #le as coordenadas de y
    y -= 20            # acrescenta mais 20 pixes
    paddle_a.sety(y)   # faz o set

#funcao para mover a plataforma b para a cima
def paddle_b_mover_up():
    y = paddle_b.ycor() #le as coordenadas de y
    y += 20            # acrescenta mais 20 pixes
    paddle_b.sety(y)   # faz o set

#funcao para mover a plataforma b para a baixo
def paddle_b_mover_dwon():
    y = paddle_b.ycor() #le as coordenadas de y
    y -= 20            # acrescenta mais 20 pixes
    paddle_b.sety(y)   # faz o set



# teclas lidas pelo teclado
wn.listen()
wn.onkeypress(paddle_a_mover_up, "w")
wn.onkeypress(paddle_a_mover_dwon, "s")
wn.onkeypress(paddle_b_mover_up, "Up")
wn.onkeypress(paddle_b_mover_dwon, "Down")


#Loop do jogo
while True:
    wn.update()

    #mover a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #limites segundo y top e down
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        #winsound.PlaySound("bounce.wav",winsound.SND_ASYNC )

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    #a bola volta ao meio quando e golo na direçao oposta
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        resul_a += 1
        score.clear()
        score.write("Player1:{}   Player2:{}".format(resul_a, resul_b), align="center", font=("Courier", 24, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        resul_b += 1
        score.clear()
        score.write("Player1:{}   Player2:{}".format(resul_a, resul_b), align="center", font=("Courier", 24, "normal"))

    #colisao da bola com a plataforma
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < paddle_b.ycor() + 40 and bola.ycor() > paddle_b.ycor() -40):
       bola.setx(340)
       bola.dx *=-1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < paddle_a.ycor() + 40 and bola.ycor() > paddle_a.ycor() -40):
       bola.setx(-340)
       bola.dx *=-1