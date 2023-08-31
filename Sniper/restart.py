import pygame
import pygame
from setting import Setting
from timeOver import TimeOver

setting = Setting()

class Restart:
    def __init__(self, score):
        timeOver = TimeOver(score)
        self.restart_button_rect = pygame.Rect(setting.screen_width // 2 - 100, timeOver.score_y + 50, 200, 50)
        pygame.draw.rect(setting.screen, (0, 255, 0), self.restart_button_rect)  # 수정된 부분
        self.restart_font = pygame.font.Font(None, 40)
        self.restart_text = self.restart_font.render("Restart", True, (0, 0, 0))
        self.restart_text_rect = self.restart_text.get_rect(center=self.restart_button_rect.center)


