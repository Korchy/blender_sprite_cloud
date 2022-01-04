# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_sprite_cloud/

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class SPRITE_CLOUD_PT_panel(Panel):
    bl_idname = 'SPRITE_CLOUD_PT_panel'
    bl_label = 'Sprite Cloud'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SpCl'

    def draw(self, context):
        self.layout.operator(
            operator='sprite_cloud.mark_sprite',
            icon='IMAGE_REFERENCE'
        )
        self.layout.operator(
            operator='sprite_cloud.remove_from_sprites',
            icon='CANCEL'
        )


def register():
    register_class(SPRITE_CLOUD_PT_panel)


def unregister():
    unregister_class(SPRITE_CLOUD_PT_panel)
