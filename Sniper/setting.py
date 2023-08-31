import pygame

class Setting:

    def __init__(self):

        # 화면 설정
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Sniper Game")

        # "바닷속.jpg" 이미지 로드
        self.background_image = pygame.image.load("venv/lib/images/underwater2.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))

        # 사운드 로드
        pygame.mixer.init()
        self.bang_sound = pygame.mixer.Sound("venv/lib/sound/gun.wav")  # 사운드 파일 이름에 맞게 수정
        self.shark_sound = pygame.mixer.Sound("venv/lib/sound/shark.wav")
        self.octopus_sound = pygame.mixer.Sound("venv/lib/sound/octopus.wav")
        self.boat_sound = pygame.mixer.Sound("venv/lib/sound/boat.wav")

        # 볼륨 설정
        self.bang_sound.set_volume(1.0)  # 0.0부터 1.0 사이의 값으로 볼륨 설정
        self.shark_sound.set_volume(1.0)
        self.octopus_sound.set_volume(1.0)
        self.boat_sound.set_volume(1.0)