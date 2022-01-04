# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_sprite_cloud/

import bpy
from bpy.app.handlers import persistent, depsgraph_update_post
from bpy.types import Scene


class SpriteCloud:

    track_constraint_name = 'sprite_cloud_track'
    active_camera_marker = None

    @staticmethod
    def mark_sprite(objects):
        # mark objects as sprites
        if not isinstance(objects, (list, tuple)):
            objects = [objects, ]
        if objects:
            for obj in objects:
                obj.is_sprite = True

    @staticmethod
    def remove_from_sprites(objects):
        # remove objects from sprites
        if not isinstance(objects, (list, tuple)):
            objects = [objects, ]
        if objects:
            for obj in objects:
                obj.is_sprite = False

    @classmethod
    def on_update_sprite_status(cls, context, obj):
        # on update sprite status
        if obj.is_sprite:
            # object became sprite
            cls.track_to_active_camera(
                context=context,
                obj=obj
            )
        else:
            # sprite status cleared
            cls.clear_track_to_camera(
                obj=obj
            )

    @classmethod
    def track_to_active_camera(cls, context, obj):
        # track object to active camera
        if cls.track_constraint_name not in obj.constraints:
            constraint = obj.constraints.new(type='TRACK_TO')
            constraint.target = context.scene.camera
            constraint.name = cls.track_constraint_name

    @classmethod
    def clear_track_to_camera(cls, obj):
        # clear track to camera for object
        track_to_constraint = cls.sprite_track_constraint(
            sprite=obj
        )
        if track_to_constraint:
            # save current transformations
            mat = obj.matrix_world.copy()
            # remove constraint
            obj.constraints.remove(track_to_constraint)
            # set current transformation
            obj.matrix_local = mat

    @classmethod
    def sprite_track_constraint(cls, sprite):
        # get track constraint from sprite
        return next(
            (constraint for constraint in sprite.constraints if constraint.type == 'TRACK_TO' and
                constraint.name == cls.track_constraint_name), None
        )

    @classmethod
    def change_sprites_target(cls, new_target):
        # change sprites target
        sprites = (obj for obj in bpy.data.objects if obj.is_sprite)
        for sprite in sprites:
            track_to_constraint = cls.sprite_track_constraint(
                sprite=sprite
            )
            if track_to_constraint:
                print('change target', new_target)
                track_to_constraint.target = new_target

    @classmethod
    def on_active_camera_change(cls, new_active_camera):
        # on active camera change
        cls.change_sprites_target(
            new_target=new_active_camera
        )
        cls.active_camera_marker = new_active_camera

    @classmethod
    def on_depsgraph_update_post(cls, scene, depsgraph):
        # check for active camera change
        if depsgraph.id_type_updated('SCENE'):
            for obj in depsgraph.updates:
                if isinstance(obj.id, Scene):
                    if scene.camera != cls.active_camera_marker:
                        cls.on_active_camera_change(
                            new_active_camera=scene.camera
                        )

    @classmethod
    def monitor_camera_start(cls):
        # start monitor if active camera changes
        if cls.on_depsgraph_update_post not in depsgraph_update_post:
            depsgraph_update_post.append(cls.on_depsgraph_update_post)

    @classmethod
    def monitor_camera_stop(cls):
        # stop monitor if active camera changes
        if cls.on_depsgraph_update_post in depsgraph_update_post:
            depsgraph_update_post.remove(cls.on_depsgraph_update_post)

    @classmethod
    def register(cls, context):
        # register
        cls.active_camera_marker = context.scene.camera
        # monitor camera changes
        cls.monitor_camera_start()
        # re-register on scene reload
        if sprite_cloud_on_scene_load_post not in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.append(sprite_cloud_on_scene_load_post)

    @classmethod
    def unregister(cls):
        # unregister
        # stop monitor camera changes
        cls.monitor_camera_stop()
        # remove re-registering on scene reload
        if sprite_cloud_on_scene_load_post in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.remove(sprite_cloud_on_scene_load_post)


@persistent
def sprite_cloud_on_scene_load_post(*args):
    # on scene reload
    SpriteCloud.monitor_camera_start()
