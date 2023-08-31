import pygame
import sys
import random
from gameObject import GameObject
from setting import Setting
from gameTime import GameTime
from timeOver import TimeOver
from restart import Restart

# Pygame 초기화
pygame.init()
setting = Setting()
game_Time = GameTime()


# 물체들 생성
sharks = []
octopuses = []
ships = []

for _ in range(5):
    sharks.append(GameObject("venv/lib/images/shark.png", 100, (-30, 30), 50))

for _ in range(5):
    octopuses.append(GameObject("venv/lib/images/octopus.png", 80, (-15, 15), 50))

for _ in range(5):
    ships.append(GameObject("venv/lib/images/boat.png", 150, (-5, 5), 30))



# 스나이퍼 초기 위치
sniper_radius = 80
sniper_x = setting.screen_width // 2
sniper_y = setting.screen_height // 2
sniper_speed = 35


# 검은색 동그라미 생성
black = (0, 0, 0)
black_circle = pygame.Surface((sniper_radius * 2, sniper_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(black_circle, (0, 0, 0), (sniper_radius, sniper_radius), sniper_radius)

# 게임 루프
running = True
pos = (0, 0)

restart_button_visible = False  # Restart 버튼 보이기 여부 설정


# 점수 변수 초기화
score = 0

clock = pygame.time.Clock()  # Clock 객체 생성


while running:

    # 시간 체크
    game_Time.checkTime()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                setting.bang_sound.play()

                for shark in sharks:
                    if shark.rect.collidepoint(sniper_x, sniper_y):
                        print("Shark hit!")
                        setting.shark_sound.play()
                        score += 50
                        shark.rect.x = random.randint(shark.size, setting.screen_width - shark.size)
                        shark.rect.y = random.randint(shark.size, setting.screen_height - shark.size)

                for octopus in octopuses:
                    if octopus.rect.collidepoint(sniper_x, sniper_y):
                        print("Octopus hit!")
                        setting.octopus_sound.play()
                        score += 40
                        octopus.rect.x = random.randint(octopus.size, setting.screen_width - octopus.size)
                        octopus.rect.y = random.randint(octopus.size, setting.screen_height - octopus.size)

                for ship in ships:
                    if ship.rect.collidepoint(sniper_x, sniper_y):
                        print("Boat hit!")
                        setting.boat_sound.play()
                        score += 30
                        ship.rect.x = random.randint(ship.size, setting.screen_width - ship.size)
                        ship.rect.y = random.randint(ship.size, setting.screen_height - ship.size)

    keys = pygame.key.get_pressed()

    # 스나이퍼 이동
    if keys[pygame.K_LEFT] and sniper_x - sniper_radius > 0:
        sniper_x -= sniper_speed
    if keys[pygame.K_RIGHT] and sniper_x + sniper_radius < setting.screen_width:
        sniper_x += sniper_speed
    if keys[pygame.K_UP] and sniper_y - sniper_radius > 0:
        sniper_y -= sniper_speed
    if keys[pygame.K_DOWN] and sniper_y + sniper_radius < setting.screen_height:
        sniper_y += sniper_speed

    pos = (sniper_x, sniper_y)

    # 물체들의 위치 업데이트
    for shark in sharks:
        shark.rect.x += shark.speed_x
        shark.rect.y += shark.speed_y
        if shark.rect.x < 0 or shark.rect.x > setting.screen_width - shark.size:
            shark.speed_x *= -1
        if shark.rect.y < 0 or shark.rect.y > setting.screen_height - shark.size:
            shark.speed_y *= -1

    for octopus in octopuses:
        octopus.rect.x += octopus.speed_x
        octopus.rect.y += octopus.speed_y
        if octopus.rect.x < 0 or octopus.rect.x > setting.screen_width - octopus.size:
            octopus.speed_x *= -1
        if octopus.rect.y < 0 or octopus.rect.y > setting.screen_height - octopus.size:
            octopus.speed_y *= -1

    for ship in ships:
        ship.rect.x += ship.speed_x
        ship.rect.y += ship.speed_y
        if ship.rect.x < 0 or ship.rect.x > setting.screen_width - ship.size:
            ship.speed_x *= -1
        if ship.rect.y < 0 or ship.rect.y > setting.screen_height - ship.size:
            ship.speed_y *= -1

    # 배경 이미지 그리기
    setting.screen.blit(setting.background_image, (0, 0))

    # 물체 이미지 그리기
    for shark in sharks:
        setting.screen.blit(shark.image, shark.rect)

    for octopus in octopuses:
        setting.screen.blit(octopus.image, octopus.rect)

    for ship in ships:
        setting.screen.blit(ship.image, ship.rect)

    for i in range(0, setting.screen_width):
        for j in range(0, setting.screen_height):
            if (sniper_x - sniper_radius < i and i < sniper_x + sniper_radius) and (
                    sniper_y - sniper_radius < j and j < sniper_y + sniper_radius):
                continue
            else:
                pygame.draw.circle(setting.screen, black, (i, j), 1)

    # 스나이퍼 초점
    pygame.draw.circle(setting.screen, (255, 0, 0), (sniper_x, sniper_y), 5)


    # 점수 표시
    font = pygame.font.Font(None, 60)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    setting.screen.blit(score_text, (10, 10))  # 좌상단에 점수 표시


    # 시간 박스 그리기
    pygame.draw.rect(setting.screen, game_Time.time_box_color, game_Time.time_box_rect)
    setting.screen.blit(game_Time.time_rendered, (setting.screen_width - 190, 20))  # 시간 텍스트 위치

    # 화면 업데이트
    pygame.display.flip()

    # 시간이 초과되었는지 확인
    if game_Time.elapsed_time >= game_Time.time_limit:
        running = False  # 게임 종료


        # TimeOver 화면
        timeOver = TimeOver(score)
        setting.screen.blit(timeOver.game_Time_over_text, (timeOver.text_x, timeOver.text_y))
        setting.screen.blit(score_text, (timeOver.score_x, timeOver.score_y))

        # Restart 버튼 그리기
        restart = Restart(score)
        setting.screen.blit(restart.restart_text, restart.restart_text_rect)
        restart_button_visible = True

        pygame.display.flip()
        # 대기 상태에서 종료할 때까지 대기

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 왼쪽 마우스 버튼 클릭
                        if restart.restart_button_rect.collidepoint(event.pos):
                            # 게임을 재시작
                            score = 0
                            game_Time.start_time = pygame.time.get_ticks()
                            game_Time.current_time = game_Time.time_limit
                            sharks = []
                            octopuses = []
                            ships = []
                            for _ in range(5):
                                sharks.append(GameObject("venv/lib/images/shark.png", 100, (-30, 30), 50))
                            for _ in range(5):
                                octopuses.append(GameObject("venv/lib/images/octopus.png", 80, (-15, 15), 50))
                            for _ in range(5):
                                ships.append(GameObject("venv/lib/images/boat.png", 150, (-5, 5), 30))
                            sniper_x = setting.screen_width // 2
                            sniper_y = setting.screen_height // 2
                            running = True
                            waiting = False


    clock.tick(10)  # FPS 설정 (여기서는 10 FPS)



# Pygame 종료
pygame.quit()
sys.exit()
