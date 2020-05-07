import bpy

from ..global_variables import(
    lib_path,
    section_collection_name,
    section_material_name,
    section_node_group_name
)

class InitializeOperator(bpy.types.Operator):
    """Initialize and add a section tool"""
    bl_idname = "object.section_plane_initialize"
    bl_label = "Initalize (Add a section tool)"

    def execute(self, context):
        # load section data
        with bpy.data.libraries.load(lib_path) as (data_from, data_to):
            data_to.collections = [section_collection_name]
            data_to.materials = [section_material_name]
            data_to.node_groups = [section_node_group_name]
        section_collection = bpy.data.collections[section_collection_name]
        section_material = bpy.data.materials[section_material_name]
        section_node_group = bpy.data.node_groups[section_node_group_name]
        # use fake user
        section_collection.use_fake_user = True
        section_material.use_fake_user = True
        section_node_group.use_fake_user = True
        # add the collection to current scene
        scene_collection = bpy.context.scene.collection
        scene_collection.children.link(section_collection)
        return {'FINISHED'}
