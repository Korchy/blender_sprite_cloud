# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_sprite_cloud/

from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .sprite_cloud import SpriteCloud


class SPRITE_CLOUD_OT_mark_sprite(Operator):
    bl_idname = 'sprite_cloud.mark_sprite'
    bl_label = 'Mark selection as Sprites'
    bl_description = 'Mark selected objects as Sprites'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        SpriteCloud.mark_sprite(
            objects=context.selected_objects
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)


class SPRITE_CLOUD_OT_remove_from_sprites(Operator):
    bl_idname = 'sprite_cloud.remove_from_sprites'
    bl_label = 'Remove from Sprites'
    bl_description = 'Remove selected objects from Sprites'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        SpriteCloud.remove_from_sprites(
            objects=context.selected_objects
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bool(context.selected_objects)


def register():
    register_class(SPRITE_CLOUD_OT_mark_sprite)
    register_class(SPRITE_CLOUD_OT_remove_from_sprites)


def unregister():
    unregister_class(SPRITE_CLOUD_OT_remove_from_sprites)
    unregister_class(SPRITE_CLOUD_OT_mark_sprite)
