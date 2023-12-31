from sprite_object import *
from random import choices, randrange
from npc import *
import pygame as pg


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = SPRITES_PATH + '/npc/'
        self.static_sprite_path = SPRITES_PATH + '/static_sprites/'
        self.anim_sprite_path = SPRITES_PATH + '/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # sprite map
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'candlebra.png', pos=(10.5, 3.5))),
        # sprite map
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(11.5, 3.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(14.5, 4.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 12.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 20.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(10.5, 20.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5, 14.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5, 18.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(14.5, 24.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(14.5, 30.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(1.5, 30.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'green_light/0.png', pos=(1.5, 24.5)))

        #add_npc(NPC(game))
        #add_npc(NPC(game, pos=(11.5, 4.5)))
        # spawn npc
        self.enemies = ENEMIES_SPAWN_COUNT  # npc count
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()


    def spawn_npc(self):
        for i in range(self.enemies):
                npc = choices(self.npc_types, self.weights)[0]
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                    pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, npc):
        self.npc_list.append(npc)
