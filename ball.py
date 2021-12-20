import pygame,os,time,random 

class Ball():
	def __init__(self,x,y,r,master,color):
		self.x = x 
		self.y = y 
		self.r = r 
		self.color = color
		self.master = master
		self.vx = random.randint(0,4) - 2
		self.vy = random.randint(0,4) - 2
		while self.vx == 0 or self.vy == 0:
			self.vx = random.randint(0,4) - 2
			self.vy = random.randint(0,4)
	def draw(self):
		pygame.draw.circle(self.master,self.color,(self.x,self.y),self.r)
	def move(self,dt,cw,ch):
		self.current_w = cw
		self.current_h = ch
		self.x += self.vx*dt
		self.y += self.vy*dt
		if self.x - self.r < 0:
			self.x = self.r
			self.vx *= -1
		elif self.x + self.r > self.current_w:
			self.x = self.current_w - self.r
			self.vx *= -1
		if self.y - self.r < 0:
			self.y = self.r
			self.vy *= -1
		elif self.y + self.r > self.current_h:
			self.y = self.current_h - self.r
			self.vy *= -1