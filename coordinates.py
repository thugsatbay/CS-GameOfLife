class life:


	#Finds Neighbour Of Each Pixel
	def boundaryScore(self,ls,a,b,r,c):
		orgX,orgY=a,b
		score=0
		#Top Left
		a,b=a-1,b-1
		if a>=0 and b>=0:
			score=score+ls[a][b]
		
		#Top
		a,b=a+1,b+1
		a,b=a-1,b
		if a>=0:
			score=score+ls[a][b]

		#Top Right
		a,b=a+1,b
		a,b=a-1,b+1
		if a>=0 and b<c:
			score=score+ls[a][b]
		
		#Right
		a,b=a+1,b-1
		a,b=a,b+1
		if b<c:
			score=score+ls[a][b]
		
		#Bottom Right
		a,b=a,b-1
		a,b=a+1,b+1
		if a<r and b<c:
			score=score+ls[a][b]
		
		#Bottom
		a,b=a-1,b-1
		a,b=a+1,b
		if a<r:
			score=score+ls[a][b]
		
		#Bottom Left
		a,b=a-1,b
		a,b=a+1,b-1
		if a<r and b>=0:
			score=score+ls[a][b]
		
		#Left
		a,b=a-1,b+1
		a,b=a,b-1
		if b>=0:
			score=score+ls[a][b]
		
		return score


	#Conways Game Of Life Rules
	def newLife(self,neighbour,state):
		if neighbour<2:
			return 0
		if neighbour>=2 and neighbour<=3 and state==1:
			return 1
		if neighbour>=4:
			return 0
		if neighbour==3 and state==0:
			return 1
		return 0


	#Update Screen FrameWork
	def updatePoints(self,oldPixelMap,r,c):
		newPixelMap = [ [0]*c for x in xrange(r) ]
		for x in xrange(r):
			for y in xrange(c):
				#Find Neighbours Of Each Pixel
				neighbour=self.boundaryScore(oldPixelMap,x,y,r,c)
				newPixelMap[x][y]=self.newLife(neighbour,oldPixelMap[x][y])
		for x in xrange(r):
			for y in xrange(c):
				if x==0:
					newPixelMap[x][y]=0
				if y==0:
					newPixelMap[x][y]=0
				if y==c-1:
					newPixelMap[x][y]=0
				if x==r-1:
					newPixelMap[x][y]=0
		return newPixelMap


	def assignGliderGunValues(self,tempX,tempY,pixelMap):
		pixelMap[tempX+5][tempY+1]=1
		pixelMap[tempX+5][tempY+2]=1
		pixelMap[tempX+6][tempY+1]=1
		pixelMap[tempX+6][tempY+2]=1
		pixelMap[tempX+5][tempY+11]=1
		pixelMap[tempX+6][tempY+11]=1
		pixelMap[tempX+7][tempY+11]=1
		pixelMap[tempX+8][tempY+12]=1
		pixelMap[tempX+4][tempY+12]=1
		pixelMap[tempX+3][tempY+13]=1
		pixelMap[tempX+3][tempY+14]=1
		pixelMap[tempX+9][tempY+13]=1
		pixelMap[tempX+9][tempY+14]=1
		pixelMap[tempX+6][tempY+15]=1
		pixelMap[tempX+4][tempY+16]=1
		pixelMap[tempX+8][tempY+16]=1
		pixelMap[tempX+5][tempY+17]=1
		pixelMap[tempX+6][tempY+17]=1
		pixelMap[tempX+7][tempY+17]=1
		pixelMap[tempX+6][tempY+18]=1
		pixelMap[tempX+3][tempY+21]=1
		pixelMap[tempX+4][tempY+21]=1
		pixelMap[tempX+5][tempY+21]=1
		pixelMap[tempX+3][tempY+22]=1
		pixelMap[tempX+4][tempY+22]=1
		pixelMap[tempX+5][tempY+22]=1
		pixelMap[tempX+2][tempY+23]=1
		pixelMap[tempX+6][tempY+23]=1
		pixelMap[tempX+2][tempY+25]=1
		pixelMap[tempX+6][tempY+25]=1
		pixelMap[tempX+1][tempY+25]=1
		pixelMap[tempX+7][tempY+25]=1
		pixelMap[tempX+3][tempY+35]=1
		pixelMap[tempX+4][tempY+36]=1
		pixelMap[tempX+3][tempY+36]=1
		pixelMap[tempX+4][tempY+35]=1
		return pixelMap	
