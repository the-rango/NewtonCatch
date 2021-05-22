import pygame
import random
pygame.init()
wn = pygame.display.set_mode((500,500))

# load the font
font = pygame.font.Font('COMIC.TTF', 50)

nx = 225
newton = pygame.image.load("newton.png")

score = 0
gameon = True

applex = random.randint(0,500)
appley = 10

lives = 3

while gameon:
  # Describes 1 frame of the game
  wn.fill((0,0,0))
  pygame.time.delay(20)

  # Make newton Move
  pygame.event.pump()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a] and nx > 0:
    nx -= 5
  if keys[pygame.K_d] and nx < 450:
    nx += 5

  # Display newton
  wn.blit(newton, (nx,450))

  # Display apple
  pygame.draw.circle(wn, (250,0,0), (applex,appley), 10)

  # Make the apple fall
  appley += (6 + score)
  if appley > 500:
    # Apple is now off the screen
    # and Newton did not catch it
    applex = random.randint(0,500)
    appley = 10
    lives -= 1

  # Catch the apple
  if nx < applex < nx+50 and appley > 450:
    score += 1
    applex = random.randint(0,500)
    appley = 10

  # IS the player still alive?
  if lives == 0:
    gameon = False
    
  # Draw lives
  if lives == 3:
    pygame.draw.circle(wn, (210,50,50), (50,50), 20)
    pygame.draw.circle(wn, (210,50,50), (100,50), 20)
    pygame.draw.circle(wn, (210,50,50), (150,50), 20)
  elif lives == 2:
    pygame.draw.circle(wn, (210,50,50), (50,50), 20)
    pygame.draw.circle(wn, (210,50,50), (100,50), 20)
  elif lives == 1:
    pygame.draw.circle(wn, (210,50,50), (50,50), 20)


  # Display score
  text = font.render(str(score), True, (150,50,50), (0,0,0))
  wn.blit(text, (450,5))

  pygame.display.update()

print("Your score was",score)
