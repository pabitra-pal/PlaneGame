import pygame
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Play Game...")


plane=pygame.Rect(200,500,40,40)

enemies=[]

clock=pygame.time.Clock()
score=0
running=True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        plane.x -= 5
    if keys[pygame.K_RIGHT]:
        plane.x += 5
    if plane.x < 0:
        plane.x = 0

    if plane.x > WIDTH - plane.width:
        plane.x = WIDTH - plane.width

    if random.randint(1,30) == 1:
        enemies.append(pygame.Rect(random.randint(0, WIDTH-40), 0, 40, 40))
    enemy_speed = 5 + score // 10
    for enemy in enemies[:]:
        enemy.y += enemy_speed

        if enemy.colliderect(plane):
            running = False

        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            score += 1

        pygame.draw.rect(screen, (255,0,0), enemy)

    pygame.draw.rect(screen, (0,255,255), plane)

    pygame.display.set_caption(f"Score: {score}")

    pygame.display.update()
    clock.tick(60)

# Game Over screen
font = pygame.font.Font(None, 50)

game_over_text = font.render("Game Over!", True, (255, 0, 0))
score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))

screen.fill((0, 0, 0))
screen.blit(game_over_text, (WIDTH//2 - 120, HEIGHT//2 - 50))
screen.blit(score_text, (WIDTH//2 - 140, HEIGHT//2 + 10))

pygame.display.update()

pygame.time.wait(3000)  # Show for 3 seconds

pygame.quit()