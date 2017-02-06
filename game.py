import pygame
import os
import coordinates as cood


#COLORS
BLACK=(0,0,0)
BLUE=(0,0,255)
SILVER=(200,200,200)
GREEN=(0,255,0)
RED=(255,0,0)
WHITE=(255,255,255)
ORANGE=(250,90,60)
#red = (200,0,0)
BUTTONGREEN = (0,200,0)
YELLOW = (255,255,0)
BUTTONBRIGHTGREEN = (0,255,0)


#Initial Size Values
width=800
height=600
boxSize=20
rows=(height/boxSize)*5
columns=(width/boxSize)*5
menuBarSize=25
lineWidth=1
frameSpeed=60
informationText=200


#CONFIG
backColor=WHITE
cellColor=GREEN
boundaryColor=BLACK
caption="Game Of Life"


#Boxes Of Game Of Life
pixelMap = [ [0]*columns for x in xrange(rows) ]



#INIT
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (25,50)
pygame.init()
myfont = pygame.font.SysFont('Arial Black', 10) #creates the font, size 15 (you can change this)
startLabel = myfont.render("START", 1, BLACK) #creates the label
stopLabel = myfont.render("PAUSE", 1, BLACK) #creates the label
resetLabel = myfont.render("RESET", 1, BLACK) #creates the label
resetText= myfont.render("Board Reset", 1, BLUE) #creates the label
runningText= myfont.render("Running", 1, BLUE) #creates the label
initText= myfont.render("Creating", 1, BLUE) #creates the label
gliderGun= myfont.render("Glider Gun", 1, BLUE) #creates the label
size=(width,height+menuBarSize)
screen=pygame.display.set_mode(size)
pygame.display.set_caption(caption)
colorFlag=True #Color Flag
gameStartFlag=False #Game Start Flag
done=False #Game Quit Loop


clock=pygame.time.Clock()#Adjust Frames
screen.fill(backColor)
for x in range(-boxSize,height,boxSize):
	pygame.draw.line(screen,boundaryColor,[0,20+x],[width,20+x],lineWidth)
for x in range(-boxSize,width,boxSize):	
	pygame.draw.line(screen,boundaryColor,[20+x,0],[20+x,height],lineWidth)


#print "Rows And Column Grid For Game Of Life",rows,columns
#Flip Coordinates Object
gamelf=cood.life()

#Game Loop
while not done:

	# --- Main event loop
	mouse=pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			if mouse[1]>height+2 and mouse[1]<height+22 and mouse[0]>10 and mouse[0]<60:
				gameStartFlag=True
			if mouse[1]>height+2 and mouse[1]<height+22 and mouse[0]>100 and mouse[0]<150:
				screen.blit(resetText, (200, height+6))
				for x in xrange(rows):
					for y in xrange(columns):
						pixelMap[x][y]=0
			if mouse[1]>height+2 and mouse[1]<height+22 and mouse[0]>width-150 and mouse[0]<width-50:
					tempX=((rows/5)*2)
					tempY=(columns/5)*2
					pixelMap=gamelf.assignGliderGunValues(tempX,tempY,pixelMap)
			if mouse[1]>0 and mouse[1]<height:
				#screen.blit(initText, (200, height+6))
				pygame.draw.rect(screen,WHITE,[195,height+2,100,20],0)
				tempX=int((mouse[1]+1)/boxSize)+((rows/5)*2)
				tempY=int((mouse[0]-1)/boxSize)+((columns/5)*2)
				print "Clicked On",tempX,tempY
				if pixelMap[tempX][tempY]==0:
					pixelMap[tempX][tempY]=1
				else:
					pixelMap[tempX][tempY]=0



	#Bottom Screen Menu
	pygame.draw.rect(screen,BUTTONGREEN,[10,height+2,50,20],0)
	pygame.draw.rect(screen,RED,[100,height+2,50,20],0)
	pygame.draw.rect(screen,BUTTONBRIGHTGREEN,[width-150,height+2,100,20],0)
	if mouse[1]>height+2 and mouse[1]<height+22 and mouse[0]>10 and mouse[0]<60:
		pygame.draw.rect(screen,YELLOW,[12,height+4,46,16],0)
	else:
		pygame.draw.rect(screen,BUTTONBRIGHTGREEN,[12,height+4,46,16],0)
	screen.blit(startLabel, (16, height+6))
	screen.blit(resetLabel, (106, height+6))
	screen.blit(gliderGun, (width-140, height+6))

	#Initial Config:
	cellColor=GREEN
	colorFlag=True
	for x in range((rows/5)*2,(rows/5)*3):
		for y in range((columns/5)*2,(columns/5)*3):
			if pixelMap[x][y]==1:
				pygame.draw.rect(screen,cellColor,[((y-((columns/5)*2))*boxSize)+lineWidth,((x-((rows/5)*2))*boxSize)+lineWidth,boxSize-lineWidth,boxSize-lineWidth],0)		
			else:
				pygame.draw.rect(screen,backColor,[((y-((columns/5)*2))*boxSize)+lineWidth,((x-((rows/5)*2))*boxSize)+lineWidth,boxSize-lineWidth,boxSize-lineWidth],0)
	

	#Update Screen
	pygame.display.flip()
	#Control Frame Spee
	clock.tick(frameSpeed)


	while gameStartFlag:
		mouse=pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameStartFlag=False
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if mouse[1]>height+2 and mouse[1]<height+22 and mouse[0]>10 and mouse[0]<60:
					gameStartFlag=False


		#Bottom Screen Menu
		pygame.draw.rect(screen,BUTTONGREEN,[10,height+2,50,20],0)
		if mouse[1]>height+2 and mouse[1]<height+22 and mouse[0]>10 and mouse[0]<60:
			pygame.draw.rect(screen,YELLOW,[12,height+4,46,16],0)
		else:
			pygame.draw.rect(screen,BUTTONBRIGHTGREEN,[12,height+4,46,16],0)
		screen.blit(stopLabel, (16, height+6))


		if colorFlag:
			cellColor=ORANGE
			colorFlag=False
		else:
			cellColor=GREEN
			colorFlag=True


		pixelMap=gamelf.updatePoints(pixelMap,rows,columns)
		for x in range((rows/5)*2,(rows/5)*3):
			for y in range((columns/5)*2,(columns/5)*3):
				if pixelMap[x][y]==1:
					pygame.draw.rect(screen,cellColor,[((y-((columns/5)*2))*boxSize)+lineWidth,((x-((rows/5)*2))*boxSize)+lineWidth,boxSize-lineWidth,boxSize-lineWidth],0)
				else:
					pygame.draw.rect(screen,backColor,[((y-((columns/5)*2))*boxSize)+lineWidth,((x-((rows/5)*2))*boxSize)+lineWidth,boxSize-lineWidth,boxSize-lineWidth],0)

		pygame.display.flip()
		clock.tick(frameSpeed)
		#Alternate Color
		
		
		#insideLoop=True
		#print pixelMap[2][1],pixelMap[2][2],pixelMap[2][3]
		#gameStartFlag=False
# Close the window and quit.
pygame.quit()