import pygame


def render_text(font, text, color="black", bg_color="white"):
    return font.render(text, True, color, bg_color)


class Button:
    def __init__(self, preloaded_content, x, y, active=True):
        self.x = x
        self.y = y
        self.rect = preloaded_content.get_rect(topleft=(x, y))
        self.active = active
        self.preloaded_content = preloaded_content

    def draw(self, screen):
        if self.active:
            screen.blit(self.preloaded_content, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos) and self.active:
            return True
        return False
