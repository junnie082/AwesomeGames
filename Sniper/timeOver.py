import pygame
from setting import Setting
from gameTime import GameTime

setting = Setting()
game_Time = GameTime()
font = pygame.font.Font

class TimeOver:
    def __init__(self, score):
        # "Time Over!" 문구와 내 점수 표시
        self.font = pygame.font.Font(None, 80)
        self.game_Time_over_text = self.font.render("Time Over!", True, (255, 0, 0))  # 빨간색 글씨로 렌더링
        self.score_text = self.font.render("Score: " + str(score), True, (255, 0, 0))  # 빨간색 글씨로 렌더링
        self.text_x = setting.screen_width // 2 - self.game_Time_over_text.get_width() // 2
        self.text_y = setting.screen_height // 2 - self.game_Time_over_text.get_height() // 2 - 30
        self.score_x = setting.screen_width // 2 - self.score_text.get_width() // 2 + 40
        self.score_y = self.text_y + self.game_Time_over_text.get_height() + 20

