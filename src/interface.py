import pygame


def render_text(font, text, color="black", bg_color="white"):
    return font.render(text, True, color, bg_color)


class Button:
    def __init__(self, preloaded_content, x, y, on_trigger, active=True):
        self.x = x
        self.y = y
        self.rect = preloaded_content.get_rect(topleft=(x, y))
        self.active = active
        self.preloaded_content = preloaded_content
        self.on_trigger = on_trigger

    def update(self, screen, mouse_pos):
        screen.blit(self.preloaded_content, (self.x, self.y))
        if self.rect.collidepoint(mouse_pos) and self.active:
            self.on_trigger()
