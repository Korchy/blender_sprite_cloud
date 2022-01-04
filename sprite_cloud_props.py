# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_sprite_cloud/

from bpy.props import BoolProperty
from bpy.types import Object
from .sprite_cloud import SpriteCloud


def register():
    Object.is_sprite = BoolProperty(
         name='Is Sprite',
         default=False,
         update=lambda self, context: SpriteCloud.on_update_sprite_status(
             context=context,
             obj=self
         )
    )


def unregister():
    del Object.is_sprite
