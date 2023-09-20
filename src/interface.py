import pygame
from vars import *


def render_text(font, text, color="black", bg_color="white"):
    if text == "0":
        return font.render("", True, color, bg_color)

    return font.render(text, True, color, bg_color)


class Button:
    def __init__(
        self,
        preloaded_content,
        x,
        y,
        when_triggered,
        func_args: tuple = (),
        active=True,
    ):
        self.rect = preloaded_content.get_rect(center=(x, y))
        self.active = active
        self.preloaded_content = preloaded_content
        self.when_triggered = when_triggered
        self.func_args = func_args

    def draw(self, screen):
        screen.blit(self.preloaded_content, self.rect.topleft)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos) and self.active:
            if self.func_args:
                self.when_triggered(*self.func_args)
                return True
            else:
                self.when_triggered()
                return True
        return False


class TileButton:
    def __init__(
        self,
        preloaded_content,
        rect,
        dif,
        active=True,
    ):
        self.rect = rect
        self.active = active
        self.preloaded_content = preloaded_content
        self.dif = dif

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.active = True
            return True
        return False

    def force_update(self):
        self.active = True
        return True

    def draw(self, screen):
        if self.active:
            screen.blit(
                self.preloaded_content,
                (
                    self.rect.centerx,
                    self.rect.y + ((HEIGHT - START) // TILES[self.dif][0][1]) / 4,
                ),
            )
