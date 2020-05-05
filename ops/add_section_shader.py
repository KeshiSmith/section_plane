import bpy
from mathutils import Vector

from ..global_variables import (
    section_material_name,
    section_node_group_name
)

class AddSectionShaderOperator(bpy.types.Operator):
    """ Add a bound section shader to all selected objects """
    bl_idname = "object.add_section_shader"
    bl_label = "Add Section Shader"
    bl_description = "Add a bound section shader to all selected objects"

    def execute(self, context):
        sp_default_material = bpy.data.materials[section_material_name]
        sp_node_group = bpy.data.node_groups[section_node_group_name]
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:

            # choose selected objects that have a material slot
            if obj.name.startswith("SP_") or \
                obj.type not in ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT']:
                continue

            # add the default material for objects that don't have materials
            if obj.active_material == None:
                obj.active_material = sp_default_material
                continue

            # add the section shader for others
            material_name_set = set()
            for material_name in obj.material_slots.keys():

                # skip materials that have had the section shader
                if material_name.startswith("SP_") or \
                    material_name in material_name_set:
                    continue

                # filter output nodes
                material_name_set.add(material_name)
                material = bpy.data.materials[material_name]
                node_tree = material.node_tree
                output_nodes = [node for node in node_tree.nodes \
                    if node.type == 'OUTPUT_MATERIAL']

                # link the section shader to output nodes
                for output_node in output_nodes:
                    output_socket = output_node.inputs['Surface']
                    surface_links = output_socket.links
                    if len(surface_links) != 0:

                        # filter the from node already have the section shader
                        from_node = surface_links[0].from_node
                        if from_node.type == "GROUP" and \
                            from_node.node_tree.name.startswith("SP_"):
                            continue
                        input_socket = surface_links[0].from_socket

                        # create and link section shader
                        group_node = node_tree.nodes.new('ShaderNodeGroup')
                        group_node.location = \
                            output_node.location + Vector((0, 150))
                        group_node.node_tree = sp_node_group
                        node_tree.links.new(
                            input_socket, 
                            group_node.inputs['Shader']
                        )
                        node_tree.links.new(
                            group_node.outputs['Shader'],
                            output_socket
                        )
                
                # modify alpha properties of materials
                if material.blend_method == 'OPAQUE':
                    material.blend_method = 'CLIP'
                if material.shadow_method == 'OPAQUE':
                    material.blend_method = 'CLIP'
            
        return {'FINISHED'}
