import pygame,os,time
from ball import*

class Game():
	def __init__(self):
		#Main Window
		pygame.init()
		pygame.font.init()
		self.main_width = 1200
		self.main_height = 700
		self.window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		pygame.display.set_caption("Window")

		#Game Assets
		self.FPS = 240
		self.running = True
		self.paused = False
		self.last_time = time.time()
		self.main_clock = pygame.time.Clock()
		#The Ball is used as a reference to dipict how pausing the Game will stop#
		#a certain function in the Game#
		#In the case of this Ball, pausing the Game will stop only the Ball's#
		#movement but will not stop the diplay of the Ball# 
		self.ball = Ball(500,100,50,self.window,'cyan')
		self.white_image = pygame.image.load("white.png")
		self.black_image = pygame.image.load('black.png')
		#Text
		self.font = pygame.font.Font("font.ttf",50)
		self.resume_text = self.font.render("resume",False,'black')
		self.exit_text = self.font.render("exit",False,'black')

	def game_window(self):
		#Delta Time
		dt = self.last_time - time.time()
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('black')
		self.current_w = self.window.get_width()
		self.current_h = self.window.get_height()
		self.ball.draw()

		#Pause Function
		#Checking if the Player have paused the Game
		if self.paused == True:
			#Transparent White Layer
			self.white = pygame.transform.scale(
				self.white_image,(self.current_w,self.current_h))
			self.white.set_colorkey('black')
			self.white.set_alpha(100)
			self.window.blit(self.white,(0,0))
			clicked = False
			mouse_pos = pygame.mouse.get_pos()
			#Resume Button
			self.resume_rect = pygame.Rect(
				self.current_w-self.resume_text.get_width()-5,5,
				self.resume_text.get_width(),self.resume_text.get_height())
			self.window.blit(self.resume_text,(self.resume_rect.x,self.resume_rect.y))
			if self.resume_rect.collidepoint(mouse_pos):
				#Resume Button Outline
				self.black = pygame.transform.scale(self.black_image,
					(self.resume_text.get_width(),self.resume_text.get_height()))
				self.black.set_colorkey('black')
				self.black.set_alpha(100)
				self.window.blit(self.black,(self.resume_rect.x,self.resume_rect.y))
				#Resume Button Clicking Function
				if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
					self.paused = False
					clicked = True
			if pygame.mouse.get_pressed()[0] == 0:
				clicked = False
			#Exit Button
			self.exit_rect = pygame.Rect(
				self.current_w-self.exit_text.get_width()-5,
				self.resume_text.get_height()+10,
				self.exit_text.get_width(),self.exit_text.get_height())
			self.window.blit(self.exit_text,(self.exit_rect.x,self.exit_rect.y))
			#Exit Button Clicking Function
			if self.exit_rect.collidepoint(mouse_pos):
				#Exit Button Outline
				self.black = pygame.transform.scale(self.black_image,
					(self.exit_text.get_width(),self.exit_text.get_height()))
				self.black.set_colorkey('black')
				self.black.set_alpha(100)
				self.window.blit(self.black,(self.exit_rect.x,self.exit_rect.y))
				#Exit Button Clicking Funciton
				if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
					self.running = False
					clicked = True
			if pygame.mouse.get_pressed()[0] == 0:
				clicked = False
		#Checking if the Player have not paused the Game
		if self.paused == False:
			self.ball.move(dt,self.current_w,self.current_h)

		#Events
		for event in pygame.event.get():
			#Exit Event
			if event.type == pygame.QUIT:
				self.running = False
			#FullScreen Events
			if event.type == pygame.KEYUP and event.key == pygame.K_F9:
				pygame.display.set_mode((self.main_width,self.main_height))
			if event.type == pygame.KEYUP and event.key == pygame.K_F10:
				pygame.display.set_mode((0,0),pygame.FULLSCREEN)
			#Pause Game Event
			if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
				if self.paused == True:
					self.paused = False
				elif self.paused == False:
					self.paused = True

		#Updating the Display and Ticking the FPS			
		pygame.display.update()
		self.main_clock.tick(self.FPS)