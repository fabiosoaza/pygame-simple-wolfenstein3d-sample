from sprite_object import *
from random import choices, randrange


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = SPRITES_PATH + '/static_sprites/'
        self.anim_sprite_path = SPRITES_PATH + '/animated_sprites/'
        add_sprite = self.add_sprite

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

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
