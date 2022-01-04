# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_sprite_cloud/

from . import sprite_cloud_props
from . import sprite_cloud_ops
from . import sprite_cloud_ui
from .addon import Addon


bl_info = {
    'name': 'sprite_cloud',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 93, 0),
    'location': '3D Viewport - N panel - SpCl tab',
    'doc_url': 'https://b3d.interplanety.org/en/',
    'tracker_url': 'https://b3d.interplanety.org/en/',
    'description': 'Simple managing sprites'
}


def register():
    if not Addon.dev_mode():
        sprite_cloud_props.register()
        sprite_cloud_ops.register()
        sprite_cloud_ui.register()
    else:
        print('It seems you are trying to use the dev version of the '
           + bl_info['name']
           + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        sprite_cloud_ui.unregister()
        sprite_cloud_ops.unregister()
        sprite_cloud_props.unregister()


if __name__ == '__main__':
    register()
