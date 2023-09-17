import pygame
from vars import *


def render_text(font, text, color="black", bg_color="white"):
    if text != "0":
        return font.render(text, True, color, bg_color)
    else:
        return font.render("", True, color, bg_color)


class Button:
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

    def draw(self, screen):
        if self.active:
            screen.blit(
                self.preloaded_content,
                (
                    self.rect.centerx,
                    self.rect.y + ((HEIGHT - START) // TILES[self.dif][0][1]) / 4,
                ),
            )
