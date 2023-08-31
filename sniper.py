import pygame
import sys

#Pygame 초기화
pygame.init()

#화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((sreen_width, screen_height))
pygame.display.set_caption("Sniper Game")

#색상 정의
black = (0, 0, 0)
white = (255, 255, 255)

#스나이퍼 위치 설정
sniper_x = screen_width // 2
sniper_y = screen_height - 50

#게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경 색상 채우기
    screen.fill(black)

    # 스나이퍼 그리기
    pygame.draw.rect(screen, white, (sniper_x, sniper_y, 20, 40))

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
