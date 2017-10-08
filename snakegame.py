# Project 1- Snake Game in python using mainly the module pygame 

import pygame
import sys #helps exit the program
import random #main function is to randomly assign the location of the food for the snake in the screen 
import time   # to measure time for the game over screen

errors_flag=pygame.init() 

if errors_flag[1] >0 : # errors_flag[1] contains the number of errors in the tuple
	print ("(!) Had {0} initalising errors, exiting..." .format(errors_flag[1]))
	sys.exit(-1)
else :
	print ("(+) Pygame succesfully initalised")

#Playing Screen

playScreen = pygame.display.set_mode((720,510))
pygame.display.set_caption('Snake Game Edition: Python ') # supposed to set the name of the window to Snake game 
#time.sleep(5)  # was used to delay the screen during development for debugging purposes 

#Colors to be used later 
red = pygame.Color(255,0,0) # game over 
blue = pygame.Color(0,0,255) #snake
black= pygame.Color(0,0,0) #screen
white = pygame.Color(255,255,255) #score 
pink = pygame.Color(255,153,255) #food

# Frames per second Controller

fps_controller=pygame.time.Clock() # makes sure the screen is not stuck in one frame 

# Game Variables

snakePos = [200,300]  # shows the position of the snake head in the x and y coordinates
snakeBody = [[200,300],[190,300], [180,300]] # list to describe the snake body

foodPos =[random.randrange(1,72) *10, random.randrange(1,51) *10 ] # so the *10 is used because the size of
																	# the snake block is 10 and it needs to be in a psotion %10 ==0 
																	#else the food wont be consumed by the snake
foodSpawn = True; # to see if a food has been spawned or not 

direction = "RIGHT" 
changeto = direction 
speed= 17
score=0

# Gameover function  function 

def gameover():
	myFont = pygame.font.SysFont('Times New Roman', 72, bold=True, italic=False)
	GameOverText = myFont.render("Game Over!" , True, red)
	GameOverRect = GameOverText.get_rect() 
	GameOverRect.midtop = (360,255)  # helps place the game over message in the middle
	playScreen.blit(GameOverText,GameOverRect) 
	showscore(0)
	# fps_controller.tick(1)
	pygame.display.update()
	# pygame.time.delay(500)
	pygame.quit()  #closes the consolose
	sys.exit()	   #quits the program

#show score function 
def showscore(choice):
	#format very similiar to the game over function except there is a choice variable that determines the positio 
	scoreFont = pygame.font.SysFont('Times New Roman', 20, bold=False, italic=False)
	scoreText = scoreFont.render("Score : {0}".format(score) , True, pink)
	scoreRect = scoreText.get_rect()
	if choice == 1:
		scoreRect.midtop = (90,10)
	else:
		scoreRect.midtop = (360,360)
	playScreen.blit(scoreText,scoreRect) 




# Central game code 

while True: #infinite loop 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:   # Note- pygame.QUIT is sent when the user clicks the window's "X" button, 
											   #or when the system 'asks' for the process to quit. If ignored, it can still be killed by the system. It lets you save, before quitting.
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):  # this is to check if a key indicating that snake moved to the right is pressed  similiar checks with be done for left,up and down
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				changeto = 'LEFT' 
			if event.key == pygame.K_UP or event.key == ord('w'):
				changeto = 'UP'
			if  event.key == pygame.K_DOWN or event.key == ord('a'):
				changeto = 'DOWN'
			if  event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))
		    # I initially applied elif but came to the realization that it wont factor in when two buttons are pressed
	    # ok now we have to change the direction of the snake
	    # this has to be done in two parts because a snake moving in one direction cannot turn to the opposite direction immediately without an intermediate steo
	if changeto =='RIGHT' and not direction == 'LEFT' :
		direction = 'RIGHT'
	if changeto =='LEFT' and not direction == 'RIGHT' :
		direction = 'LEFT'
	if changeto =='UP' and not direction == 'DOWN' :
		direction = 'UP'
	if changeto =='DOWN' and not direction == 'UP' :
		direction = 'DOWN' 


	if direction == 'RIGHT':
		snakePos[0] = snakePos[0] + 10
	if direction == 'LEFT':
		snakePos[0] = snakePos[0] - 10
	if direction == 'UP':
		snakePos[1] = snakePos[1] - 10	
	if direction == 'DOWN':
		snakePos[1] = snakePos[1] + 10	

	# in charge of snake body movements

 	snakeBody.insert(0,list(snakePos)) #inserts a block to the snake body
 	#the logic is a two step algorithm, it checks if the head passes through a food block if so it keeps that inserted block else it pops it
 	if(snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1] ):
 		score = score+1;
 		speed = speed +1;
		foodSpawn = False;
	else:
		snakeBody.pop()

	if foodSpawn == False :
		foodPos =[random.randrange(1,72) *10, random.randrange(1,51) *10 ]
	foodSpawn = True; 


	playScreen.fill(black);
	for i in snakeBody:
		pygame.draw.rect(playScreen, blue, pygame.Rect(i[0],i[1],10,10))
	pygame.draw.rect(playScreen, white, pygame.Rect(foodPos[0],foodPos[1],10,10))

	# code to be uncommented iy ou want to apply boundary condition
	#following if condition is to check if the snake hits the boundaries
	# if snakePos[0] > 720 or snakePos[0] < 0 or snakePos[1] >510 or snakePos[1] < 0 :
	# 	gameover()

	#else
	if snakePos[0] > 710 :
		snakePos[0] = 10 #+ snakePos[0] - 720
	elif snakePos[1] > 500:
		snakePos[1] = 10 #+ snakePos[1] - 510
	elif snakePos[0] < 10:
		snakePos[0] = 710 #+ snakePos[0]
	elif snakePos[1] < 10:
		snakePos[1] = 510 #+ snakePos[0]
	#for loop to check if the snake hits itself 
	for head in snakeBody[1:]:
		if head[1] ==snakePos[1] and head[0] ==snakePos[0]:
			gameover()

	showscore(1)
	pygame.display.update()
	fps_controller.tick(speed)


