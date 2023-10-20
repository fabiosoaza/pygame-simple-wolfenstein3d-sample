import pygame as pg
import sys
from settings import *
from levels import *
from map import *
from player import *
from raycasting import *
from object_renderer import *

from object_handler import *
from weapon import *
from sound import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(MOUSE_VISIBLE)

        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)

    def new_game(self):
        self.map = Map(self, MINI_MAP)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.static_sprite = SpriteObject(self)
        self.animated_sprite = AnimatedSprite(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):
        self.screen.fill('black')
        if MODE_2D is False:
            self.object_renderer.draw()
            self.weapon.draw()
        else:
            self.map.draw()
            self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit(0)
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
