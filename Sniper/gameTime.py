import pygame
from setting import Setting

setting = Setting()
class GameTime:
    def __init__(self):
        # 시간 변수 초기화
        self.start_time = pygame.time.get_ticks()  # 현재 시간(ms) 가져오기
        #self.time_limit = 180 * 1000  # 3분을 밀리초로 변환
        # 테스트용 시간:
        self.time_limit = 60 * 1000
    def checkTime(self):
        # 시간 체크
        self.current_time = pygame.time.get_ticks()
        self.elapsed_time = self.current_time - self.start_time
        self.remaining_time = max(0, self.time_limit - self.elapsed_time)
        self.seconds = self.remaining_time // 1000
        self.minutes = self.seconds // 60
        self.seconds %= 60
        self.time_text = f"{self.minutes:02d}:{self.seconds:02d}"
        self.time_font = pygame.font.Font(None, 40)
        self.time_rendered = self.time_font.render(self.time_text, True, (255, 0, 0))  # 빨간색 글씨로 렌더링
        self.time_box_color = (255, 255, 0)  # 노란색
        self.time_box_rect = pygame.Rect(setting.screen_width - 200, 10, 190, 50)